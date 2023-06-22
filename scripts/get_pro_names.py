#! /usr/bin/env python

# Use this script to populate bot.txt with names from https://www.procyclingstats.com
# pip install beautifulsoup4 country-converter fuzzywuzzy
# scripts/get_pro_names.py -h


from bs4 import BeautifulSoup
import urllib.request
import json
import country_converter as coco
import argparse
import getpass
import os
import sys
import xml.etree.ElementTree as ET
from fuzzywuzzy import process
from fuzzywuzzy import fuzz

base_url = "https://www.procyclingstats.com/rankings.php?filter=Filter"
cc = coco.CountryConverter()

teams = {
    'UAE Team Emirates': {'jersey_name': 'UAE', 'jersey_signature': 1751349769, 'bike_name': 'Colnago Colnago V3RS', 'bike_signature': 3628259811, 'front_wheel_name': 'Enve G23', 'front_wheel_signature': 190867464, 'rear_wheel_name': 'Enve SES 7.8', 'rear_wheel_signature': 886534142},
    'Soudal - Quick Step': {'jersey_name': 'Deceuninck-Quick-Step', 'jersey_signature': 2906189156, 'bike_name': 'Specialized Tarmac SL7', 'bike_signature': 935373427, 'front_wheel_name': 'Roval Rapide CLX', 'front_wheel_signature': 2181416413, 'rear_wheel_name': 'Roval Rapide CLX', 'rear_wheel_signature': 3548735686},
    'Jumbo-Visma': {'jersey_name': 'Team Jumbo-Visma Men 2023', 'jersey_signature': 88214615, 'bike_name': 'Cervelo R5', 'bike_signature': 106535518, 'front_wheel_name': 'Reserve Reserve 25 GR', 'front_wheel_signature': 635220876, 'rear_wheel_name': 'Reserve Reserve 25 GR', 'rear_wheel_signature': 1842698274},
    'Alpecin-Deceuninck': {'jersey_name': 'Deceuninck-Quick-Step', 'jersey_signature': 2906189156, 'bike_name': 'Canyon Aeroad 2015', 'bike_signature': 1520594784, 'front_wheel_name': 'Shimano C50', 'front_wheel_signature': 1742598126, 'rear_wheel_name': 'Shimano C50', 'rear_wheel_signature': 3725678091},
    'Trek - Segafredo': {'jersey_name': 'Trek-Segafredo Women', 'jersey_signature': 1154847422, 'bike_name': 'Trek Madone', 'bike_signature': 4129467727, 'front_wheel_name': 'Bontrager Aeolus5', 'front_wheel_signature': 702195190, 'rear_wheel_name': 'Bontrager Aeolus5', 'rear_wheel_signature': 3594144634},
    'Movistar Team': {'jersey_name': 'Movistar Team', 'jersey_signature': 1842355135, 'bike_name': 'Canyon Aeroad 2015', 'bike_signature': 1520594784, 'front_wheel_name': 'Zipp 202', 'front_wheel_signature': 442607221, 'rear_wheel_name': 'Zipp 808', 'rear_wheel_signature': 214800767},
    'Lotto Dstny': {'jersey_name': 'Lotto', 'jersey_signature': 4130579852},
    'EF Education-EasyPost': {'jersey_name': 'EF Education First', 'jersey_signature': 2349035663, 'bike_name': 'Cannondale System Six', 'bike_signature': 2005280203, 'front_wheel_name': 'HED HED Vanquish RC6 Pro', 'front_wheel_signature': 1791179228, 'rear_wheel_name': 'HED HED Vanquish RC6 Pro', 'rear_wheel_signature': 2913819265},
    'INEOS Grenadiers': {'jersey_name': 'INEOS Grenadiers 2022 Pro', 'jersey_signature': 542207259, 'bike_name': 'Pinarello Dogma F', 'bike_signature': 4208139356, 'front_wheel_name': 'Zwift 50mm Carbon', 'front_wheel_signature': 2060527008, 'rear_wheel_name': 'Zwift 50mm Carbon', 'rear_wheel_signature': 1848192392},
    'Groupama - FDJ': {'jersey_name': 'Groupama FDJ 2023', 'jersey_signature': 2814449542, 'bike_name': 'Specialized Amira S-Works', 'bike_signature': 2662728556, 'front_wheel_name': 'Shimano C50', 'front_wheel_signature': 1742598126, 'rear_wheel_name': 'Shimano C50', 'rear_wheel_signature': 3725678091},
    'Bahrain - Victorious': {'jersey_name': 'Bahrain McLaren', 'jersey_signature': 2155858980, 'bike_name': 'Merida Scultura', 'bike_signature': 3033010663, 'front_wheel_name': 'Zwift 50mm Carbon', 'front_wheel_signature': 2060527008, 'rear_wheel_name': 'Zwift 50mm Carbon', 'rear_wheel_signature': 1848192392},
    'Team DSM': {'jersey_name': 'Team ODZ', 'jersey_signature': 2695025247, 'bike_name': 'Scott Foil', 'bike_signature': 1315158373, 'front_wheel_name': 'Shimano C50', 'front_wheel_signature': 1742598126, 'rear_wheel_name': 'Shimano C50', 'rear_wheel_signature': 3725678091},
    'Team Jayco AlUla': {'jersey_name': 'Team 3R', 'jersey_signature': 493134166, 'bike_name': 'Giant Propel Advanced SL Disc', 'bike_signature': 103914490, 'front_wheel_name': 'Cadex CADEX 42', 'front_wheel_signature': 1497226614, 'rear_wheel_name': 'Cadex CADEX 42', 'rear_wheel_signature': 1347687916},
    'Uno-X Pro Cycling Team': {'jersey_name': 'NTT Pro Cycling Team', 'jersey_signature': 3612223524},
    'Cofidis': {'jersey_name': 'Cofidis 2018', 'jersey_signature': 927604154, 'bike_name': 'Cervelo R5', 'bike_signature': 106535518, 'front_wheel_name': 'Shimano C60', 'front_wheel_signature': 272842014, 'rear_wheel_name': 'Shimano C40', 'rear_wheel_signature': 530549195},
    'Intermarché - Circus - Wanty': {'jersey_name': 'Intermarché–Wanty–Gobert Matériaux', 'jersey_signature': 88121645, 'bike_name': 'Cube Cube Litening', 'bike_signature': 1767548815, 'front_wheel_name': 'Enve SES 2.2', 'front_wheel_signature': 1881778071, 'rear_wheel_name': 'Zwift Handcycle', 'rear_wheel_signature': 2602078812},
    'BORA - hansgrohe': {'jersey_name': 'Bora-Hansgrohe', 'jersey_signature': 321508751, 'bike_name': 'Specialized Tarmac SL7', 'bike_signature': 935373427, 'front_wheel_name': 'Roval Rapide CLX', 'front_wheel_signature': 2181416413, 'rear_wheel_name': 'Roval Rapide CLX', 'rear_wheel_signature': 3548735686},
    'Team Medellín - EPM': {'jersey_name': 'Team 3R', 'jersey_signature': 493134166},
    'Team Arkéa Samsic': {'jersey_name': 'Arkea-Samsic', 'jersey_signature': 598687666, 'bike_name': 'Trek Madone', 'bike_signature': 4129467727, 'front_wheel_name': 'Lightweight Lightweight Meilenstein', 'front_wheel_signature': 2282170788, 'rear_wheel_name': 'Lightweight Lightweight Meilenstein', 'rear_wheel_signature': 3659884507},
    'AG2R Citroën Team': {'jersey_name': 'Team 3R', 'jersey_signature': 493134166, 'bike_name': 'BMC BmcTeamMachine2022', 'bike_signature': 3868468027, 'front_wheel_name': 'Campagnolo Bora Ultra 35', 'front_wheel_signature': 1053884173, 'rear_wheel_name': 'Campagnolo Bora Ultra 35', 'rear_wheel_signature': 1614586487},
    'Astana Qazaqstan Team': {'jersey_name': 'ASTANA PRO TEAM', 'jersey_signature': 1969335676, 'bike_name': 'Giant GiantRevolt2022', 'bike_signature': 2360271970, 'front_wheel_name': 'Shimano C60', 'front_wheel_signature': 272842014, 'rear_wheel_name': 'Shimano C40', 'rear_wheel_signature': 530549195},
    'Israel - Premier Tech': {'jersey_name': 'Israel Premier-Tech', 'jersey_signature': 552170906},
    'TotalEnergies': {'jersey_name': 'Stages Kit', 'jersey_signature': 751130480},
    'Team SD Worx': {'jersey_name': 'Team SD Worx', 'jersey_signature': 1494272741},
    'UAE Team ADQ': {'jersey_name': 'UAE', 'jersey_signature': 1751349769},
    'FDJ - SUEZ': {'jersey_name': 'FDJ Suez 2023', 'jersey_signature': 3360845221},
    'Canyon//SRAM Racing': {'jersey_name': 'SRAM', 'jersey_signature': 2500137555},
    'AG Insurance - Soudal Quick-Step': {'jersey_name': 'Lotto-Soudal', 'jersey_signature': 3103938066},
    'Human Powered Health': {'jersey_name': 'Human Powered Health Fan', 'jersey_signature': 854534852},
    'Team Jumbo-Visma': {'jersey_name': 'Team Jumbo-Visma Men 2023', 'jersey_signature': 88214615},
    'Liv Racing TeqFind': {'jersey_name': 'Liv Racing 2019', 'jersey_signature': 3932519699},
    'Israel Premier Tech Roland': {'jersey_name': 'Israel Premier-Tech', 'jersey_signature': 552170906},
    'EF Education-TIBCO-SVB': {'jersey_name': 'Team EF Education-TIBCO-SVB', 'jersey_signature': 2795352821},
    'Fenix-Deceuninck': {'jersey_name': 'Deceuninck-Quick-Step', 'jersey_signature': 2906189156},
    'CERATIZIT-WNT Pro Cycling': {'jersey_name': 'Ceratizit-WNT', 'jersey_signature': 97975537},
    'St Michel - Mavic - Auber93 WE': {'jersey_name': 'South Africa Elite', 'jersey_signature': 3305515323},
    'Lifeplus Wahoo': {'jersey_name': 'Wahoo', 'jersey_signature': 3553917933},
    'Cofidis Women Team': {'jersey_name': 'Cofidis', 'jersey_signature': 4191972189},
    'Arkéa Pro Cycling Team': {'jersey_name': 'NTT Pro Cycling Team', 'jersey_signature': 3612223524},
    'MAT Atom Deweloper Wrocław': {'jersey_name': 'Race Leader - Rosa', 'jersey_signature': 1295920261},
    'Top Girls Fassa Bortolo': {'jersey_name': 'Clash Of Clubs Blue', 'jersey_signature': 520081294}
}

def get_pros(url, male, get_jersey, get_equipment):
    data = []

    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    site = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(site)

    for td in soup.find_all('td'):
        if td.span and td.contents[0]:
            tmp = {}
            if "flag" in repr(td.contents[0]):
                code = td.span.get_attribute_list("class")[1]
                tmp['country_code'] = cc.convert(names=code, to='ISOnumeric')
                tmp['is_male'] = male
                if td.a:
                    tmp['first_name'] = (td.a.contents[1].strip())
                    tmp['last_name'] = (td.a.span.contents[0])
        if td.a and td.contents[0]:
            if "cu600" in repr(td) and td.a.contents:
                if 'first_name' in tmp:
                    if get_jersey:
                        if td.a.contents[0] in teams:
                            tmp['jersey'] = teams[td.a.contents[0]]['jersey_signature']
                        else:
                            best_match = process.extractOne(td.a.contents[0], jerseys.keys(), scorer=fuzz.token_set_ratio)
                            print ("%s %s : %s - %s" % (tmp['first_name'],tmp['last_name'],td.a.contents[0], best_match))
                            tmp['jersey'] = jerseys[best_match[0]]
                    if get_equipment:
                        if td.a.contents[0] in teams:
                            team = teams[td.a.contents[0]]
                            if 'bike_signature' in team:
                                tmp['bike_frame'] = team['bike_signature']
                            if 'front_wheel_signature' in team:
                                tmp['bike_wheel_front'] = team['front_wheel_signature']
                            if 'rear_wheel_signature' in team:
                                tmp['bike_wheel_rear'] = team['rear_wheel_signature']

                    data.append(tmp)

    return data

tree = ET.parse('../cdn/gameassets/GameDictionary.xml')
root = tree.getroot()
jerseys = {}
for x in root.findall("./JERSEYS/JERSEY"):
    jerseys[x.get('name')] = int(x.get('signature'))

def main(argv):
    global args

    parser = argparse.ArgumentParser(description='Populate Bot names with professional riders')
    parser.add_argument('-n', '--nation', help='Riders from specified nation only', default=False)
    parser.add_argument('-f', '--female', help='Female riders only', default=False, action='store_true')
    parser.add_argument('-m', '--male', help='Male riders only', default=False, action='store_true')
    parser.add_argument('-a', '--alltime', help='Use all time ranking', default=False, action='store_true')
    parser.add_argument('-p', '--pages', help='Number of pages to process', default=1)
    parser.add_argument('-j', '--jersey', help='Get team jerseys', default=False, action='store_true')
    parser.add_argument('-e', '--equipment', help='Get team bike and wheels', default=False, action='store_true')
    args = parser.parse_args()
    url_additions = ""
    url_list = []
    if args.alltime:
        url_additions += "&s=all-time"
    if args.nation:
        url_additions += "&nation="+args.nation
    if args.female:
        url_list = [ { "url": base_url + url_additions + "&p=we", "is_male": False } ]
    elif args.male:
        url_list = [ { "url": base_url + url_additions + "&p=me", "is_male": True } ]
    else:
        url_list = [ { "url": base_url + url_additions + "&p=me", "is_male": True }, { "url": base_url + url_additions + "&p=we", "is_male": False } ]
    if args.pages:
        new_url_list = url_list.copy()
        for x in range(1,int(args.pages)):
            offset = str(x*100)
            for url in url_list:
                new_url_list += [ { "url": url['url'] + "&offset=" + offset, "is_male": url['is_male'] }]
        url_list = new_url_list.copy()

    total_data = {}
    total_data['riders'] = []
    for item in url_list:
        total_data['riders'] = total_data['riders'] + get_pros(item['url'], item['is_male'], args.jersey, args.equipment)
    total_data['body_types'] = [16, 48, 80, 272, 304, 336, 528, 560, 592]
    total_data['hair_types'] = [25953412, 175379869, 398510584, 659452569, 838618949, 924073005, 1022111028, 1262230565, 1305767757, 1569595897, 1626212425, 1985754517, 2234835005, 2507058825, 3092564365, 3200039653, 3296520581, 3351295312, 3536770137, 4021222889, 4179410997, 4294226781]
    total_data['facial_hair_types'] = [248681634, 398510584, 867351826, 1947387842, 2173853954, 3169994930, 4131541011, 4216468066]

    with open('bot.txt', 'w') as outfile:
        json.dump(total_data, outfile, indent=2)

if __name__ == '__main__':
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        pass
    except SystemExit as se:
        print("ERROR:", se)

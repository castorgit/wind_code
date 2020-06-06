"""
.. module:: GenerateExpRangeSites

GenerateExpSites
*************

:Description: GenerateRangeExpSites

    Generates and uploads to the DB configurations using --config configuration
    it begins at file --isite and ends at section --fsite
    It uses files with suffix --suff


:Authors: HPAI-BSC
    

:Version: 

:Created on: 07/06/2018 15:45 
modified to include --listsites from a csv file

"""

import argparse
from time import time

from Wind.Misc import load_config_file
from Wind.Private.DBConfig import mongoconnection, mongolocaltest
from Wind.Config import wind_data_path
from pymongo import MongoClient
import pandas as pd
from tqdm import tqdm
import sys


# nsites  0 - 126691
__author__ = 'HPAI-BSC'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', default=None, required=True, help='Experiment configuration')
    parser.add_argument('--exp', default=None, required=True, help='Experiment name')
    parser.add_argument('--test', action='store_true', default=False, help='Print the number of configurations')
    parser.add_argument('--suff', type=int, default=False, required=True, help='Datafile suffix')
    parser.add_argument('--testdb', action='store_true', default=False, help='Use test database')
    parser.add_argument('--listsites', default=None, required=True, help='sites csv')
    
    args = parser.parse_args()


    config = load_config_file(args.config)


    if args.test:
        print(args.fsite - args.isite + 1)
    else:
        if args.testdb:
            mongoconnection = mongolocaltest
        client = MongoClient(mongoconnection.server)
        db = client[mongoconnection.db]
        if mongoconnection.passwd is not None:
            db.authenticate(mongoconnection.user, password=mongoconnection.passwd)
        col = db[mongoconnection.col]
        
        if args.listsites != None:
            ids = int(time())
            print(wind_data_path)
            df = pd.read_csv(wind_data_path+args.listsites)

            for i, row in df.iterrows():
              # format site = number of site
              site = int(row.site)
              print(f'{site//500}-{site}-{args.suff:02d}')
              config['data']['datanames'] = [f'{site//500}-{site}-{args.suff:02d}']
              site = config['data']['datanames'][0].split('-')
              config['site'] = '-'.join(site[:2])
              config['status'] = 'pending'
              config['experiment'] = args.exp
              config['result'] = []
              config['_id'] = f"{ids}{i:05d}{int(site[1]):06d}"
              col.insert_one(config)
            
            
            
            
            
        else:
           ids = int(time())
           for i, site in tqdm(enumerate(range(args.isite, args.fsite + 1))):
              config['data']['datanames'] = [f'{site//500}-{site}-{args.suff}']
              site = config['data']['datanames'][0].split('-')
              config['site'] = '-'.join(site[:2])
              config['status'] = 'pending'
              config['experiment'] = args.exp
              config['result'] = []
              config['_id'] = f"{ids}{i:05d}{int(site[1]):06d}"
              col.insert_one(config)


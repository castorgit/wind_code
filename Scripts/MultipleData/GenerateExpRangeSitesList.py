"""
.. module:: GenerateExpRangeSites

GenerateExpSites
*************

:Description: GenerateRangeExpSites

    Generates and uploads to the DB configurations using --config configuration
    it generates configuration from a list (Pandas dataframe with one column)
    It uses files with suffix --suff


:Authors: HPAI-BSC
: Modified: JM
    

:Version: 

:Created on: 07/06/2018 15:45 

"""

import argparse
from time import time
import sys

from Wind.Misc import load_config_file
from Wind.Private.DBConfig import mongoconnection, mongolocaltest
from pymongo import MongoClient
from tqdm import tqdm
import pandas as pd


# nsites  0 - 126691
__author__ = 'HPAI-BSC'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', default=None, required=True, help='Experiment configuration')
    parser.add_argument('--exp', default=None, required=True, help='Experiment name')
    parser.add_argument('--test', action='store_true', default=False, help='Print the number of configurations')
    parser.add_argument('--suff', type=int, default=12, help='Datafile suffix')
    parser.add_argument('--testdb', action='store_true', default=False, help='Use test database')
    parser.add_argument('--listsites', default=None, required=True, help='List of selected sites')
    args = parser.parse_args()

    try:
       list_sites = pd.read_csv(args.listsites,index_col=0)
    except:
       raise NameError("File", args.listsites, " with list sites does not exist")
    
    config = load_config_file(args.config)

    if args.test:
        print("Number of sites", list_sites['0'].count())
    else:
        if args.testdb:
            mongoconnection = mongolocaltest
        client = MongoClient(mongoconnection.server)
        db = client[mongoconnection.db]
        if mongoconnection.passwd is not None:
            db.authenticate(mongoconnection.user, password=mongoconnection.passwd)
        col = db[mongoconnection.col]

        ids = int(time())
        for i, site in list_sites.iterrows():
            config['data']['datanames'] = [f'{site[0]}-{args.suff}']
            site = config['data']['datanames'][0].split('-')
            print('site :', site)
            config['site'] = '-'.join(site[:2])
            config['status'] = 'pending'
            config['experiment'] = args.exp
            config['result'] = []
            config['_id'] = f"{ids}{i:05d}{int(site[1]):06d}"
            col.insert_one(config)


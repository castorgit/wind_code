"""
.. module:: GenerateExpSitesSelect

GenerateExpSitesSelect
*************

:Description: GenerateExpSitesSelect

    Generates and uploads to the DB configurations using --config for the sites with the --upper best and --lower worst results for
    the experiment --exp with architecture --mode

    The purpose is to rerun the best/worst experiments

:Authors: HPAI-BSC
    

:Version: 

:Created on: 07/06/2018 15:45 

"""

import argparse
from time import time

from Wind.Misc import load_config_file
from Wind.Private.DBConfig import mongoconnection, mongolocaltest
from pymongo import MongoClient
import numpy as np
from tqdm import tqdm

__author__ = 'HPAI-BSC'



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', default='configrnnseq2seq', help='Experiment configuration')
    parser.add_argument('--test', action='store_true', default=False, help='Only print the number of configurations and exit')
    parser.add_argument('--upper', type=int, help='Select upper best', default=100)
    parser.add_argument('--lower', type=int, help='Select lower worst', default=100)
    parser.add_argument('--exp', help='Experiment type', default="eastwest9597")
    parser.add_argument('--mode', help='Architecture mode', default='seq2seq')
    parser.add_argument('--suff', help='Datafile suffix', default='12')
    parser.add_argument('--testdb', action='store_true', default=False, help='Use test database')

    args = parser.parse_args()
    config = load_config_file(args.config)

    if args.testdb:
        mongoconnection = mongolocaltest
    client = MongoClient(mongoconnection.server)
    db = client[mongoconnection.db]
    if mongoconnection.passwd is not None:
        db.authenticate(mongoconnection.user, password=mongoconnection.passwd)
    col = db[mongoconnection.col]

    exps = col.find({'experiment': args.exp, 'arch.mode': args.mode})

    lexps = []
    for e in exps:
        lexps.append((np.sum(np.array(e['result'])[:, 1]), e['site']))

    lupper = [v for _, v in sorted(lexps, reverse=True)][:args.upper]
    llower = [v for _, v in sorted(lexps, reverse=False)][:args.lower]
    lexps = []
    lexps.extend(lupper)
    lexps.extend(llower)

    if args.test:
        for i, e in enumerate(lexps):
            print(i, e)
    else:
        ids = int(time())
        for i, site in tqdm(enumerate(lexps)):
            config['site'] = site
            config['data']['datanames'] = [f"{site}-{args.suff}"]
            config['status'] = 'pending'
            config['result'] = []
            config['_id'] = f"{ids}{i:04d}%d%"
            col.insert_one(config)


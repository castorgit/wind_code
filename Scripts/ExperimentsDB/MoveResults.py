"""
.. module:: MoveResults

MoveResults
*************

:Description: MoveResults

    Moves experiments from one database to another

:Authors: HPAI-BSC
    

:Version: 

:Created on: 10/12/2018 7:13 

"""
from Wind.Private.DBConfig import mongoconnection, mongolocal, mongolocaltest, mongolocalmeasures
from pymongo import MongoClient
import argparse
from tqdm import tqdm

__author__ = 'HPAI-BSC'

collections = {'test':mongolocaltest, 'production':mongolocal, 'measures':mongolocalmeasures}

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--exp', help='Experiment type', default='convos2s')
    parser.add_argument('--rexp', help='Rename Experiment', default=None)
    parser.add_argument('--fr', default='test', choices=['test', 'production', 'measures'], help='Move from collection')
    parser.add_argument('--to', default='production', choices=['test', 'production', 'measures'],help='Move to collection')
    parser.add_argument('--noupdate', action='store_true', default=False, help='Do not change anything')

    args = parser.parse_args()

    if args.rexp is None:
        args.rexp = args.exp

    mprod = collections[args.fr]
    mtest = collections[args.to]

    client = MongoClient(mprod.server)

    db = client[mprod.db]
    if mprod.user is not None:
        db.authenticate(mprod.user, password=mprod.passwd)
    col = db[mprod.col]

    clientlocal = MongoClient(mtest.server)

    dblocal = clientlocal[mtest.db]
    collocal = dblocal[mtest.col]

    configs = col.find({'experiment': args.exp})

    for conf in tqdm(configs):
        if not args.noupdate:
            if args.rexp:
                conf['experiment'] = args.rexp

            confex = collocal.find_one({'_id': conf['_id']})
            if confex is not None:
                collocal.delete_one({'_id': conf['_id']})

            collocal.insert_one(conf)


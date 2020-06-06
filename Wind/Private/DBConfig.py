"""
.. module:: DBConfig

DBConfig
*************

:Description: DBConfig

   Tiene los parametros de JM P50 para mongodb

:Authors: jaume manero
Configuración para P40


:Version:

:Created on: 15/02/2017 9:21

"""

__author__ = 'HPAI-BSC'


class MongoData:
    def __init__(self, server, db, user, passwd, collect):
        self.server = server
        self.db = db
        self.user = user
        self.passwd = passwd
        self.col = collect


# la base de datos en el P50 no tiene password ni na de na                         
mongoconnection = MongoData('mongodb://localhost:27017/', 'Wind', None, None, 'Wind')

mongolocalmeasures = MongoData('mongodb://localhost:27017/', 'WindMeasures', None, None,
                            'WindMeasures')
mongolocal =      MongoData('mongodb://localhost:27017/', 'Wind', None, None,'Wind')
mongoremote =      MongoData('mongodb://localhost:27017/', 'Wind', None, None,'Wind')
mongolocaltest =      MongoData('mongodb://localhost:27017/', 'Wind', None, None,'Wind')
#mongoconnection = MongoData('mongodb://localhost:27017/', 'Database', 'User', 'Password',
#   'Collection')
# Mongo local connection
#mongolocal = MongoData('mongodb://localhost:27017/', 'Database', 'User', 'Password',
#                            'Collection')

# Token for mapbox.com to be able to plot maps with geographical information with plotly
mapbox_token = ""
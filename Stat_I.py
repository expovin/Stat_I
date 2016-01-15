#!/usr/bin/python
import StatisticalFunctions
import config

import tornado.escape
import tornado.ioloop
import tornado.web
import logging
import json


import Stat_I

#log=config.Log


'''
    Stat_I
    This Module contain a number of statistical function related to the descriptive statstics.

	Project location :  https://github.com/expovin/KMLRegionRetriver
'''

'''
     POST:getReagionFromCoordsMulti - /getReagionFromCoordsMulti - JSON
     This Method expect a JSON with the list of all the Coords to looking for and return the complete result set containing
     a Region for each Coordinates.
'''
class PearsonCorrelation(tornado.web.RequestHandler):
    def post(self):
        tdata = self.request.body.decode('utf-8')
        data = eval(tdata)
        self.add_header('Access-Control-Allow-Origin', '*')
        self.add_header('Access-Control-Allow-Methods','GET, POST, OPTIONS')
        self.add_header('Access-Control-Allow-Headers','Content-Type,X-Requested-With')

        # Le liste che contengono i valori delle due colonne
        x = []
        y = []

        for ele in data['Data']:
            x.append(data['Data'][ele][0])
            y.append(data['Data'][ele][1])

        pc = StatisticalFunctions.calculate_pearson(x, y)

        response = {
            'Method':'PearsonCorrelation',
            'Paerson Correlation' : pc
        }
        self.write(response)

    def options(self, *args, **kwargs):
        self.add_header('Access-Control-Allow-Origin', '*')
        self.add_header('Access-Control-Allow-Methods','GET, POST, OPTIONS')
        self.add_header('Access-Control-Allow-Headers','Content-Type,X-Requested-With')
        response ={'TEST':'Options'}
        self.write(response)


'''
    GET:info - /info - JSON
    Just return some info about the RESTServer such as version, author and last build date
'''

class VersionHandler(tornado.web.RequestHandler):
    def get(self):
        i=config.Info
        response = { 'author':i.author,
                     'contact':i.contact,
                     'last build':i.build,
                     'version': i.version
                   }
        self.write(response)



application = tornado.web.Application()

if (__name__=='__main__'):
    logging.basicConfig(filename='logFile.txt', format='%(asctime)s\t%(module)s:%(funcName)s\t%(levelname)s\t%(lineno)d\t%(message)s', level=logging.INFO)
    app = open('application.conf','r')
    appDict = {}
    appDict = eval(app.read())
    for app in appDict['Application']:
        application.add_handlers(r".*$",[app,])

    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

    print(appDict)


import enum
import math
import time
import argparse

import numpy
from ibapi.client import EClient

# types
from ibapi.common import * # @UnusedWildImport
from ibapi.contract import * # @UnusedWildImport
from ibapi.order import *
from ibapi.wrapper import EWrapper, inspect

import pandas as pd

#from CoreFinta import TA
from ContractSamples import ContractSamples

from DBHelperMay import DBHelper

#tick_freq_inp = input("What frequency of tickdata do you want?: ")


class GooseIndicator(EWrapper, EClient):
    def __init__(self):
        super().__init__()
        EWrapper.__init__(self)
        EClient.__init__(self, wrapper=self)
        self.nextValidOrderId = None
        self.simplePlaceOid = None
        self.connState = None
        self.conn = None


    def nextOrderId(self):
        oid = self.nextValidOrderId
        return oid

    def deriveIndicatorAndPlaceOrder(self):
        #global tick_freq_inp

        # make the input string into an integer
        #tick_periods = int(tick_freq_inp)
        actionType = self.applyMACDStrategy()
        return actionType


    def getIBClient(self):
        print ("getIBClient")

        cmdLineParser = argparse.ArgumentParser("api tests")
        cmdLineParser.add_argument("-p", "--port", action="store", type=int,
                                   dest="port", default=7497, help="The TCP port to use")
        args = cmdLineParser.parse_args()
        self.connect("127.0.0.1", args.port, clientId=0)


    def applyMACDStrategy(self):
        db = DBHelper()

        df = db.getDataInPandaDF()
        print(df)


def main():

    app = GooseIndicator()
    try:
        #app.getMACD()
        app.deriveIndicatorAndPlaceOrder()
    except:
        raise


if __name__ == "__main__":
    main()


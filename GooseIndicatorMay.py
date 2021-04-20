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

from CoreFinta import TA
from ContractSamples import ContractSamples

from DBHelperMay import DBHelper

tick_freq_inp = input("What frequency of tickdata do you want?: ")

class Signal(enum.Enum):
   BUY = "BUY"
   SELL = "SELL"
   DO_NOTHING="DO NOTHING"


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
        global tick_freq_inp

        # make the input string into an integer
        tick_periods = int(tick_freq_inp)
        actionType = self.applyMACDStrategy(tick_periods)
        return actionType


    def getIBClient(self):
        print ("getIBClient")

        cmdLineParser = argparse.ArgumentParser("api tests")
        cmdLineParser.add_argument("-p", "--port", action="store", type=int,
                                   dest="port", default=7497, help="The TCP port to use")
        args = cmdLineParser.parse_args()
        self.connect("127.0.0.1", args.port, clientId=0)

    def getWTDEHMA(self, tick_size: int):
        # len = int(num_periods_inp)
        print("test")
        len = 6
        len_half = numpy.round(len / 2)
        len_sqrt = numpy.round(math.sqrt(len))

        db = DBHelper()
        #
        tick_freq = int(tick_freq_inp)
        #
        df = db.getDeltaInPandaDF(len * 2, tick_freq)

        df["ema_slow"] = TA.EMA(df, len, "price")
        df["ema_fast"] = TA.EMA(df, len_half, "price")

        df["ema_diff"] = 4 * df["ema_fast"] - df["ema_slow"]

        df["ehma"] = TA.EMA(df, len_sqrt, "ema_diff")

        df["wma"] = TA.WMA(df, len, "price")

        df["wtdema_slow"] = TA.EMA(df, len, "wma")
        df["wtdema_fast"] = TA.EMA(df, len_half, "wma")

        df["wtdema_diff"] = 2 * df["wtdema_fast"] - df["wtdema_slow"]

        df["wtdehma"] = TA.EMA(df, len_sqrt, "wtdema_diff")
        # TODO: Fix standard HMA formula
        df["wtdehma_standard"] = TA.HMA(df, len, "ema_slow")
        #cleanup dataframe
        # df.drop(columns=['wtdehma_standard'])
        # print("df", df)
        return df

    def getZlema(self, tick_size: int):
        len = int(14)

        db = DBHelper()
        #
        df = db.getDeltaInPandaDF(len * 2, tick_size)

        df["zlema"] = TA.ZLEMA(df, len)
        # print(df)
        return df[['id','zlema']]

    def getMACD(self, tick_size: int):
        len = float(5)
        period_fast_var=float(8)
        period_slow_var=float(16)
        db = DBHelper()
        #
        df = db.getDeltaInPandaDF(5 * 2, tick_size)

        df[['MACD', 'MACD_signal']] = TA.MACD(df, period_fast=period_fast_var, period_slow=period_slow_var, signal=len)
        df[["MACD_standard","MACD_standard_signal"]] = TA.MACD(df)
        print(df[['id','price','MACD', 'MACD_signal',"MACD_standard","MACD_standard_signal"]])
        return df
        #return df[['id','MACD', 'MACD_signal',"MACD_standard","MACD_standard_signal"]]

    def applyWTDEHMAOverZLEMAStrategy(self,tick_size: int):

        #print("fetching rows after id", last_row_id_of_previous_iteration)
        df_w = self.getWTDEHMA(tick_size)
        df = df_w[['id','price','time','wtdehma','wtdehma_standard']]
        df_z = self.getZlema()

        print('vanilla df',df)
        df=pd.merge(df, df_z, on=['id']) #Merge wtdehma with zlema
        print('dataframe merged with zlema',df)

        print(df[['id','price','wtdehma','wtdehma_standard','zlema']])
        actionType = Signal.DO_NOTHING
        print(df)

        l1 = df['price'].__len__()
        last_index = l1 - 1

        if df.at[last_index, "wtdehma"] > df.at[last_index, 'zlema'] :
            actionType = Signal.BUY
        elif df.at[last_index, "zlema"] > df.at[last_index, 'wtdehma']:
            actionType = Signal.SELL

        print("applyWTDEHMAOverZLEMA:: actionType :: ",actionType)
        return actionType

    def applyMACDStrategy(self,tick_size: int):
        df = self.getMACD(tick_size)

        # print(df[['id','price','wtdehma','wtdehma_standard','zlema','MACD', 'MACD_signal',"MACD_standard","MACD_standard_signal"]])
        print(df[['id', 'price', 'MACD', 'MACD_signal', "MACD_standard", "MACD_standard_signal"]])
        actionType = Signal.DO_NOTHING
        print(df)

        l1 = df['price'].__len__()
        last_index = l1 - 1

        if df.at[last_index, "MACD"] > df.at[last_index, 'MACD_signal']:
            actionType = Signal.BUY
        elif df.at[last_index, "MACD"] < df.at[last_index, 'MACD_signal']:
            actionType = Signal.SELL

        print("applyMACDStrategy:: actionType :: ",actionType)
        return actionType

def main():

    app = GooseIndicator()
    try:
        #app.getMACD()
        app.deriveIndicatorAndPlaceOrder()
    except:
        raise


if __name__ == "__main__":
    main()


import pandas as pd
from yahoo_fin import stock_info as si
from datetime import date
from datetime import timedelta

class master:
    def get_sma30(self, ticker):
        sma30 = si.get_data(ticker, interval="1d")["close"][-80:].mean()
        return sma30

    def get_sma50(self, ticker):
        sma50 = si.get_data(ticker, interval="1d")["close"][-80:].mean()
        return sma50

    def get_sma100(self, ticker):
        sma100 = si.get_data(ticker, interval="1d")["close"][-130:].mean()
        return sma100

    def get_sma200(self, ticker):
        sma200 = si.get_data(ticker, interval="1d")["close"][-230:].mean()
        return sma200
    def volatility(self, ticker):
        c = si.get_data(ticker)['adjclose'][-1]
        for i in si.get_data(ticker)["adjclose"][-10:]:
            if i[0] > c[0] +10 or i[0] < c[0]-10:
                return True
            else:
                c = i
        return False

    def get_body(self, ticker, ):
        #return dictionary
        data =  {
            "high": si.get_data(ticker,)["high"], 
            "low": si.get_data(ticker,)["low"],
            "close": si.get_data(ticker,)["low"],
            "adjclose": si.get_data(ticker, )['adjclose'],
            }
        return data
    def get_sentiment(self, ticker):
        positive = 0
        negative = 0
        first = {
            "high": si.get_data(ticker,)["high"][-3], 
            "low": si.get_data(ticker,)["low"][-3],
            "close": si.get_data(ticker,)["low"][-3],
            "adjclose": si.get_data(ticker, )['adjclose'][-3],
            }
        second = {
            "high": si.get_data(ticker,)["high"][-2], 
            "low": si.get_data(ticker,)["low"][-2],
            "close": si.get_data(ticker,)["low"][-2],
            "adjclose": si.get_data(ticker, )['adjclose'][-2],
            }
        third = {
            "high": si.get_data(ticker,)["high"][-1:], 
            "low": si.get_data(ticker,)["low"][-1:],
            "close": si.get_data(ticker,)["low"][-1:],
            "adjclose": si.get_data(ticker, )['adjclose'][-1:],
            }
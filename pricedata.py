# -*- coding: UTF-8 -*-
import requests
from io import StringIO
import pandas as pd
import numpy as np
import datetime as dt
import csv

def sleeptime(hour,min,sec):
    return hour*3600 + min*60 + sec;
# 網址日期範圍
startdate = dt.datetime(2021, 1, 1)
enddate = dt.datetime(2021, 1, 5)
totaldays = (enddate - startdate).days + 1

my_headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
# 日期迴圈
for daynumber in range(totaldays):
    Datestring = (startdate + dt.timedelta(days=daynumber))
    datestr = Datestring.strftime("%w")
    if (datestr != "0" and datestr != "6"):
        d = Datestring.strftime("%Y%m%d")
        # 利用requests下載資料
        r = requests.get(
            'http://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + d + '&type=24')
        try:
            df = pd.read_csv(StringIO("\n".join([i.translate({ord(c): None for c in ' '})
                                                for i in r.text.split('\n')
                                                if len(i.split('",')) == 17 and i[0] != '='])), headers = my_headers)


            print("日期:", d)
            print(df)
            sleeptime()
        except:
            continue

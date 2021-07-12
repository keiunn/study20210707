# -*- coding: UTF-8 -*-
from pytrends.request import TrendReq
import pandas as pd
import numpy as np
np.set_printoptions(threshold=np.inf)
import datetime as dt
import csv
import random
import pytrends
from pytrends import dailydata

#from pytrendsdaily import getDailyData
keywords = ['麗正','聯電','華泰','台積電','旺宏','光罩','茂矽','華邦電','順德','矽統','菱生','瑞昱','威盛','凌陽','南亞科','統懋','偉詮電','超豐','京元','創見','聯發科','義隆','強茂','晶豪科','聯陽','嘉晶','聯詠','智原','揚智','立萬利','聯傑','景碩','虹冠電','京鼎','創意','晶相光','台勝科','誠創','敦泰','辛耘','通嘉','世芯','達能','日月光','新唐','凌通','天鈺','十銓','立積','祥碩','界霖','松翰','盛群','力成','迅杰','矽格','同欣電','矽力','訊芯','穎崴','捷敏','愛普','晶心科','易華電','虹 揚 ky','威鋒','矽創','昇陽','致新','華東','福懋科','南茂','富鼎','宇瞻']
ST_list = []
pd.set_option('display.max_rows', 50000) #最大行数
pd.set_option('display.max_columns', 50000) #最大列数

for i in range(1,74):
    k = keywords[i]
    df = dailydata.get_daily_data(k, 2017, 6, 2021, 6, geo = 'TW')
    #pytrend.build_payload(kw_list=k,cat=0,timeframe='today 1-m',geo='TW',gprop='')
    ST_list.append('\n')
    ST_list.append(df)



#with open('output.csv', 'w', newline='') as csvfile:
#    writer = csv.writer(csvfile)
#    writer.writerow(ST_list)

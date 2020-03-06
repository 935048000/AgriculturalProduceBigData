# -*- coding: utf-8 -*-
# @Time : 2020-3-6 9:57
# @Author : chenhao
# @FileName: crawler.py
# @Software: PyCharm
# @E-Mail: chenhao886640@gmail.com

# 项目依赖包
from web.utils import load_config
from web.logger import setup_log
from web.utils import mysql
import pandas as pd
import pymysql
from sqlalchemy import create_engine
import numpy as np

# 爬虫依赖包
from urllib.request import urlopen
import urllib
from bs4 import BeautifulSoup
from datetime import datetime
from re import sub

config = load_config ()
_logger = setup_log (__name__)
mysql = mysql (config['mysql'])


class priceFormat:
    """
    产品价格处理类
    
    """
    
    def __init__(self):
        # 时间
        self.dateList = []
        
        #  产品名称
        self.prdNameList = []
        
        # 最低价格
        self.print0List = []
        
        # 最高价格
        self.print1List = []
        
        # 平均价格
        self.print2List = []
        
        # 批发市场
        self.bazaarList = []
        
        self.AllDataList = []
        
        self.AllRawDataList = []
        
        self.AllDataList = []
    
    def getPriceData(self, pages):
        """
        爬虫获取价格数据
        
        :return:
            list date_raw_list:时间
            list price_raw_list:价格
            list bazaar_raw_list:市场
        """
        try:
            url = "http://www.vegnet.com.cn/Channel/Price?page=%d&flag=12&ename=MaLingShu" % pages
            user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'
            headers = {
                'User-Agent': user_agent
            }
            req = urllib.request.Request (url, headers=headers, method='GET')
            page = urllib.request.urlopen (req).read ().decode ('utf-8')
            bsObj = BeautifulSoup (page, "html.parser")
            userInfoObj = bsObj.find ("div", {"class": "jxs_list green"})
            self._date_raw_list = userInfoObj.find_all ("span", {"class": "k_1"})
            self._price_raw_list = userInfoObj.find_all ("span", {"class": "k_2"})
            self._bazaar_raw_list = userInfoObj.find_all ("span", {"class": "k_3"})
            _logger.info ("成功页码=%d" % pages)
        except:
            _logger.error ("错误页码=%d" % pages)
        
        self.AllRawDataList.append (self._date_raw_list)
        self.AllRawDataList.append (self._price_raw_list)
        self.AllRawDataList.append (self._bazaar_raw_list)
        
        return self.AllRawDataList
    
    def formatPriceData(self, AllRawDataList):
        """
        格式化结果数据
        :return:
        """
        
        for i in range (0, len (AllRawDataList[0])):
            # print (AllRawDataList[0][i].text[1:-1])
            # print (AllRawDataList[2][i].text)
            self.dateList.append (AllRawDataList[0][i].text[1:-1])
            self.bazaarList.append (AllRawDataList[2][i].text)
            self.prdNameList.append (AllRawDataList[1][i * 5:(i + 1) * 5][0].text)
            self.print0List.append (AllRawDataList[1][i * 5:(i + 1) * 5][1].text)
            self.print1List.append (AllRawDataList[1][i * 5:(i + 1) * 5][2].text)
            self.print2List.append (AllRawDataList[1][i * 5:(i + 1) * 5][3].text)
        
        self.AllDataList.append (self.dateList)
        self.AllDataList.append (self.prdNameList)
        self.AllDataList.append (self.print0List)
        self.AllDataList.append (self.print1List)
        self.AllDataList.append (self.print2List)
        self.AllDataList.append (self.bazaarList)
        
        return self.AllDataList
    
    def writePriceData(self,tempList2):
        """
        
        :param tempList2: 格式化后的数据
        :return:
        """
        Wcon = create_engine (
            'mysql+pymysql://ch:learn_project@49.235.241.182:3306/bigdata')


        # print (len (tempList2[0]))
        datatable = pd.DataFrame ({"date": tempList2[0],
                                     "products": tempList2[1],
                                     "mini_price": list (map (float, tempList2[2])),
                                     "max_price": list (map (float, tempList2[3])),
                                     "avg_price": list (map (float, tempList2[4])),
                                     "bazaar": tempList2[5]})

        # 字符串转浮点
        datatable.mini_price = datatable.mini_price.astype (np.float)
        datatable.max_price = datatable.max_price.astype (np.float)
        datatable.avg_price = datatable.avg_price.astype (np.float)

        # 写入数据库
        try:
            datatable.to_sql (name="prd_price", con=Wcon, if_exists='append', index=False)
            _logger.info ("本次写入数据行数=%d" % len(tempList2[0]))
        except:
            _logger.error ("写入失败数据=%s"%tempList2)

        self.__init__ ()
        return 0


def main():
    """
    主函数
    
    :return:
    """
    pf = priceFormat ()
    for i in [1, 2]:
        pf.__init__ ()
        tempList = pf.getPriceData (i)
        tempList2 = pf.formatPriceData (tempList)
        pf.writePriceData(tempList2)
    
    return 0


if __name__ == '__main__':
    pass
    # pf = priceFormat ()
    # Wcon = create_engine (
    #     'mysql+pymysql://ch:learn_project@49.235.241.182:3306/bigdata')
    #
    # for i in [1, 2]:
    #     pf.__init__ ()
    #     tempList = pf.getPriceData (i)
    #     tempList2 = pf.formatPriceData (tempList)
    #     print (len (tempList2[0]))
    #     t_datatable = pd.DataFrame ({"date": tempList2[0],
    #                                  "products": tempList2[1],
    #                                  "mini_price": list(map(float,tempList2[2])),
    #                                  "max_price": list(map(float,tempList2[3])),
    #                                  "avg_price": list(map(float,tempList2[4])),
    #                                  "bazaar": tempList2[5]})
    #
    #     t_datatable.mini_price = t_datatable.mini_price.astype (np.float)
    #     t_datatable.max_price = t_datatable.max_price.astype (np.float)
    #     t_datatable.avg_price = t_datatable.avg_price.astype (np.float)
    #
    #     t_datatable.to_sql (name="prd_price", con=Wcon, if_exists='append', index=False)

    main ()
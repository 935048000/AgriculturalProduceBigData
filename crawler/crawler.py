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
    
    def getPriceData(self, pages):
        """
        爬虫获取价格数据
        
        :return:
        date_raw_list
        """
        url = "http://www.vegnet.com.cn/Channel/Price?page=%d&flag=12&ename=MaLingShu" % pages
        user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'
        headers = {
            'User-Agent': user_agent
        }
        req = urllib.request.Request (url, headers=headers, method='GET')
        page = urllib.request.urlopen (req).read ().decode ('utf-8')
        bsObj = BeautifulSoup (page, "html.parser")
        userInfoObj = bsObj.find ("div", {"class": "jxs_list green"})
        date_raw_list = userInfoObj.find_all ("span", {"class": "k_1"})
        price_raw_list = userInfoObj.find_all ("span", {"class": "k_2"})
        bazaar_raw_list = userInfoObj.find_all ("span", {"class": "k_3"})

        return date_raw_list, price_raw_list, bazaar_raw_list
    
    def formatPriceData(self):
        """
        格式化结果数据
        :return:
        """
        pass
    
    def writePriceData(self):
        """
        价格数据写入数据库
        :return:
        """
        pass


def main():
    """
    主函数
    
    :return:
    """
    
    pass


if __name__ == '__main__':
    pass

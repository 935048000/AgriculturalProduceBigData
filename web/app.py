from web.utils import load_config
from web.logger  import setup_log
from flask import Flask, request, render_template, session, redirect, url_for
from web.utils import mysql,returnData
import math
from flask_paginate import Pagination, get_page_parameter



config = load_config()
_logger = setup_log(__name__)
app = Flask(__name__)
app.config['SECRET_KEY'] = 'test'
mysql = mysql(config['mysql'])

# 模板
# @app.route("/user", methods=['POST', 'GET'])
# def user():

# 获取指定参数：
# request.form[""]
# 获取指定参数并生成默认值：
# request.form.get("key", type=str, default=None)

#     login, userid = False, None
#     if 'userid' not in session:
#         return redirect(url_for('loginForm'))
#     else:
#         login, userid = True, session['userid']
#     userinfo = []
#     try:
#         sql = "select UserID,Location,Age from User where UserID='{}'".format(userid)
#         userinfo = mysql.fetchone_db(sql)
#         userinfo = [v for k, v in userinfo.items()]
#     except Exception as e:
#         logger.exception("select UserInfo error: {}".format(e))
#     return render_template("UserInfo.html",
#                            login=login,
#                            useid=userid,
#                            userinfo=userinfo)



@app.route("/projectInfo",methods=["POST","GET"])
def projectInfo():
    """
    项目信息，测试接口
    :return:
    """
    return "本项目是一个农产品大数据接口，通过爬取网络相关产品数据，汇总+分析得到完整的数据模型。"

@app.route("/parameterTest",methods=["POST"])
def parameterTest():
    """
    传参测试接口
    :return:
    """
    
    return returnData("0","成功",str(request.form.to_dict()))


## 产品信息接口

@app.route ("/prdInfo", methods=["POST"])
def prdInfo():
    """
    
    :return:
    """
    try:
        sql = """SELECT * FROM prd_products_info"""
        _prdinfo = mysql.fetchall_db(sql)
        _logger.info(_prdinfo)
    except Exception as e:
        _logger.exception("error: {}".format(e))
        return returnData ("404", "失败", None)
    
    return returnData ("0", "成功", _prdinfo)


## 虫害病信息接口
@app.route ("/diseases/info", methods=["POST"])
def diseasesInfo():
    """
    
    :return:
    """
    try:
        sql = """SELECT
                SUBSTRING(diseases_name,4,100) as diseases_name
                FROM
                prd_diseases"""
        _rdata = mysql.fetchall_db (sql)
        _logger.info(_rdata)
    except Exception as e:
        _logger.exception ("error: {}".format (e))
        return returnData ("404", "失败", None)
    
    return returnData ("0", "成功", _rdata)

## 技术文章信息接口
@app.route ("/article/info", methods=["POST"])
def articleInfo():
    """

    :return:
    """
    try:
        sql = """SELECT
                article_title,article_url,article_source,DATE_FORMAT(article_date,"%Y-%m-%d") as date
                FROM
                prd_article
                order by
                date"""
        _rdata = mysql.fetchall_db (sql)
        _logger.info (_rdata)
    except Exception as e:
        _logger.exception ("error: {}".format (e))
        return returnData ("404", "失败", None)
    # page = request.args.get (get_page_parameter (), type=int, default=1)
    # pagination = Pagination (page=page, total=len (_rdata))
    # _logger.info(pagination.info)
    return returnData ("0", "成功", _rdata)


## 技术文章来源分析
@app.route ("/article/source", methods=["POST"])
def articleSource():
    """

    :return:
    """
    try:
        sql = """SELECT
                article_source,count(id) as counts
                FROM
                prd_article
                GROUP BY
                article_source
                ORDER BY
                counts desc"""
        _rdata = mysql.fetchall_db (sql)
        _logger.info (_rdata)
    except Exception as e:
        _logger.exception ("error: {}".format (e))
        return returnData ("404", "失败", None)
    # page = request.args.get (get_page_parameter (), type=int, default=1)
    # pagination = Pagination (page=page, total=len (_rdata))
    # _logger.info(pagination.info)
    return returnData ("0", "成功", _rdata)

## 技术文章时间分析
@app.route ("/article/date", methods=["POST"])
def articleDate():
    """

    :return:
    """
    try:
        sql = """SELECT
                date_format(article_date,"%Y-%m") as date,count(id) as counts
                FROM
                prd_article
                GROUP BY
                date_format(article_date,"%Y-%m")
                ORDER BY
                counts desc"""
        _rdata = mysql.fetchall_db (sql)
        _logger.info (_rdata)
    except Exception as e:
        _logger.exception ("error: {}".format (e))
        return returnData ("404", "失败", None)
    # page = request.args.get (get_page_parameter (), type=int, default=1)
    # pagination = Pagination (page=page, total=len (_rdata))
    # _logger.info(pagination.info)
    return returnData ("0", "成功", _rdata)

## 技术文章时间分析
@app.route ("/article/date", methods=["POST"])
def articleDate():
    """

    :return:
    """
    try:
        sql = """SELECT
                date_format(article_date,"%Y-%m") as date,count(id) as counts
                FROM
                prd_article
                GROUP BY
                date_format(article_date,"%Y-%m")
                ORDER BY
                counts desc"""
        _rdata = mysql.fetchall_db (sql)
        _logger.info (_rdata)
    except Exception as e:
        _logger.exception ("error: {}".format (e))
        return returnData ("404", "失败", None)
    # page = request.args.get (get_page_parameter (), type=int, default=1)
    # pagination = Pagination (page=page, total=len (_rdata))
    # _logger.info(pagination.info)
    return returnData ("0", "成功", _rdata)


## 地区批发市场报价数量分析
@app.route ("/price/areaCounts", methods=["POST"])
def articleDate():
    """

    :return:
    """
    try:
        sql = """SELECT
                LEFT(bazaar,2) as bazaar,COUNT(id) as  counts
                FROM
                prd_price
                GROUP BY
                LEFT(bazaar,2)
                ORDER BY
                counts desc"""
        _rdata = mysql.fetchall_db (sql)
        _logger.info (_rdata)
    except Exception as e:
        _logger.exception ("error: {}".format (e))
        return returnData ("404", "失败", None)
    # page = request.args.get (get_page_parameter (), type=int, default=1)
    # pagination = Pagination (page=page, total=len (_rdata))
    # _logger.info(pagination.info)
    return returnData ("0", "成功", _rdata)










































if __name__ == '__main__':
    app.run(debug=False, port=8080)

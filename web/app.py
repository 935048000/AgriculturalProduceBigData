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
    # request.form.get ("key", type=str, default=None)
    return returnData("0","成功",str(request.form.to_dict()))


@app.route ("/prdInfo", methods=["POST"])
def prdInfo():
    """
    产品信息接口
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



@app.route ("/diseases/info", methods=["POST"])
def diseasesInfo():
    """
    虫害病信息接口
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


@app.route ("/article/info", methods=["POST"])
def articleInfo():
    """
    技术文章信息接口
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



@app.route ("/article/source", methods=["POST"])
def articleSource():
    """
    技术文章来源分析
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


@app.route ("/article/date", methods=["POST"])
def articleDate():
    """
    技术文章时间分析
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

@app.route ("/plantation/provincePlantationCounts", methods=["POST"])
def provincePlantationCounts():
    """
    省份种植基地数量
    :return:
    """
    try:
        sql = """SELECT
                pi.city,
                pi.counts
                FROM
                plantation_info pi
                LEFT JOIN city_info ci on pi.city=ci.city
                WHERE
                ci.begetter_code = '000000'
                AND pi.counts != -1
                ORDER BY
                pi.counts DESC"""
        _rdata = mysql.fetchall_db (sql)
        _logger.info (_rdata)
    except Exception as e:
        _logger.exception ("error: {}".format (e))
        return returnData ("404", "失败", None)
    # page = request.args.get (get_page_parameter (), type=int, default=1)
    # pagination = Pagination (page=page, total=len (_rdata))
    # _logger.info(pagination.info)
    return returnData ("0", "成功", _rdata)

@app.route ("/plantation/cityPlantationCounts", methods=["POST"])
def cityPlantationCounts():
    """
    城市种植数量
    :return:
    """
    try:
        sql = """SELECT
                pi.city,
                pi.counts
                FROM
                plantation_info pi
                LEFT JOIN city_info ci on pi.city=ci.city
                WHERE
                ci.begetter_code != '000000'
                AND pi.counts != -1
                ORDER BY
                pi.counts DESC"""
        _rdata = mysql.fetchall_db (sql)
        _logger.info (_rdata)
    except Exception as e:
        _logger.exception ("error: {}".format (e))
        return returnData ("404", "失败", None)
    # page = request.args.get (get_page_parameter (), type=int, default=1)
    # pagination = Pagination (page=page, total=len (_rdata))
    # _logger.info(pagination.info)
    return returnData ("0", "成功", _rdata)


@app.route ("/price/areaCounts", methods=["POST"])
def areaCounts():
    """
    地区批发市场报价数量分析
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


@app.route ("/price/dayAvgPrice", methods=["POST"])
def dayAvgPrice():
    """
    日均报价
    :return:
    """
    try:
        
        sql = """SELECT
                CAST(round( AVG(avg_price) , 2) AS CHAR) as avg_price,date_format(date,"%Y-%m-%d") as date
                FROM
                prd_price
                WHERE
                date >= '{0}'
                AND date <= '{1}'
                GROUP BY
                date_format(date,"%Y-%m-%d")
                ORDER BY
                date""".format(request.form['startDate'],request.form['stopDate'])
        # _logger.info ("sql="+sql)
        _rdata = mysql.fetchall_db (sql)
        _logger.info (_rdata)
    except Exception as e:
        _logger.error ("error: {}".format (e))
        return returnData ("404", "失败", None)
    # page = request.args.get (get_page_parameter (), type=int, default=1)
    # pagination = Pagination (page=page, total=len (_rdata))
    # _logger.info(pagination.info)
    return returnData ("0", "成功", _rdata)


@app.route ("/price/monAvgPrice", methods=["POST"])
def monAvgPrice():
    """
    月均报价
    :return:
    """
    try:
        
        sql = """SELECT
                CAST(round( AVG(`avg_price`) , 2) AS CHAR) as avg_price,
                date_format(`date`,"%Y-%m") as date
                FROM
                prd_price
                WHERE
                date_format(`date`,"%Y-%m") >= '{0}'
                AND date_format(`date`,"%Y-%m") <= '{1}'
                GROUP BY date_format(`date`,"%Y-%m")
                ORDER BY date""".format (request.form['startDate'], request.form['stopDate'])
        # _logger.info ("sql=" + sql)
        _rdata = mysql.fetchall_db (sql)
        _logger.info (_rdata)
    except Exception as e:
        _logger.error ("error: {}".format (e))
        return returnData ("404", "失败", None)
    return returnData ("0", "成功", _rdata)


@app.route ("/price/monLinkRelative", methods=["POST"])
def monLinkRelative():
    """
    年份 月环比 查当前年内的月份环比
    :param year:YYYY
    :return:
    """
    try:
        
        sql = """SELECT
                SUM(case when RIGHT(t1.date1,2)=1 then  CAST(ROUND(((t1.total_pay-t2.total_pay)/t2.total_pay)*100,2) AS CHAR) ELSE 0 end) as m01,
                SUM(case when RIGHT(t1.date1,2)=2 then  CAST(ROUND(((t1.total_pay-t2.total_pay)/t2.total_pay)*100,2) AS CHAR) ELSE 0 end) as m02,
                SUM(case when RIGHT(t1.date1,2)=3 then  CAST(ROUND(((t1.total_pay-t2.total_pay)/t2.total_pay)*100,2) AS CHAR) ELSE 0 end) as m03,
                SUM(case when RIGHT(t1.date1,2)=4 then  CAST(ROUND(((t1.total_pay-t2.total_pay)/t2.total_pay)*100,2) AS CHAR) ELSE 0 end) as m04,
                SUM(case when RIGHT(t1.date1,2)=5 then  CAST(ROUND(((t1.total_pay-t2.total_pay)/t2.total_pay)*100,2) AS CHAR) ELSE 0 end) as m05,
                SUM(case when RIGHT(t1.date1,2)=6 then  CAST(ROUND(((t1.total_pay-t2.total_pay)/t2.total_pay)*100,2) AS CHAR) ELSE 0 end) as m06,
                SUM(case when RIGHT(t1.date1,2)=7 then  CAST(ROUND(((t1.total_pay-t2.total_pay)/t2.total_pay)*100,2) AS CHAR) ELSE 0 end) as m07,
                SUM(case when RIGHT(t1.date1,2)=8 then  CAST(ROUND(((t1.total_pay-t2.total_pay)/t2.total_pay)*100,2) AS CHAR) ELSE 0 end) as m08,
                SUM(case when RIGHT(t1.date1,2)=9 then  CAST(ROUND(((t1.total_pay-t2.total_pay)/t2.total_pay)*100,2) AS CHAR) ELSE 0 end) as m09,
                SUM(case when RIGHT(t1.date1,2)=10 then CAST(ROUND(((t1.total_pay-t2.total_pay)/t2.total_pay)*100,2) AS CHAR) ELSE 0 end) as m10,
                SUM(case when RIGHT(t1.date1,2)=11 then CAST(ROUND(((t1.total_pay-t2.total_pay)/t2.total_pay)*100,2) AS CHAR) ELSE 0 end) as m11,
                SUM(case when RIGHT(t1.date1,2)=12 then CAST(ROUND(((t1.total_pay-t2.total_pay)/t2.total_pay)*100,2) AS CHAR) ELSE 0 end) as m12
                -- *
                FROM
                (
                SELECT
                round( AVG(avg_price) , 2) as total_pay,
                date_format(date,"%Y-%m") as date1
                FROM
                prd_price
                
                WHERE
                date_format(date,"%Y-%m") >= '{0}-01'
                AND date_format(date,"%Y-%m") <= '{1}-12'
                GROUP BY
                date_format(date,"%Y-%m")
                ) t1
                INNER JOIN
                (
                SELECT
                round( AVG(avg_price) , 2) as total_pay,
                date_format(date_add(date, interval 1 month),"%Y-%m") as date1
                -- date_format(date,"%Y-%m") as date1
                FROM
                prd_price
                
                WHERE
                date_format(date,"%Y-%m") >= '{2}-12'
                AND date_format(date,"%Y-%m") <= '{1}-12'
                GROUP BY
                date1
                ) t2 ON t2.date1=t1.date1""".format (request.form['year'], request.form['year'],int(request.form['year'])-1)
        _logger.info ("sql=" + sql)
        _rdata = mysql.fetchall_db (sql)
        _logger.info (_rdata)
    except Exception as e:
        _logger.error ("error: {}".format (e))
        return returnData ("404", "失败", None)
    return returnData ("0", "成功", _rdata)


@app.route ("/price/monCorrespondingPeriod", methods=["POST"])
def monCorrespondingPeriod():
    """
    年份 月同期
    :param year:YYYY需查年份
    :return:
    """
    try:
        
        sql = """SELECT
                SUM(case when RIGHT(t1.date1,2)=1 then  CAST(ROUND(((t1.total_pay-t2.total_pay)/t2.total_pay)*100,2) AS CHAR) ELSE 0 end) as m01,
                SUM(case when RIGHT(t1.date1,2)=2 then  CAST(ROUND(((t1.total_pay-t2.total_pay)/t2.total_pay)*100,2) AS CHAR) ELSE 0 end) as m02,
                SUM(case when RIGHT(t1.date1,2)=3 then  CAST(ROUND(((t1.total_pay-t2.total_pay)/t2.total_pay)*100,2) AS CHAR) ELSE 0 end) as m03,
                SUM(case when RIGHT(t1.date1,2)=4 then  CAST(ROUND(((t1.total_pay-t2.total_pay)/t2.total_pay)*100,2) AS CHAR) ELSE 0 end) as m04,
                SUM(case when RIGHT(t1.date1,2)=5 then  CAST(ROUND(((t1.total_pay-t2.total_pay)/t2.total_pay)*100,2) AS CHAR) ELSE 0 end) as m05,
                SUM(case when RIGHT(t1.date1,2)=6 then  CAST(ROUND(((t1.total_pay-t2.total_pay)/t2.total_pay)*100,2) AS CHAR) ELSE 0 end) as m06,
                SUM(case when RIGHT(t1.date1,2)=7 then  CAST(ROUND(((t1.total_pay-t2.total_pay)/t2.total_pay)*100,2) AS CHAR) ELSE 0 end) as m07,
                SUM(case when RIGHT(t1.date1,2)=8 then  CAST(ROUND(((t1.total_pay-t2.total_pay)/t2.total_pay)*100,2) AS CHAR) ELSE 0 end) as m08,
                SUM(case when RIGHT(t1.date1,2)=9 then  CAST(ROUND(((t1.total_pay-t2.total_pay)/t2.total_pay)*100,2) AS CHAR) ELSE 0 end) as m09,
                SUM(case when RIGHT(t1.date1,2)=10 then CAST(ROUND(((t1.total_pay-t2.total_pay)/t2.total_pay)*100,2) AS CHAR) ELSE 0 end) as m10,
                SUM(case when RIGHT(t1.date1,2)=11 then CAST(ROUND(((t1.total_pay-t2.total_pay)/t2.total_pay)*100,2) AS CHAR) ELSE 0 end) as m11,
                SUM(case when RIGHT(t1.date1,2)=12 then CAST(ROUND(((t1.total_pay-t2.total_pay)/t2.total_pay)*100,2) AS CHAR) ELSE 0 end) as m12
                -- *
                FROM
                (
                SELECT
                round( AVG(avg_price) , 2) as total_pay,
                date_format(date,"%Y-%m") as date1
                FROM
                prd_price
                WHERE
                date_format(date,"%Y") = '{0}'
                GROUP BY
                date_format(date,"%Y-%m")
                ) t1
                INNER JOIN
                (
                SELECT
                round( AVG(avg_price) , 2) as total_pay,
                date_format(date_add(date, interval 12 month),"%Y-%m") as date1
                FROM
                prd_price
                WHERE
                date_format(date,"%Y") = '{1}'
                GROUP BY
                date1
                ) t2 ON t2.date1=t1.date1""".format (request.form['year'],int(request.form['year'])-1)
        _logger.info ("sql=" + sql)
        _rdata = mysql.fetchall_db (sql)
        _logger.info (_rdata)
    except Exception as e:
        _logger.error ("error: {}".format (e))
        return returnData ("404", "失败", None)
    return returnData ("0", "成功", _rdata)





@app.route ("/price/yearAvgPrice", methods=["POST"])
def yearAvgPrice():
    """
    年均报价
    :param startDate :YYYY 开始年
    :param startDate :YYYY 结束年
    :return:
    """
    try:
        
        sql = """SELECT
                CAST(round( AVG(`avg_price`) , 2) AS CHAR) as avg_price,
                date_format(`date`,"%Y") as date
                FROM
                prd_price
                WHERE
                date_format(`date`,"%Y") >= '{0}'
                AND date_format(`date`,"%Y") <= '{1}'
                GROUP BY date_format(`date`,"%Y")
                ORDER BY date""".format (request.form['startDate'], request.form['stopDate'])
        # _logger.info ("sql=" + sql)
        _rdata = mysql.fetchall_db (sql)
        _logger.info (_rdata)
    except Exception as e:
        _logger.error ("error: {}".format (e))
        return returnData ("404", "失败", None)
    return returnData ("0", "成功", _rdata)


@app.route ("/price/yearLinkRelative", methods=["POST"])
def yearLinkRelative():
    """
    年均报价
    :return:
    """
    try:
        
        sql = """SELECT
                SUM(case when t1.date1=2020 then CAST(ROUND(((t1.total_pay-t2.total_pay)/t2.total_pay)*100,2) AS CHAR) ELSE 0 end) as '2020',
                SUM(case when t1.date1=2019 then CAST(ROUND(((t1.total_pay-t2.total_pay)/t2.total_pay)*100,2) AS CHAR) ELSE 0 end) as '2019',
                SUM(case when t1.date1=2018 then CAST(ROUND(((t1.total_pay-t2.total_pay)/t2.total_pay)*100,2) AS CHAR) ELSE 0 end) as '2018'
                FROM
                (
                SELECT
                round( AVG(avg_price) , 2) as total_pay,
                date_format(date,"%Y") as date1
                FROM
                prd_price
                GROUP BY
                date1
                ) t1
                INNER JOIN
                (
                SELECT
                round( AVG(avg_price) , 2) as total_pay,
                date_format(date_add(date, interval 12 month),"%Y") as date1
                FROM
                prd_price pp
                GROUP BY
                date1
                ) t2 on t1.date1 = t2.date1"""
        # _logger.info ("sql=" + sql)
        _rdata = mysql.fetchall_db (sql)
        _logger.info (_rdata)
    except Exception as e:
        _logger.error ("error: {}".format (e))
        return returnData ("404", "失败", None)
    return returnData ("0", "成功", _rdata)









































if __name__ == '__main__':
    app.run(debug=False, port=8080)

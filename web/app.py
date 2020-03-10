from web.utils import load_config
from web.logger  import setup_log
from flask import Flask, request, render_template, session, redirect, url_for
from web.utils import mysql
import math

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
    return str(request.form.to_dict())

















if __name__ == '__main__':
    app.run(debug=True, port=8080)

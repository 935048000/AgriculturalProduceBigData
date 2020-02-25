from .utils import load_config
from .logger  import setup_log
from flask import Flask, request, render_template, session, redirect, url_for
from .utils import mysql
import math

config = load_config()
_logger = setup_log(__name__)
app = Flask(__name__)
mysql = mysql(config['mysql'])

# 模板
# @app.route("/user", methods=['POST', 'GET'])
# def user():
#     """
#     个人信息
#     :return: UserInfo.html
#     """
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





















if __name__ == '__main__':
    app.run(debug=True, port=8080)

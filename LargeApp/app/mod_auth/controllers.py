import urllib.request
import base64
import cv2
import flask
import numpy as np
import requests
from matplotlib import pyplot as plt
from pymysql import connect
# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

from pymysql import Connection
def mysql_conn():
    #连接数据库
    conn=Connection(host='localhost',user='root',password='lw2019',port=3306,database='ly')
    cursor=conn.cursor()
    sql='insert into ly.talk(username, PHONE, EMAIL, MESS) values ("小红","123456","123456@qq.com","不错")'
    # 执行提交
    cursor.execute(sql)
    conn.commit()
    print("成功")
    cursor.close()
    conn.close()
mysql_conn()
# Import password / encryption helper tools
# from werkzeug import check_password_hash, generate_password_hash

# Import the database object from the main app module
# from app import db

# Import module forms
# from app.mod_auth.forms import LoginForm

# Import module models (i.e. User)
# from app.mod_auth.models import User


# Define the blueprint: 'auth', set its url prefix: app.url/auth

mod_auth = Blueprint('auth', __name__, url_prefix='/auth')

# Set the route and accepted methods


@mod_auth.route('/comment/', methods=['GET', 'POST'])




def comment():
    return render_template('auth/index.html')

#     # If sign in form is submitted
#     form = LoginForm(request.form)

#     # Verify the sign in form
#     if form.validate_on_submit():
#
#         user = User.query.filter_by(email=form.email.data).first()
#
#         if user and check_password_hash(user.password, form.password.data):
#
#             session['user_id'] = user.id
#
#             flash('Welcome %s' % user.name)
#
#             return redirect(url_for('auth.home'))
#
#         flash('Wrong email or password', 'error-message')
#
#     return render_template("auth/signin.html", form=form)
#
# # # elevateChina



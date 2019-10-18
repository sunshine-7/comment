import datetime
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
#
from pymysql import Connection
def mysql_conn(username,phone,email,mess):
    # print(username, "\n", phone, "\n", email, "\n", mess, "\n")
    #连接数据库
    conn=Connection(host='localhost',user='root',password='lw2019',port=3306,database='ly')
    cursor=conn.cursor()

    sql='insert into ly.talk(USERNAME) values (%s)'

    # --------------
    data = {
        'username': username,
        'phone': phone,
        'email': email,
        'mess':mess
    }
    table = 'ly.talk'
    # 获取到一个以键且为逗号分隔的字符串，返回一个字符串
    keys = ', '.join(data.keys())
    values = ', '.join(['%s'] * len(data))
    sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
    try:
        # 这里的第二个参数传入的要是一个元组
        # 执行
        if cursor.execute(sql, tuple(data.values())):
            print('Successful')
            # 提交
            conn.commit()
    except:
        print('Failed')
        conn.rollback()
    # ------------
    cursor.execute('select * from ly.talk')

    # conn.commit()
    # print("成功")
    cursor.close()
    conn.close()
# mysql_conn()
# Import password / encryption helper tools
# from werkzeug import check_password_hash, generate_password_hash

# Import the database object from the main app module
# from app import db

# Import module forms
from app.mod_auth.forms import LoginForm

# Import module models (i.e. User)
from app.mod_auth.models import User


# Define the blueprint: 'auth', set its url prefix: app.url/auth

mod_auth = Blueprint('auth', __name__, url_prefix='/auth')
@mod_auth.route('/mess/', methods=['GET', 'POST'])
def mess():
    if request.method=="POST":
        username=request.form.get('username')
        phone = request.form.get('phone')
        email = request.form.get('email')
        mess = request.form.get('mess')
        # print(username,"\n",phone,"\n",email,"\n",mess,"\n")
        # create_at = datetime.now()
        # mysql_conn(username, phone,email,mess,create_at)
        mysql_conn(username, phone, email, mess)
    return render_template('auth/index.html')



# Set the route and accepted methods
# @mod_auth.route('/signin/', methods=['GET', 'POST'])
# def signin():
#     # If sign in form is submitted
#     form = LoginForm(request.form)
#
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
#
#

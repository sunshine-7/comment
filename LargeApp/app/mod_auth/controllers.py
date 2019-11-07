import datetime
import urllib.request
import base64
import cv2
import flask
import numpy as np
import requests
from matplotlib import pyplot as plt
from pymysql import connect
from pymysql import Connection

# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

def mysql_conn(username,phone,email,mess):
    # print(username, "\n", phone, "\n", email, "\n", mess, "\n")
    #连接数据库
    conn=Connection(host='localhost',user='root',password='lw2019',port=3306,database='ly')
    cursor=conn.cursor()
    # ------------
    data = {
        'username': username,
        'phone': phone,
        'email': email,
        'mess':mess
    }
    table = 'ly.talk'
    # 获取到一个以键且为逗号分隔的字符串，返回一个字符串
    keys = ', '.join(data.keys())
    print("keys\n")
    print(keys)
    values = ', '.join(['%s'] * len(data))
    print("values\n ")
    print(values)
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
    cursor.close()
    conn.close()
    return render_template("auth/index.html")

# Import password / encryption helper tools
# from werkzeug import check_password_hash, generate_password_hash

# Import the database object from the main app module
# from app import db

# Import module forms
from app.mod_auth.forms import LoginForm

# Import module models (i.e. User)
from app.mod_auth.models import User


# sql="update table set column="" where column="" "
# sql="delete from table where column="" "
# sql="select * from table where column="" "
# sql = "insert into table (column) value ("")"

def pic():
    # conn = Connection(host='localhost', user='root', password='lw2019', port=3306, database='ly')
    # cursor = conn.cursor()
    img = cv2.imread("LargeApp/app/mod_auth/1.jpg")
    print(type(img))
    print(img)
    # imgEncode = cv2.imencode(".jpg",img)[1]
    # imgstr = np.array(imgEncode).tostring()
    # imgbase64str = base64.b64encode(imgstr)
    # sql="insert into ly.company (pic_str) value (%s)" %imgbase64str
    # cursor.execute(sql)
    # conn.commit()
    # cursor.close()
    # conn.close()

def stc():
    conn = Connection(host='localhost', user='root', password='lw2019', port=3306, database='ly')
    cursor = conn.cursor()
    sql = "SELECT * FROM ly.company"
    cursor.execute(sql)
    u = cursor.fetchall()
    cursor.close()
    conn.close()
    return u

mod_auth = Blueprint('auth', __name__, url_prefix='/auth')
@mod_auth.route('/mess/', methods=['GET', 'POST'])
def mess():
    pic()
    if request.method=="POST":
        username=request.form.get('username')
        phone = request.form.get('phone')
        email = request.form.get('email')
        mess = request.form.get('mess')
        mysql_conn(username, phone, email, mess)
    # aa=stc()
    # dimg=base64.b64decode(aa[0][5])
    # dimg=cv2.imdecode(np.fromstring(dimg,dtype='uint8'),1)
    # return render_template('auth/index.html',aa,dimg)
    return render_template('auth/index.html',aa=stc())



# -*- coding: UTF-8 -*-
'''
@author: xuqiang
'''
from sqlalchemy import create_engine
import pandas as pd
class mysql_engine():
    user='root'
    passwd='root'
    host='localhost'
    port = '3306'
    db_name='test'
    engine = create_engine('mysql://{0}:{1}@{2}:{3}/{4}?charset=utf8'.format(user,passwd,host,port,db_name))

def get_data(sql):
    pg_enine = mysql_engine()
    try:
        with pg_enine.engine.connect() as con,con.begin():
            df = pd.read_sql(sql,con) #获取数
        con.close()
    except:
        df = None
    return df
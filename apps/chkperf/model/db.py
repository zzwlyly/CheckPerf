# -*- coding:utf-8 -*-
import os
import sqlite3

DIR_PATH = os.path.abspath(os.path.dirname(__file__))
db_name = os.path.join(DIR_PATH, 'mydb.db')


def create_db():
    # 连接
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    # 创建表

    c.execute(
        '''CREATE TABLE IF NOT EXISTS disk (id INTEGER PRIMARY KEY, insert_time datetime,dev_name text, r_s float, w_s float, rMB_s float,wMB_s float, avgrq_sz float, avgqu_sz float, await float, util float)''')

    c.execute(
        '''CREATE TABLE IF NOT EXISTS network (id INTEGER PRIMARY KEY, insert_time datetime,eth_name text, r_traffic float, w_traffic float)''')

    c.execute(
        '''CREATE TABLE IF NOT EXISTS cpu (id INTEGER PRIMARY KEY, insert_time datetime, cpu_use float, cpu_sy float, cpu_id float, cpu_wa float, m1 float, m5 float, m15 float)''')

    c.execute(
        '''CREATE TABLE IF NOT EXISTS mem (id INTEGER PRIMARY KEY, insert_time datetime,mem_use float, buff_cache float, available float)''')
    # 关闭
    conn.close()


def insert_to_disk(*args):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    c.execute(
        """INSERT INTO disk(insert_time,dev_name,r_s,w_s,rMB_s,wMB_s,avgrq_sz,avgqu_sz,await,util) VALUES (?,?,?,?,?,?,?,?,?,?)""",
        args)

    conn.commit()

    conn.close()


def insert_to_network(*args):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    c.execute('INSERT INTO network(insert_time,eth_name,r_traffic,w_traffic) VALUES (?,?,?,?)', args)

    conn.commit()

    conn.close()


def insert_to_cpu(*args):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    c.execute('INSERT INTO cpu(insert_time,cpu_use,cpu_sy,cpu_id,cpu_wa,m1,m5,m15) VALUES (?,?,?,?,?,?,?,?)', args)

    conn.commit()

    conn.close()


def insert_to_mem(*args):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    c.execute('INSERT INTO mem(insert_time,mem_use,buff_cache,available) VALUES (?,?,?,?)', args)

    conn.commit()

    conn.close()


def query_db(query, args=()):
    db = sqlite3.connect(db_name)
    c = db.cursor()
    cur = c.execute(query, args)
    db.commit()
    res = cur.fetchall()
    db.close()
    return res


def delete_db(sql, args=()):
    db = sqlite3.connect(db_name)
    c = db.cursor()
    c.execute(sql, args)
    db.commit()
    db.close()


if __name__ == '__main__':
    create_db()

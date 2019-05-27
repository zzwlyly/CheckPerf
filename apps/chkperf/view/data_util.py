# -*- coding:utf-8 -*-
'''
数据读写
'''
import datetime

from apps.chkperf.model.db import query_db


def get_disk_json(flag):
    """
    读取硬盘信息
    :param flag:
    :return:
    """
    try:
        now_time = datetime.datetime.strptime(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                              "%Y-%m-%d %H:%M:%S")
        interval = (now_time - datetime.timedelta(minutes=10)).strftime("%Y-%m-%d %H:%M:%S")
        interval = "2019-05-26 22:08:30"
        lines = []
        names = query_db("select distinct dev_name from disk order by dev_name")
        for name in names:
            infos = []
            if flag == "1":
                infos = query_db("select * from disk where dev_name=(?) and insert_time>(?)", (name[0], interval))
            elif flag == "0":
                infos = query_db("select * from disk where dev_name=(?)", name)
            data_list = []
            for info in infos:
                tmp = {"time": info[1][11:], 'name': info[2], 'r_s': info[3], 'w_s': info[4], 'rMB_s': info[5],
                       'wMB_s': info[6],
                       'avgrq_sz': info[7], 'avgqu_sz': info[8],
                       'await': info[9], 'util': info[10]}
                data_list.append(tmp)
            disk_data = {'name': name[0], 'data': data_list}
            lines.append(disk_data)
        return lines
    except Exception as msg:
        pass


def get_network_json(flag):
    """
    读取网卡信息
    :param flag:
    :return:
    """
    try:
        now_time = datetime.datetime.strptime(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                              "%Y-%m-%d %H:%M:%S")
        interval = (now_time - datetime.timedelta(minutes=10)).strftime("%Y-%m-%d %H:%M:%S")
        lines = []
        names = query_db("select distinct eth_name from network order by eth_name")
        for name in names:
            infos = []
            if flag == "1":
                infos = query_db("select * from network where eth_name=(?) and insert_time>(?)", (name[0], interval))
            elif flag == "0":
                infos = query_db("select * from network where eth_name=(?)", name)
            data_list = []
            for info in infos:
                tmp = {"time": info[1][11:], "read ": info[3], "write": info[4]}
                data_list.append(tmp)
            network_data = {'name': name[0], 'data': data_list}
            lines.append(network_data)
        return lines
    except Exception as msg:
        pass


def get_cpu_json(flag):
    """
    读取CPU信息
    :param flag:
    :return:
    """
    try:
        now_time = datetime.datetime.strptime(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                              "%Y-%m-%d %H:%M:%S")
        interval = (now_time - datetime.timedelta(minutes=10)).strftime("%Y-%m-%d %H:%M:%S")
        lines = []
        infos = []
        if flag == "1":
            infos = query_db("select * from cpu where insert_time>(?)", (interval,))
        elif flag == "0":
            infos = query_db("select * from cpu")
        data_list = []
        for info in infos:
            tmp = {"time": info[1][11:], "cpu_use": info[2],
                   "cpu_sy": info[3], "cpu_id": info[4], "cpu_wa": info[5],
                   "m1": info[6], "m5": info[7], "m15": info[8], }
            data_list.append(tmp)
        network_data = {'name': "CPU", 'data': data_list}
        lines.append(network_data)
        return lines
    except Exception as msg:
        pass


def get_mem_json(flag):
    """
    读取内存信息
    :param flag:
    :return:
    """
    try:
        now_time = datetime.datetime.strptime(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                              "%Y-%m-%d %H:%M:%S")
        interval = (now_time - datetime.timedelta(minutes=10)).strftime("%Y-%m-%d %H:%M:%S")
        lines = []
        infos = []
        if flag == "1":
            infos = query_db("select * from mem where insert_time>(?)", (interval,))
        elif flag == "0":
            infos = query_db("select * from mem")
        data_list = []
        for info in infos:
            tmp = {"time": info[1][11:], "mem_use（%）": info[2],
                   "buff_cache（MB/s）": info[3], "available（MB/s）": info[4]}
            data_list.append(tmp)
        network_data = {'name': "Memory", 'data': data_list}
        lines.append(network_data)
        return lines
    except Exception as msg:
        pass


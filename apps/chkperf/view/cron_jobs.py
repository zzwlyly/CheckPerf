# -*- coding:utf-8 -*-
import datetime
import os
import re

from apps.chkperf.model import db


def exec_get_disk():
    '''
    采集硬盘信息
    :return:
    '''

    cmd = "iostat -d -m -x 1 2"
    try:
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        infos = os.popen(cmd).readlines()
        tmp = [i.strip() for i in infos[len(infos) / 2:] if
               len(i.strip()) > 0 and not i.startswith("Device") and not i.startswith("Linux")]
        for i in tmp:
            info_tmp = i.split()
            db.insert_to_disk(now_time, info_tmp[0], info_tmp[3], info_tmp[4], info_tmp[5], info_tmp[6], info_tmp[7],
                              info_tmp[8], info_tmp[9], info_tmp[-1])
    except Exception as msg:
        pass


def exec_get_network():
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        # 查找可以使用的网口
        network_info = os.popen("""ip add | grep 'state UP'""").readlines()
        networks = [i.split(':')[1].strip() for i in network_info]  # 可用网口的名称
        for network in networks:
            line = os.popen("sar -n DEV 1 10 | grep '%s'" % network).readlines()[-1].split()
            lines = [i.strip() for i in line if i.strip() not in ' ']
            r_traffic = round(float(lines[4].strip()) / 1024, 2)
            w_traffic = round(float(lines[5].strip()) / 1024, 2)
            db.insert_to_network(now_time, lines[1].strip(), r_traffic, w_traffic)

    except Exception as msg:
        pass


def exec_get_cpu():
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cmd1 = "top -b -d 1 -n 2 | grep Cpu"
    cmd2 = "top -b -d 1 -n 2 | grep 'load'"
    try:
        cpu_infos = os.popen(cmd1).readlines()
        cpu = cpu_infos[len(cpu_infos) - 1].split()
        load_average = os.popen(cmd2).readlines()
        la = load_average[-1].split("load average:")[-1].split(',')
        la = [i.strip() for i in la]
        db.insert_to_cpu(now_time, cpu[1], cpu[3], cpu[7], cpu[9], la[0], la[1], la[2])
    except Exception as msg:
        pass


def exec_get_mem():
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    """
    获取节点内存使用率信息
    @return:
    """
    try:
        cmd = "free"
        lines = os.popen(cmd).readlines()
        for line in lines:
            if re.search('Mem', line):
                total = int(line.split()[1])
                used = int(line.split()[2])
                # 磁盘缓存的大小
                buff_cache = round(float(int(line.split()[5]) / 1024), 2)
                available = round(float(int(line.split()[6]) / 1024), 2)
                percent = round(100 * used / total, 2)
                db.insert_to_mem(now_time, percent, buff_cache, available)
    except Exception as msg:
        pass


def exec_clear_disk_info():
    try:
        time = db.query_db("select insert_time from disk order by id DESC limit 1")
        time = datetime.datetime.strptime(time[0][0], "%Y-%m-%d %H:%M:%S")
        interval = (time - datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S")
        db.delete_db("delete from disk where insert_time<(?)", args=(interval,))
    except Exception as msg:
        pass


def exec_clear_network_info():
    try:
        time = db.query_db("select insert_time from network order by id DESC limit 1")
        time = datetime.datetime.strptime(time[0][0], "%Y-%m-%d %H:%M:%S")
        interval = (time - datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S")
        db.delete_db("delete from network where insert_time<(?)", args=(interval,))
    except Exception as msg:
        pass


def exec_clear_cpu_info():
    try:
        time = db.query_db("select insert_time from cpu order by id DESC limit 1")
        time = datetime.datetime.strptime(time[0][0], "%Y-%m-%d %H:%M:%S")
        interval = (time - datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S")
        db.delete_db("delete from cpu where insert_time<(?)", args=(interval,))
    except Exception as msg:
        pass


def exec_clear_mem_info():
    try:
        time = db.query_db("select insert_time from mem order by id DESC limit 1")
        time = datetime.datetime.strptime(time[0][0], "%Y-%m-%d %H:%M:%S")
        interval = (time - datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S")
        db.delete_db("delete from mem where insert_time<(?)", args=(interval,))
    except Exception as msg:
        pass

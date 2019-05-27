# -*- coding:utf-8 -*-


from flask import Blueprint, request, render_template, make_response, jsonify

from apps.chkperf.view import data_util

BLUEPRINT_PERF_KEY = 'perf'
perf = Blueprint(BLUEPRINT_PERF_KEY, __name__, template_folder='templates')


@perf.route('/')
def index():
    return render_template('index.html')


@perf.route('/disk/', methods=['get'])
def get_disk_info():
    '''
    检测硬盘信息
    :return:
    '''
    if request.method == 'GET':
        flag = request.args.get("flag")
        data = data_util.get_disk_json(flag)
        return make_response(jsonify({'data': data}))


@perf.route('/network/', methods=['get'])
def get_network_info():
    '''
    检测网卡信息
    :return:
    '''
    if request.method == 'GET':
        flag = request.args.get("flag")
        data = data_util.get_network_json(flag)
        return make_response(jsonify({'data': data}))


@perf.route('/cpu/', methods=['get'])
def get_cpu_info():
    '''
    检测CPU信息
    :return:
    '''
    if request.method == 'GET':
        flag = request.args.get("flag")
        data = data_util.get_cpu_json(flag)
        return make_response(jsonify({'data': data}))


@perf.route('/mem/', methods=['get'])
def get_mem_info():
    '''
    检测内存信息
    :return:
    '''
    if request.method == 'GET':
        flag = request.args.get("flag")
        data = data_util.get_mem_json(flag)
        return make_response(jsonify({'data': data}))



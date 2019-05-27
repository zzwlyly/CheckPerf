# -*- coding:utf-8 -*-

from apps.chkperf.view import cron_jobs


class Config(object):
    DEBUG = False
    SCHEDULER_API_ENABLED = True
    JOBS = [
        {
            'id': 'job_exec_get_disk',
            'func': cron_jobs.exec_get_disk,
            'args': '',
            'trigger': 'interval',
            'seconds': 2
        },
        {
            'id': 'job_exec_get_network',
            'func': cron_jobs.exec_get_network,
            'args': '',
            'trigger': 'interval',
            'seconds': 2
        },
        {
            'id': 'job_exec_get_cpu',
            'func': cron_jobs.exec_get_cpu,
            'args': '',
            'trigger': 'interval',
            'seconds': 2
        },
        {
            'id': 'job_exec_get_mem',
            'func': cron_jobs.exec_get_mem,
            'args': '',
            'trigger': 'interval',
            'seconds': 30
        },
        {
            'id': 'job_exec_clear_disk_info',
            'func': cron_jobs.exec_clear_disk_info,
            'args': '',
            'trigger': 'interval',
            'seconds': 600
        },
        {
            'id': 'job_exec_clear_network_info',
            'func': cron_jobs.exec_clear_network_info,
            'args': '',
            'trigger': 'interval',
            'seconds': 600
        },
        {
            'id': 'job_exec_clear_cpu_info',
            'func': cron_jobs.exec_clear_cpu_info,
            'args': '',
            'trigger': 'interval',
            'seconds': 600
        },
        {
            'id': 'job_exec_clear_mem_info',
            'func': cron_jobs.exec_clear_mem_info,
            'args': '',
            'trigger': 'interval',
            'seconds': 600
        }
    ]

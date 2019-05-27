# -*- coding:utf-8 -*-


from flask_apscheduler import APScheduler


# 初始化第三方插件
def init_ext(app):
    init_scheduler(app)


# 初始化定时任务
def init_scheduler(app):
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()

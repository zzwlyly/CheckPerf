#### 安装步骤

```
tar -zxvf checkperf-build.tgz
```

```
cd checkperf-build
```

```
sh install.sh
出现 "python libs install success!" 则安装成功
```

#### 启动

```
cd checkperf-build
sh start.sh
```

#### 停止

```
cd checkperf-build
sh stop.sh
```

#### 访问

```
当前主机IP:8080
例：172.16.18.182:8080
```

#### 注意事项

```
页面10s刷新一次
数据默认显示为10分钟数据，
可选，需先点击 时间 「10min | 60min」，再选择需查看的性能数据

由于数据采集和当前机器有关
磁盘数据间隔2-6s
网卡数据间隔15s
CPU数据间隔2-5s
内存数据间隔30s
```


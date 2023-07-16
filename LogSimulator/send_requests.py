import re
import requests
from datetime import datetime

# 读取日志文件
log_file = 'log.txt'  # 日志文件路径
with open(log_file, 'r') as file:
    logs = file.readlines()

# 解析日志，提取时间和请求参数
for log in logs:
    # 使用正则表达式提取时间和请求参数
    match = re.search(r'\[(.*?)\].*request=(.*)', log)
    if match:
        timestamp = match.group(1)
        params = match.group(2)

        # 解析时间戳
        log_time = datetime.strptime(timestamp, '%Y-%m-%d %H:%M')

        # 获取当前时间
        current_time = datetime.now()

        # 检查是否到达请求时间
        if current_time.hour == log_time.hour and current_time.minute == log_time.minute:
            # 发送HTTP请求到服务端
            url = 'http://example.com'  # 替换为实际的服务端URL
            headers = {'Content-Type': 'application/json'}  # 请求头，根据实际情况进行修改
            data = {'timestamp': timestamp, 'params': params}  # 请求数据，根据实际情况进行修改

            response = requests.post(url, headers=headers, json=data)

            # 处理响应
            if response.status_code == 200:
                print('请求成功！')
            else:
                print('请求失败！')

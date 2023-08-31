import pandas as pd
import os
import requests
import datetime

def is_workday(date):
    # 读取Excel文件
    df = pd.read_excel(r'E:\20230810-wechat-bot\project\workdays_2023.xlsx')
    
    # 将日期转换为字符串格式
    date_str = date.strftime('%Y-%m-%d')
    
    # 查找日期是否在Excel文件中，并返回是否为工作日
    if date_str in df['Date'].astype(str).values:
        return df.loc[df['Date'].astype(str) == date_str, 'Is_Workday'].values[0]
    else:
        return None

def call_api():
    # 从环境变量中获取key
    key = os.environ.get('WECHAT_KEY')
    print(key)

    # 设置要发送的消息内容
    message = {
        "msgtype": "text",
        "text": {
            "content": "hello world"
        }
    }

    # 调用接口发送消息
    response = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={key}', json=message)

    # 打印响应结果
    print(response.json())

current_time = datetime.datetime.now()
r = is_workday(current_time)
if(r == 1):
    call_api()


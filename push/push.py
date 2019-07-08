'''
time:验证的时间戳,
verify:验证字符串
Type:发送消息类型， 1 好友信息 2,群信息 3,讨论组信息 4,群临时会话 5,讨论组临时会话 ...,20001 点赞,20002 窗口抖动,20011 群禁言（管理）,20012 退群,20013 踢群成员（管理）,20021 设置群名片（管理）,20022 设置群管理（群主）,20023 入群处理（某人请求入群、我被邀请入群、某人被邀请入群）,20024 加好友处理（是否同意被加好友）,20031 发公告,20032 发作业
SubType:子类型，0普通，1匿名（需要群开启，默认0）,
StructureType:消息结构类型，0为普通文本消息（默认）、1为XML消息、2为JSON消息,
Group:操作或发送的群号或者讨论组号,
QQ:操作或者发送的QQ,
Msg:文本消息【标签等】，当发送类型为JSON、XML时为相应文本，禁言时为分钟数【分钟】,
Send:是否开启同步发送（1为开启同步发送【测试】，0为不开启【默认】）,
Data:附加数据，用于特定操作等（文本型）

'''
import copy
import json

import requests
from flask import current_app as app

from log import botLog

push_data = {
    # "time": '',
    # "verify": "",
    "data": [
        {
            "Type": -1,
            "SubType": 0,
            "StructureType": 0,
            "Group": "",
            "QQ": "",
            "Msg": "",
            "Send": 0,
            "Data": ''
        }
    ]

}
headers = {
    'Content-Type': 'application/json',
    'Connection': 'close',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Mobile Safari/537.36',

}


def push_msg_private(msg: str, private: str):
    data = copy.deepcopy(push_data)
    data["data"][0]["Type"] = 1
    data["data"][0]["QQ"] = private
    data["data"][0]["Msg"] = msg
    data = json.dumps(data)
    try:
        requests.post(app.config["PUSH_URL"], headers=headers, data=data)
    except Exception as e:
        botLog.error("插件问题再现!")


def push_msg_group(msg: str, group: str):
    data = copy.deepcopy(push_data)
    data["data"][0]["Type"] = 2
    data["data"][0]["Group"] = group
    data["data"][0]["Msg"] = msg

    data = json.dumps(data)
    try:
        requests.post(app.config["PUSH_URL"], headers=headers, data=data)
    except Exception as e:
        botLog.error("插件问题再现!")


def push_msg_temp(msg: str, obj_qq: str):
    data = copy.deepcopy(push_data)
    data["data"][0]["Type"] = 4
    data["data"][0]["Group"] = obj_qq
    data["data"][0]["Msg"] = msg

    data = json.dumps(data)
    try:
        requests.post(app.config["PUSH_URL"], headers=headers, data=data)
    except Exception as e:
        botLog.error("插件问题再现!")


if __name__ == '__main__':

    try:
        requests.post("http://127.0.0.1:6666/", headers=headers, data=push_msg_private("test", 'xxxx'))
    except Exception as e:
        pass

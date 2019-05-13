import json
import sdk.msgType as types

from copy import deepcopy
from sdk.datas import returnData,returnDataCell

class HTTPSDK():
    def __init__(self, postData):
        self.__returnDataCell = returnDataCell
        self.__postData = postData
        self.__sendData = deepcopy(returnData)

    def send(self):
        '''
        :return: 提交给插件的json数据
        '''
        return json.dumps(self.__sendData)


    def __addDataCell(self,
                      Type,
                      SubType=0,
                      StructureType=0,
                      Group='',
                      QQ='',
                      Msg='',
                      Data='',
                      Send=0):
        data = deepcopy(self.__returnDataCell)
        data["Type"] = Type
        data["SubType"] = SubType
        data["StructureType"] = StructureType
        data["Group"] = str(Group)
        data["QQ"] = str(QQ)
        data["Msg"] = Msg
        data["Data"] = Data
        data["Send"] = Send
        self.__sendData["data"].append(data)

    # 以下为具体功能

    # 发送私聊消息
    def sendPrivateMsg(self, qq, msg, structureType=0, subType=0):
        return self.__addDataCell(types.TYPE_FRIEND, subType, structureType, '',
                                  qq, msg, '', 0)

    # 发送群消息
    def sendGroupMsg(self, group, msg, structureType=0, subType=0):
        return self.__addDataCell(types.TYPE_GROUP, subType, structureType,
                                  group, '', msg, '', 0)

    # 发送讨论组消息
    def sendDiscussMsg(self, discuss, msg, structureType=0, subType=0):
        return self.__addDataCell(types.TYPE_DISCUSS, subType, structureType,
                                  discuss, '', msg, '', 0)

    # 向QQ点赞
    def sendLike(self, qq, count=1):
        return self.__addDataCell(types.TYPE_SEND_LIKE, 0, 0, '', qq, str(count), '',
                                  0)

    # 窗口抖动
    def sendShake(self, qq):
        return self.__addDataCell(types.TYPE_SEND_SHAKE, 0, 0, '', qq, '', '',
                                  0)

    # 是否同意被加好友
    def handleFriendAdd(self, qq, agree=True, msg=''):
        return self.__addDataCell(types.TYPE_FRIEND_HANDLE_FRIEND_ADD, 0, 0, '',
                                  qq, '1' if agree else '0', msg, 0)
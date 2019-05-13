from flask import Flask, request, jsonify

from app.util.data_format import data_format_forward
from app.util.db import DbUtils
from app.util.parse_cmd import parse_cmd
from app.util.utils import get_json
from config import config
from log import botLog
from push.push import push_msg_group
from sdk import HTTPSDK

app = Flask(__name__)
app.config.update(config)


@app.route('/', methods=["GET", "POST"])
def index():
    msg = request.get_data().decode()
    res = get_json(msg)
    botLog.info(res)
    if res.get("Type") == '2':
        if res.get("Group") == app.config["JUDGE_GROUP"]:
            cmd = res.get("Msg")
            sdk = HTTPSDK(res)
            # 解析指令，查找编号，排序
            key, value = parse_cmd(cmd)
            if key == "通过":
                # 查询enable是否为1 为1的话就提醒审核过了
                with DbUtils() as c:
                    enable = c.execute("SELECT enable FROM information WHERE id={}".format(value)).fetchone()
                if enable is None:
                    sdk.sendGroupMsg(app.config["JUDGE_GROUP"],"[ksust,at:qq={}] 参数错误! ".format(res.get("QQ")))
                    return sdk.send()
                if int(enable[0]) == 1:
                    sdk.sendGroupMsg(app.config["JUDGE_GROUP"], "[ksust,at:qq={}] {}已经审核过了! ".format(res.get("QQ"), value))
                else:
                    with DbUtils() as c:
                        c.execute("UPDATE information SET enable = 1 WHERE ID = {}".format(value))
                        max = c.execute("SELECT MAX(sort) FROM information WHERE time = date('now')")
                        max = max.fetchone()[0]
                        if max is None:
                            max = 0
                        c.execute("UPDATE information SET sort = {} WHERE ID = {}".format(int(max + 1), value))

                    sdk.sendGroupMsg(app.config["JUDGE_GROUP"], "[ksust,at:qq={}] 通过{}成功 ".format(res.get("QQ"), value))
                    # 转发消息
                    # TODO 消息队列
                    with DbUtils() as c:
                        r = c.execute("select * from information where id={}".format(value))
                        res = r.fetchone()
                    for group in app.config["PUSH_GROUP"]:
                        push_msg_group(data_format_forward(res[5], res[1], res[2], res[3]), group)


            elif key == "拒绝":
                sdk.sendGroupMsg(app.config["JUDGE_GROUP"], "[ksust,at:qq={}] 不通过{}成功 ".format(res.get("QQ"), value))
            else:
                botLog.info("cmd is not correct!")
            return sdk.send()

    return jsonify(success=True)


from app.api import api

app.register_blueprint(api)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

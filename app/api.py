import os

from flask import Blueprint, request, jsonify, current_app as app

from app.util.data_format import data_format
from app.util.db import DbUtils
from app.util.utils import get_random_filename
from log import botLog
from push.push import push_msg_group

api = Blueprint("api", __name__, url_prefix='/api/v1')


@api.route('/upload', methods=["POST"])
def get_info():
    if request.method == 'POST':

        # 只有文字
        res = request.get_json()
        if res != None:
            title = res["title"]
            content = res["content"]

            with DbUtils() as c:
                c.execute(
                    "INSERT INTO information (title,content,time) VALUES ('{}','{}',date('now'))".format(title,
                                                                                                         content))
                id = c.execute("SELECT LAST_INSERT_ROWID()").fetchone()[0]
                botLog.info("成功写入id({})".format(id))
                # TODO 转发到相关qq群中(主动推送)
                # TODO 队列，保证一定能转发成功和应对高并发的
                push_msg_group(data_format(id, title, content), app.config["JUDGE_GROUP"])
            return jsonify(code=1, msg="提交成功!")

        # 文字+图片
        filename = None
        if 'title' in request.form and 'content' in request.form:
            title = request.form["title"]
            content = request.form["content"]
        else:
            return jsonify(code=-1, msg="缺少参数{title,content}!")

        if 'file' in request.files:
            file = request.files['file']
            upload_folder = os.path.join(app.config['UPLOAD_FOLDER'])
            if not os.path.exists(upload_folder):
                os.mkdir(upload_folder)
            filename = os.path.join(upload_folder, "{}.jpg".format(get_random_filename()))
            file.save(filename)

        # 有图片
        if filename is not None:
            # 写入数据库
            with DbUtils() as c:
                c.execute(
                    "INSERT INTO information (title,content,img,time) VALUES ('{}','{}','{}',date('now'))".format(title,
                                                                                                                  content,
                                                                                                                  filename))
                id = c.execute("SELECT LAST_INSERT_ROWID()").fetchone()[0]
                botLog.info("成功写入id({})".format(id))
                # TODO 转发到相关qq群中(主动推送)
                # TODO 队列，保证一定能转发成功和应对高并发
                push_msg_group(data_format(id, title, content, filename), app.config["JUDGE_GROUP"])
        return jsonify(code=1, msg="提交成功!")

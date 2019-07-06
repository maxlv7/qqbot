import os

config = {
    "PUSH_URL": "http://139.196.98.165:6001/",
    # 审核群
    "JUDGE_GROUP": "644919551",
    # 用户群
    "PUSH_GROUP": ["565764426", "669065596", "364273302", "571600396", "640544764", "622080940", "928290072",
                   "821822935"],
    "UPLOAD_FOLDER": os.path.join(os.path.abspath(os.path.dirname(__file__)), "upload")
}

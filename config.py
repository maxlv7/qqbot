import os

config = {
    "PUSH_URL": "http://127.0.0.1:6666/",
    # 审核群
    "JUDGE_GROUP": "644919551",
    # 用户群
    "PUSH_GROUP": ["619569056","673863858","667850229","606902515"],
    "UPLOAD_FOLDER": os.path.join(os.path.abspath(os.path.dirname(__file__)), "upload")
}

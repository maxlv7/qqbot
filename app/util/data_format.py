from app.util.utils import to_online_pic


def data_format(id: str, title: str, content: str, img: str = None) -> str:
    if img is None:
        data = \
'''
审核编号:【{}】
标题：{}
内容：{}
通过请回复 通过+编号
拒绝请回复 拒绝+编号
如：通过 1'''.format(id, title, content)
    else:
        data = \
'''
审核编号:【{}】
标题：{}
内容：{}
图片: [ksust,image:pic={}]
通过请回复 通过+编号
拒绝请回复 拒绝+编号
如：通过 1'''.format(id, title, content, to_online_pic(img))
    return data


# 审核成功，转发到指定群
def data_format_forward(sort: str, title: str, content: str, img: str = None) -> str:
    if img is None:
        data = '''
{}.【{}】{}
        '''.format(sort, title, content)
    else:
        data = '''
{}.【{}】{}
[ksust,image:pic={}]
         '''.format(sort, title, content, to_online_pic(img))
    return data

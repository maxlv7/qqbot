import re


def parse_cmd(cmd: str):
    # 正则表达式提取出有用的信息
    # 通过
    par = re.compile(r"通过 \d*")
    res = par.findall(cmd)
    if len(res) != 0:
        return res[0].split(" ")

    par1 = re.compile(r"拒绝 \d*")
    res1 = par1.findall(cmd)
    if len(res1) != 0:
        return res1[0].split(" ")

    par2 = re.compile(r"通过\d*")
    res2 = par2.findall(cmd)
    if len(res2) != 0:
        return res2[0].split(" ")

    par3 = re.compile(r"拒绝\d*")
    res3 = par3.findall(cmd)
    if len(res3) != 0:
        return res3[0].split(" ")

    return "error",-1

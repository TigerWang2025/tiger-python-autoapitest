import os
import pytest
import requests
import jsonpath
from xToolkit import xfile
from string import Template

print("DATAs22222:", os.path.dirname(os.getcwd()))  # 当前执行文件的路径
current_path1 = os.path.dirname(os.getcwd())  # 当前执行文件的上一层路径
current_path = os.path.join(current_path1, "resources", "Test.xls")
print("路径：", current_path)  # 当前执行文件的上一层路径，再拼接新的目录&文件的路径
datas = xfile.read(current_path).excel_to_dict(sheet=1)
# datas = xfile.read(r".\resources\Test.xls").excel_to_dict(sheet=0)  # 相对路径，建议使用相对路径
# datas = xfile.read(r"D:\CodeSpace\tiger-python-autoapitest\resources\Test.xls").excel_to_dict(sheet=0)  # 绝对路径
print("DATATTTT:", datas)

dic = {}


@pytest.mark.parametrize("case_info", datas)  # 和for循环一样，循环数据
def test_excute(case_info):
    url = Template(case_info["接口URL"]).substitute(dic)
    result = requests.request(url=url,
                              method=case_info["请求方式"],
                              params=eval(case_info["URL参数"]),
                              data=eval(case_info["JSON参数"]))
    print(result.json())

    assert result.status_code == 200

    if case_info["提取参数"]:
        token = jsonpath.jsonpath(result.json(), "$.." + case_info["提取参数"])
        dic[case_info["提取参数"]] = token[0]


# for case_info in datas:
#     excute(case_info)


# case_info = {"接口URL": "http://shop-xo.hctestedu.com/index.php?s=api/user/login",
#              "请求方式": "post",
#              "URL参数": {"application": "app", "application_client_type": "weixin"},
#              "JSON参数": {"accounts": "huace_xm", "pwd": "123456", "type": "username"}}


if __name__ == '__main__':
    # 运行 pytest 并生成 allure 结果
    pytest.main([
        "-vs",
        "--capture=sys",
        "test_framework.py",
        "--alluredir=allure-result"
    ])

    # 生成 allure 报告
    os.system("allure generate allure-result -o ./report-allure --clean")

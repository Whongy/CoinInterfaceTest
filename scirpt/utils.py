import os
import json
import sys

from os.path import dirname

sys.path.append(dirname(dirname(__file__)))
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


base_url = "https://futures.coin-up.pro"
token ='631e7f97683ec9ffc89af62c84deb751c9625e39c53b4fe384b352248e77cb49'
base_HEADERS = {"authority": "futures.coin-up.pro",
                "method":"POST",
                "path":"fe-ex-api/common/user_info",
                "scheme": "https",
                "content-type":"application/json;charset=UTF-8",
                "exchange-token":token,
                "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
                }





#定义统一的读取所有参数文件的方法,此方法 将上方 俩个读取配置文件得方法 抽象为一个方法，read_register_data   read_imgVerify_data
def read_param_data(filename,method_name,param_names):

    #filename: 参数数据文件的文件名
    #method_name: 参数数据文件中定义的测试数据列表的名称， 如 test_get_img_verify_code
    #
    #param_name  参数数据文件一组测试数据中所有的参数组成的字符串,如：type,status_code

    #获取测试数据的文件的文件路径
    file = base_url + "/data/" + filename
    test_case_data = []
    with open(file,encoding="utf-8")as f:
        #将JSON字符串转换为字典格式
        file_data = json.load(f)
    #获取所有测试数据的列表
        test_data_list = file_data.get(method_name)
        for test_data in test_data_list:
            # 将test_data对应的一组测试数据，全部读取出来，并生成一个列表
            test_params =[]
            for param in param_names.split(","):
            #依次获取同一组测试数据中的每个参数的值，添加到test_params中,形成一个列表
                test_params.append(test_data.get(param))
            #每完成一组测试数据的读取，就添加到test_case_data后, 直到所有的测试数据读取完成
            test_case_data.append(test_params)
    print("test_case_data={}".format(test_case_data))
    return test_case_data

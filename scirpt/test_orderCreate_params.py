from datetime import datetime
import requests
import pytest
from utils import base_url,base_HEADERS,read_param_data
import yaml
import json
import sys
import allure

from os.path import dirname

sys.path.append(dirname(dirname(__file__)))


import allure
import logging
headres = base_HEADERS


#@pytest.mark.parametrize("contractId,volume,price",[["45","BUY","0.1860986085","3","OPEN"],["47","BUY","0.1860986085","3","OPEN"]])

#限价开仓
@pytest.mark.normal
@pytest.mark.parametrize("contractId,price,volume",[["41","102.75","2"]])
def test_orderCreate_open(contractId,price,volume):
    print(volume)
    orderCreateUrl = base_url + '/fe-co-api/order/order_create'

    data = json.dumps({"desc": "XLM买入开多","contractId":contractId,"positionType":2,"side":"BUY","leverageLevel":22,"price":price,"volume":volume,
                       "triggerPrice":"null","open":"OPEN","type":1,"isConditionOrder":"false","uaTime":"2022-04-25 09:19:13",
                       "securityInfo":"{\"id\":\"\",\"org\":\"futures.coin-up.pro\",\"timestamp\":\"2022-04-25 09:19:13\",\"userAgent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36\",\"availableScreenResolution\":\"1707;1027\",\"screenResolution\":\"1707;1067\",\"touchSupport\":\"0;false;false\",\"sessionStorage\":1,\"localStorage\":1,\"indexedDb\":1,\"plugins\":\"PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf,Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf,Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf,Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf,WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"fonts\":\"Arial;Arial Black;Arial Narrow;Book Antiqua;Bookman Old Style;Calibri;Cambria;Cambria Math;Century;Century Gothic;Century Schoolbook;Comic Sans MS;Consolas;Courier;Courier New;Georgia;Helvetica;Impact;Lucida Bright;Lucida Calligraphy;Lucida Console;Lucida Fax;Lucida Handwriting;Lucida Sans;Lucida Sans Typewriter;Lucida Sans Unicode;Microsoft Sans Serif;Monotype Corsiva;MS Gothic;MS PGothic;MS Reference Sans Serif;MS Sans Serif;MS Serif;Palatino Linotype;Segoe Print;Segoe Script;Segoe UI;Segoe UI Light;Segoe UI Semibold;Segoe UI Symbol;Tahoma;Times;Times New Roman;Trebuchet MS;Verdana;Wingdings;Wingdings 2;Wingdings 3\",\"client_type\":\"\",\"identity\":\"\",\"device\":\"d46c0e699f229dc6539b06da6333973d\",\"ip\":\"\",\"ip2region\":\"\",\"language\":\"zh-CN\",\"platform\":\"Win32\",\"browser\":\"\",\"browser_version\":\"\",\"os\":\"\",\"os_version\":\"\",\"resolution\":\"\",\"timezone\":\"Asia/Shanghai\",\"ctime\":\"\",\"mtime\":\"\"}"})



    response = requests.post(url=orderCreateUrl, headers=headres,data=data)
    print(response.json())

    orderId = response.json().get("data").get("ids")
    msg = response.json().get("msg")
    assert response.status_code ==200
    assert msg =="成功"


#平仓市价
@pytest.mark.smoke
@pytest.mark.parametrize("contractId,volume",[["41","2"]])
def test_orderCreate_colseSuccess(contractId,volume):
    print(volume)
    orderCreateUrl = base_url + '/fe-co-api/order/order_create'

    data = json.dumps({"desc": "XLM限价卖出平多","contractId":contractId,"positionType":2,"side":"SELL","leverageLevel":22,"price":"0","volume":volume,
                       "triggerPrice":"null","open":"CLOSE","type":2,"isConditionOrder":"false","uaTime":"2022-04-25 09:19:13",
                       "securityInfo":"{\"id\":\"\",\"org\":\"futures.coin-up.pro\",\"timestamp\":\"2022-04-29 09:19:13\",\"userAgent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36\",\"availableScreenResolution\":\"1707;1027\",\"screenResolution\":\"1707;1067\",\"touchSupport\":\"0;false;false\",\"sessionStorage\":1,\"localStorage\":1,\"indexedDb\":1,\"plugins\":\"PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf,Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf,Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf,Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf,WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"fonts\":\"Arial;Arial Black;Arial Narrow;Book Antiqua;Bookman Old Style;Calibri;Cambria;Cambria Math;Century;Century Gothic;Century Schoolbook;Comic Sans MS;Consolas;Courier;Courier New;Georgia;Helvetica;Impact;Lucida Bright;Lucida Calligraphy;Lucida Console;Lucida Fax;Lucida Handwriting;Lucida Sans;Lucida Sans Typewriter;Lucida Sans Unicode;Microsoft Sans Serif;Monotype Corsiva;MS Gothic;MS PGothic;MS Reference Sans Serif;MS Sans Serif;MS Serif;Palatino Linotype;Segoe Print;Segoe Script;Segoe UI;Segoe UI Light;Segoe UI Semibold;Segoe UI Symbol;Tahoma;Times;Times New Roman;Trebuchet MS;Verdana;Wingdings;Wingdings 2;Wingdings 3\",\"client_type\":\"\",\"identity\":\"\",\"device\":\"d46c0e699f229dc6539b06da6333973d\",\"ip\":\"\",\"ip2region\":\"\",\"language\":\"zh-CN\",\"platform\":\"Win32\",\"browser\":\"\",\"browser_version\":\"\",\"os\":\"\",\"os_version\":\"\",\"resolution\":\"\",\"timezone\":\"Asia/Shanghai\",\"ctime\":\"\",\"mtime\":\"\"}"})



    response = requests.post(url=orderCreateUrl, headers=headres,data=data)
    print(response.json())
# TestData.test_orderCreate_open()
#
    orderId = response.json().get("data").get("ids")
    msg = response.json().get("msg")
#      print(orderId)
#      print(succ)

    assert response.status_code ==200
    assert msg =="成功"


#市价平仓超出可平量
@pytest.mark.smoke
@pytest.mark.parametrize("contractId,volume",[["41","2"]])
def test_orderCreate_colseFail(contractId,volume):
    print(volume)
    orderCreateUrl = base_url + '/fe-co-api/order/order_create'

    data = json.dumps({"desc": "XLM限价卖出平多","contractId":contractId,"positionType":2,"side":"SELL","leverageLevel":22,"price":"0","volume":volume,
                       "triggerPrice":"null","open":"CLOSE","type":2,"isConditionOrder":"false","uaTime":"2022-04-25 09:19:13",
                       "securityInfo":"{\"id\":\"\",\"org\":\"futures.coin-up.pro\",\"timestamp\":\"2022-04-29 09:19:13\",\"userAgent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36\",\"availableScreenResolution\":\"1707;1027\",\"screenResolution\":\"1707;1067\",\"touchSupport\":\"0;false;false\",\"sessionStorage\":1,\"localStorage\":1,\"indexedDb\":1,\"plugins\":\"PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf,Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf,Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf,Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf,WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"fonts\":\"Arial;Arial Black;Arial Narrow;Book Antiqua;Bookman Old Style;Calibri;Cambria;Cambria Math;Century;Century Gothic;Century Schoolbook;Comic Sans MS;Consolas;Courier;Courier New;Georgia;Helvetica;Impact;Lucida Bright;Lucida Calligraphy;Lucida Console;Lucida Fax;Lucida Handwriting;Lucida Sans;Lucida Sans Typewriter;Lucida Sans Unicode;Microsoft Sans Serif;Monotype Corsiva;MS Gothic;MS PGothic;MS Reference Sans Serif;MS Sans Serif;MS Serif;Palatino Linotype;Segoe Print;Segoe Script;Segoe UI;Segoe UI Light;Segoe UI Semibold;Segoe UI Symbol;Tahoma;Times;Times New Roman;Trebuchet MS;Verdana;Wingdings;Wingdings 2;Wingdings 3\",\"client_type\":\"\",\"identity\":\"\",\"device\":\"d46c0e699f229dc6539b06da6333973d\",\"ip\":\"\",\"ip2region\":\"\",\"language\":\"zh-CN\",\"platform\":\"Win32\",\"browser\":\"\",\"browser_version\":\"\",\"os\":\"\",\"os_version\":\"\",\"resolution\":\"\",\"timezone\":\"Asia/Shanghai\",\"ctime\":\"\",\"mtime\":\"\"}"})



    response = requests.post(url=orderCreateUrl, headers=headres,data=data)
    print(response.json())
# TestData.test_orderCreate_open()
#
    orderId = response.json().get("data").get("ids")
    msg = response.json().get("msg")
#      print(orderId)
#      print(succ)

    assert response.status_code ==200
    assert msg =="平仓超出仓位总量"
if __name__ == '__main__':
        pytest.main('-v','test_orderCreate_param.py')




#{"contractId": 41, "positionType": 2, "side": "BUY", "leverageLevel": 10, "price": 105.21, "volume": "3","triggerPrice": "null", "open": "OPEN", "type": 1, "isConditionOrder": "false","uaTime": "2022-04-25 20:10:34","securityInfo":"{\"id\":\"\",\"org\":\"futures.coin-up.pro\",\"timestamp\":\"2022-04-25 20:10:34\",\"userAgent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36\",\"availableScreenResolution\":\"1707;1027\",\"screenResolution\":\"1707;1067\",\"touchSupport\":\"0;false;false\",\"sessionStorage\":1,\"localStorage\":1,\"indexedDb\":1,\"plugins\":\"PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf,Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf,Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf,Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf,WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"fonts\":\"Arial;Arial Black;Arial Narrow;Book Antiqua;Bookman Old Style;Calibri;Cambria;Cambria Math;Century;Century Gothic;Century Schoolbook;Comic Sans MS;Consolas;Courier;Courier New;Georgia;Helvetica;Impact;Lucida Bright;Lucida Calligraphy;Lucida Console;Lucida Fax;Lucida Handwriting;Lucida Sans;Lucida Sans Typewriter;Lucida Sans Unicode;Microsoft Sans Serif;Monotype Corsiva;MS Gothic;MS PGothic;MS Reference Sans Serif;MS Sans Serif;MS Serif;Palatino Linotype;Segoe Print;Segoe Script;Segoe UI;Segoe UI Light;Segoe UI Semibold;Segoe UI Symbol;Tahoma;Times;Times New Roman;Trebuchet MS;Verdana;Wingdings;Wingdings 2;Wingdings 3\",\"client_type\":\"\",\"identity\":\"\",\"device\":\"d46c0e699f229dc6539b06da6333973d\",\"ip\":\"\",\"ip2region\":\"\",\"language\":\"zh-CN\",\"platform\":\"Win32\",\"browser\":\"\",\"browser_version\":\"\",\"os\":\"\",\"os_version\":\"\",\"resolution\":\"\",\"timezone\":\"Asia/Shanghai\",\"ctime\":\"\",\"mtime\":\"\"}"}
# @pytest.mark.parametrize("contractId,positionType,side,leverageLevel,price,volume,triggerPrice,open,type,isConditionOrder,uaTime,securityInfo",yaml.safe_load(open("./orderCreate.yml")))
# contractId,positionType,side,leverageLevel,price,volume,triggerPrice,open,type,isConditionOrder,uaTime,securityInfo
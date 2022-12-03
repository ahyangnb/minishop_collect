import requests  # 导入requests包
import json

token = "a8b8ea51353e49c1ac23039e4586969d"
# 根据类别获取商品列表
def getGoodsListOfCategory(current=1, twoCategoryId=5):
    url = 'https://bjsc.szbaoly.com/api/agent/pageGoods?current=' + str(current) + '&size=10&total=-1&twoCategoryId=' + str(twoCategoryId) + '&keyword='
    headersData = {
        "Host": "bjsc.szbaoly.com",
        "appId": "wxeed6d656b89aeef3",
        "Accept": "*/*",
        "appletVersion": "2.0.7",
        "terminal": "2",
        "cId": "1",
        "Accept-Language": "en-us",
        "Accept-Encoding": "gzip, deflate, br",
        "token": token,
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "https",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E217 MicroMessenger/6.8.0(0x16080000) NetType/WIFI Language/en Branch/Br_trunk MiniProgramEnv/Mac",
        "Connection": "keep-alive",
        "client": "1",
        "aId": "677"
    }
    # 请求表单数据
    response = requests.post(url, headers=headersData, verify=False)
    # 将Json格式字符串转字典
    content = json.loads(response.text)
    print("HTTP::getGoodsListOfCategory::"+str(content))


# 根据类别获取商品列表
def getCategoryList():
    url = 'https://bjsc.szbaoly.com/api/agent/pageGoods?current=1&size=10&total=-1&twoCategoryId=4&keyword='
    headersData = {
        "Host": "bjsc.szbaoly.com",
        "appId": "wxeed6d656b89aeef3",
        "Accept": "*/*",
        "appletVersion": "2.0.7",
        "terminal": "2",
        "cId": "1",
        "Accept-Language": "en-us",
        "Accept-Encoding": "gzip, deflate, br",
        "token": token,
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "https",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E217 MicroMessenger/6.8.0(0x16080000) NetType/WIFI Language/en Branch/Br_trunk MiniProgramEnv/Mac",
        "Connection": "keep-alive",
        "client": "1",
        "aId": "677"
    }
    # 请求表单数据
    response = requests.post(url, headers=headersData)
    # 将Json格式字符串转字典
    content = json.loads(response.text)
    print("HTTP::getGoodsListOfCategory::"+str(content))

def jsonOption():
    # use mock json to test load.
    content = json.loads('{"a":1,"data":[]}')
    # use "[" and "]" center input key to fetch value.
    print("HTTP::jsonOption::"+str(content['a']))

if __name__ == '__main__':
    jsonOption()

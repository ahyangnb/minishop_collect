import requests  # 导入requests包
import json
import pymysql

token = "a8b8ea51353e49c1ac23039e4586969d"


# 根据类别获取商品列表
def getGoodsListOfCategory(current=1, twoCategoryId=5):
    url = 'https://bjsc.szbaoly.com/api/agent/pageGoods?current=' + str(
        current) + '&size=10&total=-1&twoCategoryId=' + str(twoCategoryId) + '&keyword='
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
    print("HTTP::getGoodsListOfCategory::" + str(content))


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
    print("HTTP::getGoodsListOfCategory::" + str(content))


def jsonOption():
    # use mock json to test load.
    content = json.loads('{"a":1,"data":[]}')
    # use "[" and "]" center input key to fetch value.
    print("HTTP::jsonOption::" + str(content['a']))


def searchGoods(cursor, store_name):
    # SQL 查询语句
    sql = "SELECT * FROM `db_mini_shop`.`eb_store_product` WHERE store_name = '%s'" % (store_name)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        # 打印结果
        print("Search goods result is %s" % (str(results)))
    except:
        print("Error: unable to fetch data")


def optiomSql():
    # 打开数据库连接
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='Budengyu1.',
                         database='db_mini_shop')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT VERSION()")
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()
    print("Database version : %s " % data)
    searchGoods(cursor, '展艺进口无盐黄油20粒动物煎牛排专用奶油面包饼干烘培家用小包装')
    # 关闭数据库连接
    db.close()


if __name__ == '__main__':
    optiomSql()

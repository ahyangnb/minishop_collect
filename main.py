import sys

import requests  # 导入requests包
import json
import pymysql

token = "ed4eb3db76374bc7885e5cfc454224e0"
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


def get_img_h1(url):
    return 'http://oss-hxq-prod.szbaoly.com/bjsc/goods/' + str(url).replace('"','') + '?x-oss-process=style/h1'


# 根据类别获取商品列表
def getGoodsDet(id=16820):
    url = 'https://bjsc.szbaoly.com/api/agent/getGoodsDetail?id=' + str(
        id) + '&selectType=0&sceneType=&sceneId='
    # 请求表单数据
    response = requests.post(url, headers=headersData, verify=False)
    # 将Json格式字符串转字典
    content = json.loads(response.text)
    print("HTTP::getGoodsDet::" + str(content))
    if content['code'] != 200 & content['code'] != 0:
        return None
    return content['result']


# 根据类别获取商品列表
def getGoodsListOfCategory(current=1, twoCategoryId=5):
    url = 'https://bjsc.szbaoly.com/api/agent/pageGoods?current=' + str(
        current) + '&size=10&total=-1&twoCategoryId=' + str(twoCategoryId) + '&keyword='
    # 请求表单数据
    response = requests.post(url, headers=headersData, verify=False)
    # 将Json格式字符串转字典
    content = json.loads(response.text)
    print("HTTP::getGoodsListOfCategory::" + str(content))


# 根据类别获取商品列表
def getCategoryList():
    url = 'https://bjsc.szbaoly.com/api/agent/pageGoods?current=1&size=10&total=-1&twoCategoryId=4&keyword='
    # 请求表单数据
    response = requests.post(url, headers=headersData)
    # 将Json格式字符串转字典
    content = json.loads(response.text)
    print("HTTP::getGoodsListOfCategory::" + str(content))


def searchGoods(cursor, store_name):
    # SQL 查询语句
    sql = "SELECT * FROM `eb_store_product` WHERE store_name = '%s'" % (store_name)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        # 打印结果
        print("SEARCH::searchGoods:: Search goods result is %s" % (str(results)))
        if str(results) == '()':
            return str(results)
        return None
    except:
        print("Error: unable to fetch data")
        return None


def innsertData(cursor, db, goodsData):
    # result list of img.
    result_img_list = []
    slider_image_list = goodsData['imgs']

    if ', ' in slider_image_list:
        res = slider_image_list.strip('][').split(', ')
    else:
        res = slider_image_list.strip('][').split(',')

    # Result and its type
    for str_item in res:
        str_item_new = get_img_h1(str_item)
        result_img_list.append(str_item_new)

    # print the result.
    print("result_img_list value is ", str(result_img_list))

    # dump data
    dump_data = json.dumps(result_img_list)
    print("result_img_list value of json is ", dump_data)

    # SQL inner oprate.
    import time
    sql = """INSERT INTO `eb_store_product` (`mer_id`, `image`, `recommend_image`, `slider_image`, `store_name`, `store_info`
    , `keyword`, `bar_code`, `cate_id`, `price`, `vip_price`, `ot_price`, `postage`, `unit_name`,
     `sort`, `sales`, `stock`, `is_show`, `is_hot`, `is_benefit`, `is_best`, `is_new`, `is_virtual`,
      `virtual_type`, `add_time`, `is_postage`, `is_del`, `mer_use`, `give_integral`, `cost`, `is_seckill`,
       `is_bargain`, `is_good`, `is_sub`, `is_vip`, `ficti`, `browse`, `code_path`, `soure_link`, `video_link`,
        `temp_id`, `spec_type`, `activity`, `spu`, `label_id`, `command_word`, `recommend_list`, `vip_product`,
         `presale`, `presale_start_time`, `presale_end_time`, `presale_day`, `logistics`, `freight`, `custom_form`) VALUES
(%s, '%s', '%s','%s', '%s', '%s', '%s', 
 '%s', '%s', '%s', '%s', '%s', '%s', '%s', %s,%s , %s, %s,%s , %s, %s, %s, %s, %s, %s, %s, %s,%s , '%s', '%s', %s, %s, %s, %s, %s, %s, %s
 , '%s', '%s', '%s', %s, %s, '%s',
  '%s', '%s', '%s', '%s', %s, %s, %s, %s, %s, '%s', %s, '%s');""" % (
        # Real value inner.
        0, get_img_h1(goodsData['itemMainImg']),
        '',
        str(dump_data),
        goodsData['name'],
        goodsData['name'],
        '','',
        '4', str(goodsData['marketPrice']), str(goodsData['currVipPrice']), str(goodsData['marketPrice']), '0.00',
        # unit_name
        goodsData['unit'],
        0, goodsData['sales'], goodsData['stock'], 0, 1, 1, 1, 1, 0,
        # virtual_type
        0,
        # add_time   1642241487
        time.time(), 1, 0, 0, '0.00',
        # cost
        str(goodsData['currVipPrice']), 0, 0, 1, 0, 1, 0, 0, '', '', '', 1,
        # todo spec_type 规格 0单 1多
        1,
        '0,1,2,3',
        # spu
        str(goodsData['goodsId']), '', '', '',
        # vip_product 是否会员专属商品
        0, 0, 0, 0, 0,
        # logistics
        '1,2', 3, '[]',
    )
    try:
        print("Start innert Data.")
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        print("data innser success.")
    except:
        print("[data innser except.] Oops!", sys.exc_info()[0], "occurred.")
        # 如果发生错误则回滚
        db.rollback()


def optiomSql(goodsData):
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
    search_goods_result = searchGoods(cursor, goodsData['name'])
    if search_goods_result is not None:
        print("Can inner data")
        innsertData(cursor, db, goodsData)
    else:
        print("Un need ")
    # 关闭数据库连接
    db.close()


if __name__ == '__main__':
    goodsResult = getGoodsDet()
    if goodsResult is not None:
        optiomSql(goodsResult)

    # jsonOption()
    # optiomSql()

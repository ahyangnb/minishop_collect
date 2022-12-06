import html
import sys

import requests  # 导入requests包
import json
import pymysql

token = "15ad6ec4ac214f13b58caa5f3d6445a8"
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
    return 'http://oss-hxq-prod.szbaoly.com/bjsc/goods/' + str(url).replace('"', '') + '?x-oss-process=style/h1'
def get_img_des(url):
    return 'http://oss-hxq-prod.szbaoly.com/bjsc/goods/' + str(url).replace('"', '') + '?x-oss-process=style/gd'
def get_video_full_url(url):
    if url is None :
        return ''
    if url == '':
        return url
    # http://oss-hxq-prod.szbaoly.com/bjsc/goods/2d2d32d0cd1d400c9e62b8b008d2f308.mp4
    return 'http://oss-hxq-prod.szbaoly.com/bjsc/goods/' + str(url).replace('"', '')


# 根据类别获取商品列表
def getGoodsDet(id=13261):
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

# 规格处理
# def getProp():
#     # https://bjsc.szbaoly.com/api/agent/getGoodsItemDetailById?id=13261&type=1
#     return 1


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


def get_det_slider_img_list(goodsData):
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

    # add main pic
    result_img_list.append(goodsData['itemMainImg'])

    # dump data
    dump_data_of_img = json.dumps(result_img_list)
    print("[result_img_list] value of json is ", dump_data_of_img)
    return dump_data_of_img


def get_det_decription_img_list(goodsData):
    # result list of img.
    result_des_img_list = []
    des_image_list = goodsData['detailImgs']

    if ', ' in des_image_list:
        res = des_image_list.strip('][').split(', ')
    else:
        res = des_image_list.strip('][').split(',')

    # Result and its type
    for str_item in res:
        str_item_new = get_img_des(str_item)
        result_des_img_list.append(str_item_new)
    return result_des_img_list


def innsertData(cursor, db, goodsData):
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
        str(get_det_slider_img_list(goodsData)),
        goodsData['name'],
        goodsData['name'],
        '', '',
        '4', str(goodsData['marketPrice']), str(goodsData['currVipPrice']), str(goodsData['marketPrice']), '0.00',
        # unit_name
        goodsData['unit'],
        0, goodsData['sales'], goodsData['stock'],
        # is_show
        0, 0, 0, 0, 0, 0,
        # virtual_type
        0,
        # add_time   1642241487
        time.time(), 1, 0, 0, '0.00',
        # cost
        str(goodsData['currVipPrice']), 0, 0, 1, 0, 1, 0, 0, '', '',
        # video_link
        get_video_full_url(goodsData['goodsVideo']),
        1,
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
        print("innert Data success.")

        goods_result_id = get_insert_goods_id(cursor, goodsData['name'])
        print("data innser success. id is ", goods_result_id)
        return goods_result_id
    except:
        print("[data innser except.] Oops!", sys.exc_info()[0], "occurred.")
        # 如果发生错误则回滚
        db.rollback()
        return None


def get_insert_goods_id(cursor, store_name):
    # SQL 查询语句
    sql = "SELECT * FROM `eb_store_product` WHERE store_name = '%s'" % (store_name)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchone()
        # 打印结果
        print("SEARCH::get_insert_goods_id:: Search goods result is %s" % (str(results[0])))
        if str(results) == '()':
            return None
        return results[0]
    except:
        print("Error[get_insert_goods_id]: unable to fetch data", sys.exc_info()[0], "occurred.")
        return None
    # # 使用 execute()  方法执行 SQL 查询
    # cursor.execute("SELECT * FROM eb_store_product WHERE store_name='%s';" % (goods_name))
    # # 使用 fetchone() 方法获取单条数据.
    # data = cursor.fetchone()
    # return data['id']


def insert_des(goods_id, goodsData,cursor, db):
    print('When insert des data of id ', goods_id)
    get_des_img_str = ''

    print("length ", len(get_det_decription_img_list(goodsData)))
    for currenUrl in get_det_decription_img_list(goodsData):
        get_des_img_str += '<p><img style="max-width:100%;height:auto;display:block;margin-top:0;margin-bottom:0;"  src="' + currenUrl + '"/></p>'
    print('[insert_des] get_des_img_str is ', get_des_img_str)

    desHtmlResult = html.escape(get_des_img_str)
    print('[insert_des] html is ', )
    insert_des_sql(goods_id, desHtmlResult,cursor,db)


def insert_des_sql(goods_id, desHtmlResult,cursor, db):
    sql = '''INSERT INTO `eb_store_product_description` (`product_id`, `description`, `type`) VALUES
(%s, '%s', 0);''' % (goods_id,desHtmlResult)
    try:
        print("Start innert des Data.")
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        print("innert des Data success.")
        return 1
    except:
        print("[data innser except.] Oops!", sys.exc_info()[0], "occurred.")
        # 如果发生错误则回滚
        db.rollback()
        return None


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
        goods_id = innsertData(cursor, db, goodsData)
        if goods_id is not None:
            insert_des(goods_id, goodsData,cursor, db)
    else:
        print("Un need ", goodsData['name'])
        goods_result_id = get_insert_goods_id(cursor, goodsData['name'])
        print("[Un need] already contain", goods_result_id)
    # 关闭数据库连接
    db.close()


if __name__ == '__main__':
    goodsResult = getGoodsDet()
    if goodsResult is not None:
        optiomSql(goodsResult)

    # jsonOption()
    # optiomSql()

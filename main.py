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
    sql = "SELECT * FROM `eb_store_product` WHERE store_name = '%s'" % (store_name)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        # 打印结果
        print("Search goods result is %s" % (str(results)))
    except:
        print("Error: unable to fetch data")


def innsertData(cursor, db):
    # SQL 插入语句
    sql = """INSERT INTO `eb_store_product` (`mer_id`, `image`, `recommend_image`, `slider_image`, `store_name`, `store_info`, `keyword`, `bar_code`, `cate_id`, `price`, `vip_price`, `ot_price`, `postage`, `unit_name`, `sort`, `sales`, `stock`, `is_show`, `is_hot`, `is_benefit`, `is_best`, `is_new`, `is_virtual`, `virtual_type`, `add_time`, `is_postage`, `is_del`, `mer_use`, `give_integral`, `cost`, `is_seckill`, `is_bargain`, `is_good`, `is_sub`, `is_vip`, `ficti`, `browse`, `code_path`, `soure_link`, `video_link`, `temp_id`, `spec_type`, `activity`, `spu`, `label_id`, `command_word`, `recommend_list`, `vip_product`, `presale`, `presale_start_time`, `presale_end_time`, `presale_day`, `logistics`, `freight`, `custom_form`) VALUES
(0, 'https://data44.wuht.net//uploads/attach/2022/01/15/8a2d668e1b8fde3ed9422c242eedbb32.jpg', '',
 '[\"https:\\/\\/data44.wuht.net\\/\\/uploads\\/attach\\/2022\\/01\\/15\\/8a2d668e1b8fde3ed9422c242eedbb32.jpg\",\"https:\\/\\/data44.wuht.net\\/\\/uploads\\/attach\\/2022\\/01\\/15\\/b4dc68ca453c74fda4ffcf385b0d4414.jpg\",\"https:\\/\\/data44.wuht.net\\/\\/uploads\\/attach\\/2022\\/01\\/15\\/76559ec8017c8ac68ea5ecac8145b56c.jpg\",\"https:\\/\\/data44.wuht.net\\/\\/uploads\\/attach\\/2022\\/01\\/15\\/409219640e8cd3b347c306b566785f2d.jpg\",\"https:\\/\\/data44.wuht.net\\/\\/uploads\\/attach\\/2022\\/01\\/15\\/742ec1ba074a8cc3a95839bb230c4244.jpg\",\"https:\\/\\/data44.wuht.net\\/\\/uploads\\/attach\\/2022\\/01\\/15\\/680b6fb7bbbcba59bb8fd015b63413c0.jpg\",\"https:\\/\\/data44.wuht.net\\/\\/uploads\\/attach\\/2022\\/01\\/15\\/1294869126a770d8519686eec84c9734.jpg\",\"https:\\/\\/data44.wuht.net\\/\\/uploads\\/attach\\/2022\\/01\\/15\\/c3936b8d5ff3195edda9c3427c18a7d3.jpg\"]'
 , '111优家UPLUS ins风简约无痕发夹金属一字夹4个装（金色+银色 刘海边夹前额一字发卡碎发夹卡子夹子分发夹）', '优家UPLUS ins风简约无痕发夹金属一字夹4个装（金色+银色 刘海边夹前额一字发卡碎发夹卡子夹子分发夹）', '', 
 '', '4', '15.90', '0.00', '0.00', '0.00', '件', 0, 0, 400, 1, 1, 1, 1, 1, 0, 0, 1642241487, 0, 0, 0, '0.00', '15.90', 0, 0, 1, 0, 0, 0, 0, '', '', '', 1, 1, '0,1,2,3',
  '1025349510439', '', '', '', 0, 0, 0, 0, 0, '1,2', 3, '[]');"""
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        print("data innser success.")
    except:
        # 如果发生错误则回滚
        db.rollback()


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
    searchGoods(cursor, 's王府井')
    # innsertData(cursor, db)
    # 关闭数据库连接
    db.close()


if __name__ == '__main__':
    optiomSql()

import requests  # 导入requests包
import json
import pymysql

token = "a11eef2679854758bf1d5ee5c168e26a"
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

# 根据类别获取商品列表
def getGoodsDet(id=16347):
    url = 'https://bjsc.szbaoly.com/api/agent/getGoodsDetail?id=' + str(
        id) + '&selectType=0&sceneType=&sceneId='
    # 请求表单数据
    response = requests.post(url, headers=headersData, verify=False)
    # 将Json格式字符串转字典
    content = json.loads(response.text)
    print("HTTP::getGoodsDet::" + str(content))
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


def jsonOption():
    mockJson = '''{
	"msg": "操作成功！",
	"result": {
		"boxNum": 1,
		"canBoxBuy": 0,
		"canUpCm": 1,
		"canUpSm": 1,
		"code": "CPZG01",
		"currVipPrice": 108,
		"detailImgs": "["75d024791fec4f908e097d1bd09dceae.png","ba4fb8852ea04a40ad7ef143eb275992.jpg"]",
		"forbidBuyArea": "",
		"goodsId": 16347,
		"goodsVideo": "",
		"id": 18746,
		"imgs": "["9a88be48f7bd429e88e2d3cce6832740.jpg","182543d86478464ab37e48435feec615.jpg","84d6bc5fb2b64c748b70eefcb6406e11.jpg","9049b92c9db144dda14e4fc5f49451f1.jpg"]",
		"itemMainImg": "beeb7acad249427989e59e0fcd8c7e95.jpg",
		"marketPrice": 999.00,
		"minBuyNum": 1,
		"name": "格卡诺6.8L家用大容量空气炸锅GKN-KQZG-16（珍珠白）",
		"piecesPerBox": "否",
		"plusStep": 1,
		"remoteAreaFreight": "",
		"sales": 4096,
		"specInfo": "{"颜色":"珍珠白"}",
		"specJson": "{"颜色":["珍珠白"]}",
		"state": 1,
		"stock": 381,
		"supplierFreightPayer": 2,
		"supplierType": 1,
		"title": "格卡诺6.8L家用大容量空气炸锅GKN-KQZG-16",
		"titleIcon": "[]",
		"type": 1,
		"unit": "台",
		"vip0Price": 133
	},
	"code": 0
}'''
    # use mock json to test load.
    content = json.loads(mockJson)
    # use "[" and "]" center input key to fetch value.
    print("HTTP::jsonOption::" + str(content))


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
        return str(results)
    except:
        print("Error: unable to fetch data")
        return None


def innsertData(cursor, db, goodsData):
    # SQL 插入语句
    sql = """INSERT INTO `eb_store_product` (`mer_id`, `image`, `recommend_image`, `slider_image`, `store_name`, `store_info`, `keyword`, `bar_code`, `cate_id`, `price`, `vip_price`, `ot_price`, `postage`, `unit_name`, `sort`, `sales`, `stock`, `is_show`, `is_hot`, `is_benefit`, `is_best`, `is_new`, `is_virtual`, `virtual_type`, `add_time`, `is_postage`, `is_del`, `mer_use`, `give_integral`, `cost`, `is_seckill`, `is_bargain`, `is_good`, `is_sub`, `is_vip`, `ficti`, `browse`, `code_path`, `soure_link`, `video_link`, `temp_id`, `spec_type`, `activity`, `spu`, `label_id`, `command_word`, `recommend_list`, `vip_product`, `presale`, `presale_start_time`, `presale_end_time`, `presale_day`, `logistics`, `freight`, `custom_form`) VALUES
(0, 'https://data44.wuht.net//uploads/attach/2022/01/15/8a2d668e1b8fde3ed9422c242eedbb32.jpg', '',
 '[\"https:\\/\\/data44.wuht.net\\/\\/uploads\\/attach\\/2022\\/01\\/15\\/8a2d668e1b8fde3ed9422c242eedbb32.jpg\",\"https:\\/\\/data44.wuht.net\\/\\/uploads\\/attach\\/2022\\/01\\/15\\/b4dc68ca453c74fda4ffcf385b0d4414.jpg\",\"https:\\/\\/data44.wuht.net\\/\\/uploads\\/attach\\/2022\\/01\\/15\\/76559ec8017c8ac68ea5ecac8145b56c.jpg\",\"https:\\/\\/data44.wuht.net\\/\\/uploads\\/attach\\/2022\\/01\\/15\\/409219640e8cd3b347c306b566785f2d.jpg\",\"https:\\/\\/data44.wuht.net\\/\\/uploads\\/attach\\/2022\\/01\\/15\\/742ec1ba074a8cc3a95839bb230c4244.jpg\",\"https:\\/\\/data44.wuht.net\\/\\/uploads\\/attach\\/2022\\/01\\/15\\/680b6fb7bbbcba59bb8fd015b63413c0.jpg\",\"https:\\/\\/data44.wuht.net\\/\\/uploads\\/attach\\/2022\\/01\\/15\\/1294869126a770d8519686eec84c9734.jpg\",\"https:\\/\\/data44.wuht.net\\/\\/uploads\\/attach\\/2022\\/01\\/15\\/c3936b8d5ff3195edda9c3427c18a7d3.jpg\"]'
 , '%s', '%s', '', 
 '', '4', '15.90', '0.00', '0.00', '0.00', '件', 0, 0, 400, 1, 1, 1, 1, 1, 0, 0, 1642241487, 0, 0, 0, '0.00', '15.90', 0, 0, 1, 0, 0, 0, 0, '', '', '', 1, 1, '0,1,2,3',
  '1025349510439', '', '', '', 0, 0, 0, 0, 0, '1,2', 3, '[]');""" % (goodsData['name'], goodsData['name'])
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        print("data innser success.")
    except:
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

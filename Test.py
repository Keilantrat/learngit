import requests;
import json;
import time;


def url_requests():
    #获取url地址
    url = 'https://j1.pupuapi.com/client/product/storeproduct/detail/4dcdeca2-f5a3-4be8-9e2f-e099889a23a0/0b777094-c58b-4fd0-843c-8c9d264d1e88'
    #头
    head = {
        'User-Agent': ': Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI '
                      'MiniProgramEnv/Windows WindowsWechat '
    }

    response = requests.get(url, headers=head, verify=False)

    dict = json.loads(response.text)#将字符串转为字典
    name = dict["data"]["name"]#获取商品的名称
    spec = dict["data"]["spec"]#获取商品规格
    price = str(int(dict["data"]["price"]) / 100)#获取商品原价
    market_price = str(int(dict["data"]["market_price"]) / 100)#获取商品原价/折扣价
    share_content = dict["data"]["share_content"]#获取商品详细内容
    #输出语句
    print("---------------商品：" + name + "----------------")
    print("规格：" + spec)
    print("原价：" + price)
    print("原价/折扣价：" + price + "/" + market_price)
    print("详细内容：" + share_content)
    print('\n')
    print("---------------" + name + "------------------")
    #循环获取信息
    i = 1
    for i in range(15):
        nowTimeandprint = time.strftime('%Y' + '-' + '%m' + '-' + '%d' + ' %H:%M:%S,价格为：' + price)
        print(nowTimeandprint)
        time.sleep(5)

    #main函数
if __name__ == '__main__':
    url_requests()#调用函数

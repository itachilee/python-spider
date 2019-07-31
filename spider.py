# -*- coding: UTF-8 -*-
from urllib import request
from urllib import parse
import json

def translate(i):
    # 对应上图的Request URL
    Request_URL = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    header ={}
    header['User-Agent'] ='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    # 创建Form_Data字典，存储上图的Form Data
    Form_Data = {}
    Form_Data['to'] = 'AUTO'
    Form_Data['i'] = i
    Form_Data['from'] = 'AUTO'
    Form_Data['smartresult'] = 'dict'
    Form_Data['client'] = 'fanyideskweb'
    Form_Data['salt'] = '15644904334192'
    Form_Data['sign'] = 'a86b1d86fbe1614705f1c60315c8de67'
    Form_Data['ts'] = '1564490433419'
    Form_Data['bv'] = '57d46cf581e5c43f8109a84cf9227e5e'
    Form_Data['doctype'] = 'json'
    Form_Data['version'] = '2.1'
    Form_Data['keyfrom'] = 'fanyi.web'
    Form_Data['action'] = 'FY_BY_REALTlME'
    # 使用urlencode方法转换标准格式
    data = parse.urlencode(Form_Data).encode('utf-8')
    #创建request对象
    req=request.Request(Request_URL,headers=header,data=data)
    # 传递Request对象和转换完格式的数据
    response = request.urlopen(req)
    # 读取信息并解码
    html = response.read().decode('utf-8')
    # 使用JSON
    translate_results = json.loads(html)
    # 找到翻译结果
    translate_results = translate_results['translateResult'][0][0]['tgt']
    # 打印翻译信息
    print("翻译的结果是：%s" % translate_results)


if __name__ == '__main__':
    translate('today is sunny')
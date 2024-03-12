import os
import requests

url = "https://wxhy.cpcity.vip/hddma/api/c/wx/signin/add"

headers = {
    "Connection": "keep-alive",
    "AuthorizationInf": 'MD5 appid="wx467816359f7bef2a",nonce_str="593BEC0C930BF1AFEB40B4A08C8FB242",signature="d1ba43d80917a2208bc36b2d2f779faf",timestamp="1710246730"',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309092b) XWEB/8555",
    "tenantId": "10000",
    "Content-Type": "application/json",
    "userName": "",
    "userId": "",
    "orgcode": "0102",
    "xweb_xhr": "1",
    "currentPageRoute": "pages/mbr/sign/index",
    "token": "",
    "Accept": "*/*",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://servicewechat.com/wx467816359f7bef2a/22/page-frame.html",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
}

data = {
    "appid": "wx467816359f7bef2a",
    "openId": "oSimT4s0pwV3G2wKVDtB9B4oOts4",
    "orgCode": "0102",
    "orgName": "Rmall全生活广场",
    "appId": "wx467816359f7bef2a",
}

response = requests.post(url=url, headers=headers, json=data)


print(response.text)

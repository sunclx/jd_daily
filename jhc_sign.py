import os
import requests

url = "https://wxhy.cpcity.vip/hddma/api/c/wx/signin/add"

headers = {
    "Connection": "keep-alive",
    "AuthorizationInf": 'MD5 appid="wxbc14026abc9ac6dc",nonce_str="593BEC0C930BF1AFEB40B4A08C8FB242",signature="c0ffc76d9b18160a7953de1d13f23f6d",timestamp="1710242144"',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309092b) XWEB/8555",
    "tenantId": "10000",
    "Content-Type": "application/json",
    "userName": "",
    "userId": "",
    "orgcode": "0101",
    "xweb_xhr": "1",
    "currentPageRoute": "pages/mbr/sign/index",
    "token": "",
    "Accept": "*/*",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://servicewechat.com/wxbc14026abc9ac6dc/27/page-frame.html",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
}
data = {
    "appid": "wxbc14026abc9ac6dc",
    "openId": "obHSZ5BcoilDo5iRzu276mRMq5cc",
    "orgCode": "0101",
    "orgName": "扬州京华城全生活广场",
    "appId": "wxbc14026abc9ac6dc",
}

response = requests.post(url=url, headers=headers, json=data)


print(response.text)

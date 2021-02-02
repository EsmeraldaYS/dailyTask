# coding=utf-8
import requests,os
import json

# 设置Server酱post地址 不需要可以删除
serverChan = "https://sc.ftqq.com/SCU157493T1325b7595c0c4982ad779bb315f49e13601918347f082.send"
# 状态地址
current_url = 'https://zhiyou.smzdm.com/user/info/jsonp_get_current'
# 签到地址
checkin_url = 'https://zhiyou.smzdm.com/user/checkin/jsonp_checkin'
# 用用户名和密码登录后获取Cookie
userCookie = '__ckguid=woE6QjkYINpQ6A5cs25V6A5; __jsluid_s=ad51cc538cedd0433e11c85c9c6cbb37; device_id=20718537341611125062019887f8fdd17dc1cb8d2455a7e710bd9b65f2; _ga=GA1.2.1964442828.1611125020; homepage_sug=d; r_sort_type=score; _zdmA.vid=*; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221771e88ccfb84b-01c6dcc0fd07b5-31346d-921600-1771e88ccfca39%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24latest_landing_page%22%3A%22https%3A%2F%2Fwww.smzdm.com%2F%22%7D%2C%22%24device_id%22%3A%221771e88ccfb84b-01c6dcc0fd07b5-31346d-921600-1771e88ccfca39%22%7D; gadsTest=test; Hm_lvt_9b7ac3d38f30fe89ff0b8a0546904e58=1612256883; zdm_qd=%7B%22referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%7D; _gid=GA1.2.1877491175.1612256883; footer_floating_layer=0; ad_date=2; ad_json_feed=%7B%7D; sess=MGU3YzF8MTYxNjE0NDk0MXw3MDY2MDgxODE4fDE5YmY5ZDYxOGY4Y2Y2NjNiNDE2YTM0ZTgzYWJjY2U3; user=user%3A7066081818%7C7066081818; smzdm_id=7066081818; _zdmA.uid=ZDMA.8x-TFwDg6.1612256943.2419200; Hm_lpvt_9b7ac3d38f30fe89ff0b8a0546904e58=1612256943; userId=user:7066081818|7066081818; bannerCounter=%5B%7B%22number%22%3A1%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A1%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A1%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A1%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A1%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A2%7D%5D; zdm_not_read=%7B%227066081818%22%3A%7B%22commit%22%3Anull%2C%22notice%22%3A%22787671225_43%22%7D%7D; __gads=ID=78aaae0c17a27053:T=1612256943:S=ALNI_MYP_f_mGhYp5nJmv9gok0EcRcC2ng; zdm_read_comment=%7B%227066081818%22%3A%5B168811649%5D%7D; amvid=7daa52dcdee6ea0cc89588c18b7cc571; _zdmA.time=1612256948617.2792.https%3A%2F%2Fwww.smzdm.com%2F'
headers = {
    'Referer': 'https://www.smzdm.com/',
    'Host': 'zhiyou.smzdm.com',
    'Cookie': userCookie,
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
}


def req(url):
    url = url
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        data = json.loads(res.text)
        return data


data = req(current_url)
if data['checkin']['has_checkin']:
    info = '%s ：%s 你目前积分：%s，经验值：%s，金币：%s，碎银子：%s，威望：%s，等级：%s，已经签到：%s天' % (data['sys_date'], data['nickname'], data['point'], data['exp'], data['gold'], data['silver'], data['prestige'], data['level'],data['checkin']['daily_checkin_num'])
    print(info)
    # 通过Server酱发送状态 不需要可以删除
    requests.post(serverChan, data={'text': data['nickname'] + '已经签到过了', 'desp': info})
else:
    checkin = req(checkin_url)['data']
    # print(checkin)
    info = '%s 目前积分：%s，增加积分：%s，经验值：%s，金币：%s，威望：%s，等级：%s' % (data['nickname'], checkin['point'], checkin['add_point'], checkin['exp'], checkin['gold'], checkin['prestige'], checkin['rank'])
    print(info)
    # 通过Server酱发送状态 不需要可以删除
    requests.post(serverChan, data={'text': data['nickname'] + '签到信息', 'desp': info})

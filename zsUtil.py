import requests

# 获取战双表单
def zhansuangTable(token, devCode):
    url = "http://api.kurobbs.com/gamer/widget/game2/getData"
    headers = {
        "devCode": devCode,
        "source": "android",
        "Cookie": f"user_token={token}",
        "token": token
    }
    data = {
        "gameId": "2",
        "type": "1",
        "sizeType": "1"
    }
    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    return response.text

def zhansuangRefresh(token, devCode):
    zhansuangTable(token, devCode)
    url = "http://api.kurobbs.com/gamer/widget/game2/refresh"
    headers = {
        "devCode": devCode,
        "source": "android",
        "Cookie": f"user_token={token}",
        "token": token
    }
    data = {
        "gameId": "2",
        "type": "1",
        "sizeType": "1"
    }
    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    return response.text

def serverSwich(token, devCode):
    url = "http://api.kurobbs.com/config/dict/timingSwitch"
    headers = {
        "version": "2.4.4",
        "devCode": devCode,
        "source": "android",
        "token": token,
        "countryCode": "CN",
        "lang": "zh-Hans",
        "channelId": "2",
        "Cookie": f"user_token={token}"

    }
    response = requests.get(url, headers=headers, timeout=30)
    response.raise_for_status()
    return response.text

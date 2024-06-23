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
    return response.text
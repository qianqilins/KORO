import requests, time

# 鸣潮签到 (roleId, userId 来自表单)
def mingchaoSignin(token, roleId, userId):
    urlsignin = "https://api.kurobbs.com/encourage/signIn/v2"
    headers = {
        "token": token,
        "devCode": "Kuro/2.4.4 KuroGameBox/2.4.4",
        "User-Agent": "Kuro/2.4.4 KuroGameBox/2.4.4",
        "source": "android"
    }
    datasign = {
        "gameId": "3",
        "serverId": "76402e5b20be2c39f095a152090afddc",
        "roleId": roleId,
        "userId": userId,
        "reqMonth": time.strftime("%m")
    }
    response = requests.post(urlsignin, headers=headers, data=datasign)
    # 检查响应状态码
    if response.status_code != 200:
        return (f"请求失败，状态码: {response.status_code}, 消息: {response.text}")
    response_data = response.json()
    if response_data.get("code") != 200:
        return (f"请求失败，响应代码: {response_data.get('code')}, 消息: {response_data.get('msg')}")
    try:
        goods_names = getmingchaoSignprize(token, roleId, userId)
        return goods_names
    except ValueError as e:
        print(f"获取奖品失败: {e}")
        return None

# 鸣潮物品 (roleId, userId 来自表单)
def getmingchaoSignprize(token, roleId, userId):
    urlqueryRecord = "https://api.kurobbs.com/encourage/signIn/queryRecordV2"
    headers = {
        "token": token,
        "devCode": "Kuro/2.4.4 KuroGameBox/2.4.4",
        "User-Agent": "Kuro/2.4.4 KuroGameBox/2.4.4",
        "source": "android"
    }
    data = {
        "gameId": "3",
        "serverId": "76402e5b20be2c39f095a152090afddc",
        "roleId": roleId,
        "userId": userId
    }
    response = requests.post(urlqueryRecord, headers=headers, data=data)
    # 检查响应状态码
    if response.status_code != 200:
        return (f"请求失败，状态码: {response.status_code}, 消息: {response.text}")
    response_data = response.json()
    if response_data.get("code") != 200:
        return (f"请求失败，响应代码: {response_data.get('code')}, 消息: {response_data.get('msg')}")
    data = response_data["data"]
    if isinstance(data, list) and len(data) > 0:
        first_goods_name = data[0]["goodsName"]
        return first_goods_name
    return ("数据错误")

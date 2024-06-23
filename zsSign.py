import requests, time

# 战双签到 (roleId, userId 来自表单)
def zhansuangSignin(token, devCode, roleId, userId):
    urlsignin = "https://api.kurobbs.com/encourage/signIn/v2"
    headers = {
        "token": token,
        "devCode": devCode,
        "User-Agent": "Kuro/2.2.0 KuroGameBox/2.2.0",
        "source": "android"
    }
    datasign = {
        "gameId": "2",
        "serverId": "1000",
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
        goods_names = getzhansuangSignprize(token, devCode, roleId, userId)
        return goods_names
    except ValueError as e:
        print(f"获取奖品失败: {e}")
        return None

# 战双物品 (roleId, userId 来自表单)
def getzhansuangSignprize(token, devCode, roleId, userId):
    urlqueryRecord = "https://api.kurobbs.com/encourage/signIn/queryRecordV2"
    headers = {
        "token": token,
        "devCode": devCode,
        "User-Agent": "Kuro/2.2.0 KuroGameBox/2.2.0",
        "source": "android"
    }
    data = {
        "gameId": "2",
        "serverId": "1000",
        "roleId": roleId,
        "userId": userId,
        "reqMonth": time.strftime("%m")
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

from log import mclog, mc_message
import requests, json, datetime, os, sys, re, time

token = os.getenv('COOKIE')

# 获取鸣潮表单
def mingchaoTable(token):
    url = "http://api.kurobbs.com/gamer/widget/game3/getData"
    headers = {
        "source": "android",
        "Cookie": f"user_token={token}",
        "token": token
    }
    data = {
        "type": "1",
        "sizeType": "2"
    }
    response = requests.post(url, headers=headers, data=data)
    return response.text

# 获取鸣潮终端
def mingchaoIndex(token, roleId, userId):
    url = "http://api.kurobbs.com/gamer/roleBox/aki/exploreIndex"
    headers = {
        "token": token,
        "devCode": "Kuro/2.2.0 KuroGameBox/2.2.0",
        "User-Agent": "Kuro/2.2.0 KuroGameBox/2.2.0",
        "source": "android"
    }
    data = {
        "gameId": "3",
        "serverId": "76402e5b20be2c39f095a152090afddc",
        "roleId": roleId,
        "userId": userId,
        "channelId":"19",
        "countryCode":"1"
    }
    response = requests.post(url, headers=headers, data=data)
    return response.text

# 鸣潮物品 (roleId, userId 来自表单)
def getmingchaoSignprize(token, roleId, userId):
    urlqueryRecord = "https://api.kurobbs.com/encourage/signIn/queryRecordV2"
    headers = {
        "token": token,
        "devCode": "Kuro/2.2.0 KuroGameBox/2.2.0",
        "User-Agent": "Kuro/2.2.0 KuroGameBox/2.2.0",
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

# 鸣潮签到 (roleId, userId 来自表单)
def mingchaoSignin(token, roleId, userId, month):
    urlsignin = "https://api.kurobbs.com/encourage/signIn/v2"
    headers = {
        "token": token,
        "devCode": "Kuro/2.2.0 KuroGameBox/2.2.0",
        "User-Agent": "Kuro/2.2.0 KuroGameBox/2.2.0",
        "source": "android"
    }
    datasign = {
        "gameId": "3",
        "serverId": "76402e5b20be2c39f095a152090afddc",
        "roleId": roleId,
        "userId": userId,
        "reqMonth": month
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

# 鸣潮终端写出
def mingchaoIndexWrite(token, roleId, userId):
    data = json.loads(str(mingchaoIndex(token, roleId, userId)))
    areaInfoList = data['data']['areaInfoList']
    countryName = data['data']['countryName']
    countryProgress = data['data']['countryProgress']
    mc_message('地区　　：'+countryName)
    mc_message('收集度　：'+countryProgress+'%')
    mc_message("-"*60)
    for i in range(len(areaInfoList)-1):
        areaName = areaInfoList[i]['areaName']
        if len(str(areaName)) <= 4:
            areaName = areaName + '　' * (4-len(str(areaName)))
        areaProgress = areaInfoList[i]['areaProgress']
        mc_message(areaName+' · ['+' '*(3-len(str(areaProgress)))+str(areaProgress)+'%'+' '+'█'*int(areaProgress/4)+'═'*(25-int(areaProgress/4))+']')
        itemList = areaInfoList[i]['itemList']
        for t in range(len(itemList)-1):
            itemName = itemList[t]['name']
            itemNames = itemName+'　'*(int(3-len(itemName)))
            if len(str(itemName)) == 2:
                itemName = re.sub(r'^(.)', r'\1　', itemName)
            itemProgress = itemList[t]['progress']
            itemPercentage = ' '*(3-len(str(itemProgress)))+str(itemProgress)+'%'
            itemBar = '|'+'█'*int(itemProgress/4)+'═'*(25-int(itemProgress/4))+'|'

            mc_message(' ---  '+itemName+itemBar+itemPercentage)
        mc_message("-"*60)

# 鸣潮表单写出
def mingchaoWrite():
    # 基本
    mc_message("-"*60)
    mc_message('游戏：'+mc.serverName)
    mc_message('昵称：'+mc.roleName+' · 特征码：'+str(mc.roleId))
    mc_message('时间：'+str(mc.serverTime))
    mc_message('状态：'+mc.signInTxt)
    mc_message("-"*60)

    dataTableName = [mc.energyData['name'], mc.livenessData['name']+'　', mc.battlePassData[0]['name'], mc.battlePassData[1]['name']]
    dataTableNum = [mc.energyData['cur'], mc.livenessData['cur'], mc.battlePassData[0]['cur'], mc.battlePassData[1]['cur']]
    dataTableMax = [240, 100, 70, 10000]
    for i in range(len(dataTableName)):
        name = dataTableName[i]
        mathCount = dataTableMax[i]/20
        progress = str(dataTableNum[i])+'/'+str(dataTableMax[i])
        progress = ' '*(int(11-len(progress)))+progress
        bar = '█'*(int(dataTableNum[i]/mathCount))+'═'*(int(dataTableMax[i]/mathCount)-int(dataTableNum[i]/mathCount))
        mc_message(name+'：['+bar+progress+']')
    mc_message('（备注：活跃度数据有延迟。）')
    mc_message("-"*60)

class mingchaoTableCode:
    data = json.loads(str(mingchaoTable(token)))

    userId = data['data']['userId']
    roleId = data['data']['roleId']
    roleName = data['data']['roleName']

    serverName = data['data']['serverName']
    serverTime = datetime.datetime.fromtimestamp(data['data']['serverTime'])
    month = serverTime.strftime('%m')

    signInTxt = data['data']['signInTxt']

    energyData = data['data']['energyData']
    livenessData = data['data']['livenessData']
    battlePassData = data['data']['battlePassData']

mc = mingchaoTableCode()

mingchaoWrite()
mingchaoIndexWrite(token, mc.roleId, mc.userId)

# 触发签到
if mc.signInTxt != '已完成签到':
    mingchaoSignin(token, mc.roleId, mc.userId, mc.month)

with open(mclog, 'r') as CONTENT:
    wemessage(WEAPI, CONTENT)

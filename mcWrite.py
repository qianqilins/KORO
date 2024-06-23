import requests, json, re
from log import mc_message

LWide = 4

# 获取鸣潮区域终端
def mcIndex(token, roleId, userId):
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

# 获取鸣潮基本资料
def mcBaseData(token, roleId, userId):
    url = "http://api.kurobbs.com/gamer/roleBox/aki/baseData"
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

# 获取鸣潮角色资料
def mcRoleData(token, roleId, userId):
    url = "http://api.kurobbs.com/gamer/roleBox/aki/roleData"
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

# 鸣潮基本资料写出
def mcBaseWrite(token, roleId, userId):
    data = json.loads(str(mcBaseData(token, roleId, userId)))

    activeDays = data['data']['activeDays']
    level = data['data']['level']
    worldLevel = data['data']['worldLevel']
    achievementCount = data['data']['achievementCount']

    roleNum = data['data']['roleNum']
    soundBox = data['data']['soundBox']
    bigCount = data['data']['bigCount']
    smallCount = data['data']['smallCount']

    boxList = data['data']['boxList']

    mc_message("-"*50)

    mc_message('游戏天数 '+str(activeDays)+' 联觉等级 '+str(level)+' 索拉等级 '+str(worldLevel)+' 达成成就 '+str(achievementCount))
    mc_message('解锁角色 '+str(roleNum)+' 背包声匣 '+str(soundBox)+' 中型信标 '+str(bigCount)+' 小型信标 '+str(smallCount))
    boxAllContent = ''
    boxContent = ''
    for i in range(len(boxList)):
        boxName = boxList[i]['boxName']
        boxName = boxName.replace('奇藏箱','奇藏')
        boxNum = boxList[i]['num']
        boxContent = boxName+' '+str(boxNum)+' '
        boxAllContent += boxContent
    mc_message(boxAllContent.rstrip())
    mc_message("-"*50)

# 鸣潮区域终端写出
def mcIndexWrite(token, roleId, userId):
    data = json.loads(str(mcIndex(token, roleId, userId)))
    areaInfoList = data['data']['areaInfoList']
    countryName = data['data']['countryName']
    countryProgress = data['data']['countryProgress']
    mc_message('地区：'+countryName+' · 收集度：'+countryProgress+'%')
    mc_message("-"*50)
    for i in range(len(areaInfoList)-1):
        areaName = areaInfoList[i]['areaName']
        if len(str(areaName)) <= 4:
            areaName = areaName + '　' * (4-len(str(areaName)))
        areaProgress = areaInfoList[i]['areaProgress']
        mc_message(areaName+' · ['+' '*(3-len(str(areaProgress)))+str(areaProgress)+'%'+' '+'█'*int(areaProgress/LWide)+'═'*(int(100/LWide)-int(areaProgress/LWide))+']')
        itemList = areaInfoList[i]['itemList']
        for t in range(len(itemList)-1):
            itemName = itemList[t]['name']
            itemNames = itemName+'　'*(int(3-len(itemName)))
            if len(str(itemName)) == 2:
                itemName = re.sub(r'^(.)', r'\1　', itemName)
            itemProgress = itemList[t]['progress']
            itemPercentage = ' '*(3-len(str(itemProgress)))+str(itemProgress)+'%'
            itemBar = '|'+'█'*int(itemProgress/LWide)+'═'*(int(100/LWide)-int(itemProgress/LWide))+'|'

            mc_message(' > 　　'+itemName+itemBar+itemPercentage)
        mc_message("-"*50)




# 鸣潮服务终端写出
def mcServerWrite(roleId, roleName, serverName, serverTime, signInTxt, energyData, livenessData, battlePassData):
    mc_message("-"*50)
    mc_message('游戏：'+serverName)
    mc_message('昵称：'+roleName+' · 特征码：'+str(roleId))
    mc_message('时间：'+str(serverTime))
    mc_message('状态：'+signInTxt)
    mc_message("-"*50)

    dataTableName = [energyData['name'], livenessData['name']+'　', battlePassData[0]['name'], battlePassData[1]['name']]
    dataTableNum = [energyData['cur'], livenessData['cur'], battlePassData[0]['cur'], battlePassData[1]['cur']]
    dataTableMax = [240, 100, 70, 10000]
    for i in range(len(dataTableName)):
        name = dataTableName[i]
        mathCount = dataTableMax[i]/(100/LWide)
        progress = str(dataTableNum[i])+'/'+str(dataTableMax[i])
        bar = '█'*(int(dataTableNum[i]/mathCount))+'═'*(int(dataTableMax[i]/mathCount)-int(dataTableNum[i]/mathCount))
        mc_message(name+'：['+bar+']'+progress)
    mc_message("-"*50)
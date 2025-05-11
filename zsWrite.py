import requests, json, re, datetime
from log import zs_message
LWide = 20

# 角色简介
def zsroleList(token, roleId):
    url = "http://api.kurobbs.com/gamer/roleBox/roleList"
    headers = {
    "source": "android",
    "devCode": "Kuro/2.4.4 KuroGameBox/2.4.4",
    "User-Agent": "Kuro/2.4.4 KuroGameBox/2.4.4",
            "token": token
    }
    data = {
    "gameId": "2",
    "roleId": roleId,
    "serverId": "1000"
    }
    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    return response.text

def zscharInfo(token, roleId, charId):
    url = "http://api.kurobbs.com/gamer/roleBox/characterInfo"
    headers = {
    "source": "android",
    "devCode": "Kuro/2.4.4 KuroGameBox/2.4.4",
    "User-Agent": "Kuro/2.4.4 KuroGameBox/2.4.4",
    "token": token
    }
    data = {
    "gameId": "2",
    "roleId": roleId,
    "serverId": "1000",
    "characterId": charId
    }
    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    return response.text

# 资源月报
def zsMonth(token, roleId):
    url = "http://api.kurobbs.com/gamer/resource/month"
    headers = {
        "Host": "api.kurobbs.com",
        "source": "android",
        "User-Agent": "Kuro/2.4.4 KuroGameBox/2.4.4",
        "token": token
        }
    data = {
      "roleId": roleId
        }
    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    return response.text

def zsWrite(gameName, roleName, roleId, serverTime, signInTxt, actionData, dormData, activeData):
    # 基本
    zs_message("-"*50)
    zs_message('游戏：'+gameName)
    # zs_message('昵称：'+roleName+' · 编号：'+str(roleId))
    zs_message('时间：'+str(serverTime))
    zs_message('状态：'+signInTxt)
    zs_message("-"*50)

    dataTableName = [actionData['name'], dormData['name'], activeData['key']]
    dataTableNum = [actionData['cur'], dormData['cur'], activeData['cur']]
    dataTableMax = [actionData['total'], dormData['total'], activeData['total']]

    for i in range(len(dataTableName)):
        name = dataTableName[i]
        if name == '血清':
            name = '血　　清'
        mathCount = dataTableMax[i]/LWide
        progress = str(dataTableNum[i])+'/'+str(dataTableMax[i])
        if dataTableNum[i] > dataTableMax[i]:
            dataTableNum[i] = dataTableMax[i]
        bar = '█'*(int(dataTableNum[i]/mathCount))+'═'*(int(dataTableMax[i]/mathCount)-int(dataTableNum[i]/mathCount))
        zs_message(name+'：['+bar+']'+progress)
    zs_message("-"*50)

def zsBossWrite(bossData):
    for i in range(len(bossData)):
        bossName = bossData[i]['name']
        bossGoods = bossData[i]['key']
        bossTimes = bossData[i].get('expireTimeStamp')
        if bossTimes == None:
            bossTimes = bossData[i].get('refreshTimeStamp')
        bossValue = bossData[i]['value']
        bossCur = bossData[i]['cur']
        bossTotal = bossData[i]['total']
        if bossTotal == 0:
            bossTotal = 100
        mathCount = bossTotal/LWide

        bossBar = '█'*(int(bossCur/mathCount))+'═'*(int(bossTotal/mathCount)-int(bossCur/mathCount))
        content = bossName+'('+bossGoods+')|'+bossBar+'|'+bossValue
        zs_message(content.rstrip())
        if bossTimes != None:
            zs_message(" >>> 刷新时间："+str(datetime.datetime.fromtimestamp(bossTimes)))
    zs_message("-"*50)

def zsMonthWrite(token, roleId):
    data = json.loads(str(zsMonth(token, roleId)))
    gameLevel = data['data']['gameLevel']

    currentBlackCard = data['data']['currentBlackCard']
    currentDevelopResource = data['data']['currentDevelopResource']
    currentTradeCredit = data['data']['currentTradeCredit']

    currentMonth = data['data']['currentMonth']
    monthBlackCard = data['data']['monthBlackCard']
    monthDevelopResource = data['data']['monthDevelopResource']
    monthTradeCredit = data['data']['monthTradeCredit']
    zs_message('游戏等级：'+str(gameLevel))
    zs_message("-"*50)
    zs_message('当前资源：')
    zs_message(' > 黑　　卡 - '+str(currentBlackCard))
    zs_message(' > 研发资源 - '+str(currentDevelopResource))
    zs_message(' > 贸易凭据 - '+str(currentTradeCredit))
    zs_message("-"*50)
    zs_message(str(currentMonth)+'月资源情况：')
    zs_message(' > 黑　　卡 - '+str(monthBlackCard))
    zs_message(' > 研发资源 - '+str(monthDevelopResource))
    zs_message(' > 贸易凭据 - '+str(monthTradeCredit))
    zs_message("-"*50)

def zsCharWrite(token, roleId):
    data = json.loads(zsroleList(token, roleId))
    dataAll = data['data']['all']
    for i in range(len(dataAll)):
        characterId = dataAll[i]['characterId']
        charaData = json.loads(zscharInfo(token, roleId, characterId))
        versionName = charaData['data']['versionName']
        characterCareer = charaData['data']['characterCareer']
        characterName = dataAll[i]['characterName']
        targetQyNew = dataAll[i]['targetQyNew']
        fb = dataAll[i]['fb']
        lv = dataAll[i]['lv']
        attributeName = dataAll[i]['attributeName']
        # zs_message(' * ID:'+str(characterId)+' NAME:'+characterName+'·'+versionName)
        zs_message(f' ===== {str(characterId)} {characterName}·{versionName} =====')
        zs_message(' * TARGET: '+targetQyNew+'  LV: '+str(lv)+'  FB: '+str(fb))
        zs_message(' * ATTRIBUTE: '+attributeName+'  CAREER: '+characterCareer+'\n')
    zs_message("-"*50)

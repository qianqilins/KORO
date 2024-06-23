import requests, json, re
import datetime
from log import zs_message

LWide = 20

def zhansuangWrite(gameName, roleName, roleId, serverTime, signInTxt, actionData, dormData, activeData):
    # 基本
    zs_message("-"*50)
    zs_message('游戏：'+gameName)
    zs_message('昵称：'+roleName+' · 编号：'+str(roleId))
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

def zhansuangBossWrite(bossData):
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



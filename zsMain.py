import requests
import datetime
import json, os
from key import token, devCode
from log import zs_log, logclean
from zsUtil import zhansuangRefresh
from zsSign import zhansuangSignin
from zsWrite import zhansuangWrite, zhansuangBossWrite

class zhansuangTableCode:
    data = json.loads(str(zhansuangRefresh(token, devCode)))

    gameId = data['data']['gameId']
    if gameId == 2:
    	gameName = '战双帕弥什'

    userId = data['data']['userId']
    roleId = data['data']['roleId']
    roleName = data['data']['roleName']

    serverName = data['data']['serverName']
    serverTime = datetime.datetime.fromtimestamp(data['data']['serverTime'])

    signInTxt = data['data']['signInTxt']

    actionData = data['data']['actionData']
    dormData = data['data']['dormData']
    activeData = data['data']['activeData']

    bossData = data['data']['bossData']

zs = zhansuangTableCode()

# if zs.signInTxt != '已领取每日补给':
#     print('获得补给：'+zhansuangSignin(token, devCode, zs.roleId, zs.userId))
print('获得补给：'+zhansuangSignin(token, devCode, zs.roleId, zs.userId))

zhansuangWrite(zs.gameName, zs.roleName, zs.roleId, zs.serverTime, zs.signInTxt, zs.actionData, zs.dormData, zs.activeData)
zhansuangBossWrite(zs.bossData)

logclean('zs_',zs_log)

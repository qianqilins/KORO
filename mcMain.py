import requests
import datetime
import json, os
from key import token
from log import mc_log, logclean
from mcUtil import mingchaoRefresh
from mcSign import mingchaoSignin
from mcWrite import mcServerWrite, mcBaseWrite, mcIndexWrite

class mingchaoTableCode:
    data = json.loads(str(mingchaoRefresh(token)))

    userId = data['data']['userId']
    roleId = data['data']['roleId']
    roleName = data['data']['roleName']
    serverName = data['data']['serverName']
    serverTime = datetime.datetime.fromtimestamp(data['data']['serverTime'])

    signInTxt = data['data']['signInTxt']

    energyData = data['data']['energyData']
    livenessData = data['data']['livenessData']
    battlePassData = data['data']['battlePassData']

mc = mingchaoTableCode()

# ==============================================================================

mcServerWrite(mc.roleId,mc.roleName,mc.serverName,mc.serverTime,mc.signInTxt,mc.energyData,mc.livenessData,mc.battlePassData)
mcBaseWrite(token, mc.roleId, mc.userId)
mcIndexWrite(token, mc.roleId, mc.userId)

# mingchaoWrite(mc.serverName, mc.roleName, mc.roleId, mc.serverTime, mc.signInTxt, mc.energyData, mc.livenessData, mc.battlePassData)
# mingchaoIndexWrite(token, mc.roleId, mc.userId)

# if mc.signInTxt != '已完成签到':
#     print('获得补给：'+mingchaoSignin(token, mc.roleId, mc.userId))

print('获得补给：'+mingchaoSignin(token, mc.roleId, mc.userId))

logclean('mc_',mc_log)

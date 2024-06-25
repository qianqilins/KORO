import httpx, re

gachaUrl = "https://aki-gm-resources.aki-game.com/aki/gacha/index.html#/record?svr_id=76402e5b20be2c39f095a152090afddc&player_id=109170226&lang=zh-Hans&gacha_id=100002&gacha_type=1&svr_area=cn&record_id=d4fac8bac4686712eedd58d2a97a64db&resources_id=89e301f1dfcbd79ea04fb10bde2469e4"

def mcGacha(playerId, recordId):
	with httpx.Client() as client:
		url = "https://gmserver-api.aki-game2.com/gacha/record/query"
		request = {
		  "cardPoolType": "1",
		  "languageCode": "zh-Hans",
		  "playerId": playerId,
		  "recordId": recordId,
		  "cardPoolId": "89e301f1dfcbd79ea04fb10bde2469e4",
		  "serverId": "76402e5b20be2c39f095a152090afddc",
			}
		respose = client.post(url=url, json=request, timeout=90)
		# print(respose.text)

def mcUrlInfo(url):
	playerId = re.search(r'player_id=([^&]+)', url).group(1)
	recordId = re.search(r'record_id=([^&]+)', url).group(1)
	resourcesId = re.search(r'resources_id=([^&]+)', url).group(1)
	return playerId, recordId

mcUrlInfo = mcUrlInfo(gachaUrl)
mcGacha(mcUrlInfo[0],mcUrlInfo[1])

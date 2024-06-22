import requests

WEAPI = os.getenv('WEAPI')

def wemessage(WEAPI, CONTENT)
    url = f"https://api.anpush.com/push/{WEAPI}"
    payload = {
        "title": "鸣潮",
        "channel": "微信通知",
        "content": CONTENT
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    response = requests.post(url, headers=headers, data=payload)

import requests

def wemessage(WEAPI, WEUSERID, CONTENT):
    url = f"https://api.anpush.com/push/{WEAPI}"
    payload = {
        "title": "鸣潮",
        "channel": "01100",
        "to": WEUSERID,
        "content": CONTENT
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    response = requests.post(url, headers=headers, data=payload)
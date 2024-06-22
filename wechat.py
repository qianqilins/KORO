import requests

WEAPI = os.getenv('WEAPI')

def wemessage(WEAPI)
url = f"https://api.anpush.com/push/{WEAPI}"
payload = {
    "title": "鸣潮",
    "content": "your_content",
    "channel": "微信通知"
}
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}
response = requests.post(url, headers=headers, data=payload)

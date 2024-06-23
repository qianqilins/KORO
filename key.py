import os

token = os.getenv('COOKIE')
devCode = os.getenv('devCode')
WEAPI = os.getenv('WEAPI')
WEUSERID = os.getenv('WEUSERID')

if token == None:
	token = ''
if devCode == None:
	devCode = ''
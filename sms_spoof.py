#sms_spoof
import requests

CON_CODE = input("ENTER THE COUNTRY CODE WITHOUT + ----> ")
MOB_NO = input("ENTER THE MOBILE NUMBER WIHOIT COUNTRY CODE ----> ")
RECIEVER = '+' + CON_CODE + MOB_NO
MESSAGE = input("ENTER THE MESSAGE -----> ")
resp = requests.post('https://textbelt.com/text', {
  'phone': RECIEVER,
  'message': MESSAGE,
  'key': 'textbelt',
})
print(resp.json())
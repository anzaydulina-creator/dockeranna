import time
import requests

print('')
time.sleep(10)

print('')

while True:
    otvet = requests.get('http://web:8098/')
    server_text = otvet.text
    print('')
    time.sleep(5)

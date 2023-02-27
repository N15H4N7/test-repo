import os
import requests

r = requests.get("https://youtube.com/")
print(r)
print(r.ok)
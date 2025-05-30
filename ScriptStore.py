#Script Store

import requests
r=requests.get("https://automatetheboringstuff.com/files/rj.txt")

with open("RomeoAndJuliet.txt","wb") as f:
    for chunk in r.iter_content(100000):
        f.write(chunk)


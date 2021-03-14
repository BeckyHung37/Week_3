#week_3 Q1
#網路連線
import urllib.request as request #request是簡化的名稱
import json #載入json模組
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json"
with request.urlopen(src) as response:
    data=json.load(response) #利用json模組處理json資料格式
    #data=response.read("utf-8") #讀取純網站，取得原始碼
#整理資料
#將景點名稱列表出來
landscape_list=data["result"]["results"]
with open("data.txt", "w" , encoding="utf-8") as file: #因為資料有中文，用UTF-8編碼
    for landscape in landscape_list: #for迴圈必須在with裡面運作
        img = landscape["file"]
        img_list = img.split("http")
        first_img_path = "http" + img_list[1]

        file.write(landscape["stitle"]+","+landscape["longitude"]+
            ","+landscape["latitude"]+","+first_img_path+"\n")
        
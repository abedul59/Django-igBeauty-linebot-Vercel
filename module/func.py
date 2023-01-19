from django.conf import settings

import os

def sendImageA(event):  #傳送圖片
    import  json, ssl, urllib.request

    url = 'https://igbeauty-restful.onrender.com/api/images/random/'
    context = ssl._create_unverified_context()

    with urllib.request.urlopen(url, context=context) as jsondata:
    #將JSON進行UTF-8的BOM解碼，並把解碼後的資料載入JSON陣列中
        data = json.loads(jsondata.read().decode('utf-8-sig')) 


    print(data['id'])
    print(data['Url'])



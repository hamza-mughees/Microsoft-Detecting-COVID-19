
import requests
url = "http://20.50.145.15:80/api/v1/service/classification-model/score"
content_type = 'image/jpeg'
headers = {'content-type': content_type}

img= open('path', 'rb').read() #*edit here: change to path to your image


r = requests.post(url, data=img, headers=headers)

print(r.text)



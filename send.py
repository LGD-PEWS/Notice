import requests
from variable import title1, token1


def send_notice(content):
    token = token1
    title = title1
    url = f"http://www.pushplus.plus/send?token={token}&title={title}&content={content}&template=html"
    response = requests.request("GET", url)
    print(response.text)

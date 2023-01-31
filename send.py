import requests
from variable import title1


def send_notice(content):
    token = "5cc97d72996d42e9a884c69167fa6310"
    title = title1
    url = f"http://www.pushplus.plus/send?token={token}&title={title}&content={content}&template=html"
    response = requests.request("GET", url)
    print(response.text)

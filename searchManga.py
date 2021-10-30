import json
from requests_html import HTMLSession

url = "https://mangalivre.net/lib/search/series.json"
s = HTMLSession()

payload = "search=one punch"
headers = {
    "authority": "mangalivre.net",
    "sec-ch-ua": "\"Google Chrome\";v=\"95\", \"Chromium\";v=\"95\", \";Not A Brand\";v=\"99\"",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "x-requested-with": "XMLHttpRequest",
    "sec-ch-ua-mobile": "?0",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
    "sec-ch-ua-platform": "\"Windows\"",
    "origin": "https://mangalivre.net",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://mangalivre.net/",
    "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "cookie": "_ga=GA1.2.458525192.1634521647; _gid=GA1.2.189787841.1635001700; mZ_rem=bad2346d95b445e22068a4882eca2459d1ad98a2f3989695c08f8f0677e8d8ec%2C%C0%B88%A1%DE%0E%BA%EA%AA%F4byOZ%1E%EA+%D0%92%89%09%3Da%E6%3C%EC%DE%88%1Cw%81y4%04H%CCV%AF%01%29%CF%97%7Dj%B6%CC%09%CB%5De%5E%C8%D3%E95%CE%16o%60%28%2B%F1%7B; __cf_bm=iVl_rKxNtTey.nKqpzT9YstPMlYUHnl0j2EjGcwgCUI-1635561253-0-AT1NJrbe0uv2Z2hmIQ7F19LOflkQYM7qxwMA3XGQxpdnZmnE1BrLJcbTgT1Gk1Gx+FOWN1eJMJ+OZVuFTfuCkk4qLjq7cBX8vZZRD6QxNtUKf0MnrZk1WbRn2bRM+TCHag==; mZ_sess=346338656230386563326463346164656338613630376566303538346439323661356533386334336661303635393335316136646239373930303164666635322b318fa166290d98133da1321bff96c9898e6c9ce4bad6e3ae31f8c1dfc87b5f56ce045159371d95b5bbe2ad6d2c973fd16672d274fbaab0896e13902730b3fe"
}

response = s.post(url, data=payload, headers=headers).text
search_response_json = json.loads(response)

for item in search_response_json["series"]:
    print(item["id_serie"], item["name"], item["author"], item["artist"], item["score"])

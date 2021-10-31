import json
from requests_html import HTMLSession


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
    }

def searchMangaByName(manga_name):

    url = "https://mangalivre.net/lib/search/series.json"
    payload = f"search={manga_name}"
    s = HTMLSession()

    response = s.post(url, data=payload, headers=headers).text
    search_response_json = json.loads(response)

    for item in search_response_json["series"]:
        info_manga = {
                    "id_serie": item["id_serie"],
                    "name": item["name"],
                    "score": item["score"],
                    "author": item["author"],
                    "artist": item["artist"],
                    "cover": item["cover"],
                    "link": item["link"],
                    "categories": [],
                }
        listaCat = [cat["name"] for cat in item["categories"]] #  item["categories"][i]["name"]
        print(listaCat)

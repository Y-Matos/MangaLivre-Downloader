import json
from requests.models import ReadTimeoutError
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

def searchMangaByName(manga_name,  exact_match=False):
    results = []

    url = "https://mangalivre.net/lib/search/series.json"
    payload = f"search={manga_name}"
    s = HTMLSession()

    response = s.post(url, data=payload, headers=headers).text
    search_response_json = json.loads(response)

    try:
        for item in search_response_json["series"]:        
            info_manga = {
                        "manga_id": item["id_serie"],
                        "name": item["name"],
                        "score": item["score"],
                        "author": item["author"],
                        "artist": item["artist"],
                        "cover": item["cover"],
                        "manga_url": item["link"],
                        "categories": [cat["name"] for cat in item["categories"]],
                    }
            if not exact_match:
                results.append(info_manga)
            elif item["name"].lower().strip() == manga_name.lower().strip():
                results.append(info_manga)
                return json.dumps(results[0],ensure_ascii= False, indent=4)
    except TypeError as tp:
        if exact_match:
            print(f"Nenhuma correspondência exata encontrada.")
        else:
            print(f"Nenhum resultado foi encontrado para a busca.")
        return

    return json.dumps(results,ensure_ascii= False, indent=4)

def get_manga_id_by_name(manga_name):
    try:
        manga = json.loads(searchMangaByName(manga_name, exact_match=True))
        return(manga["manga_id"])
    except TypeError:
        return None

    
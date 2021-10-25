from requests.models import Response
from requests.sessions import session
from requests_html import HTMLSession
import requests_html

headers= {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}

def getPageHTML(url):
    session = HTMLSession()
    response = session.get(url, headers=headers)

    while response.status_code == 103:
        response = session.get(url, headers=headers)
        
    return response

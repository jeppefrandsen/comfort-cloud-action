import pytz
import requests
from datetime import datetime

PRICE_API_URL = "https://www.billigkwh.dk/api/Priser/HentPriser"


def price(area_dk: str, net_company: str, electricity_company: str) -> float | None:
    now = datetime.now(pytz.timezone("Europe/Copenhagen"))
    hour = int(datetime.strftime(now, "%H"))
    params = {'sted': area_dk, 'netselskab': net_company, 'produkt': electricity_company}
    headers = {'User-Agent': 'UserAgent/1.0'}

    response = requests.get(url=PRICE_API_URL, params=params, headers=headers).json()
    if response:
        prices = response[0].get('priser', [])
        if prices:
            return float(prices[hour])
    return None

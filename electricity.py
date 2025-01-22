"""Electricity price module"""

from datetime import datetime
import pytz
import requests

ELECTRICITY_PRICE_URL = "https://www.billigkwh.dk/api/Priser/HentPriser"


def get_price(area: str, network_company: str, company: str) -> float | None:
    """Get electricity price"""
    params = {'sted': area, 'netselskab': network_company, 'produkt': company}
    headers = {'User-Agent': 'UserAgent/1.0'}

    response = requests.get(url=ELECTRICITY_PRICE_URL, params=params, headers=headers).json()
    if response:
        prices = response[0].get('priser', [])
        if prices:
            now = datetime.now(pytz.timezone("Europe/Copenhagen"))
            hour = int(datetime.strftime(now, "%H"))
            return float(prices[hour])
    return None

"""Panasonic Comfort Cloud module"""

import os
import pcomfortcloud
import electricity

AREA = os.getenv('COMFORT_CLOUD_AREA')
PRICE_MAX = float(os.getenv('COMFORT_CLOUD_PRICE_MAX'))
NETWORK_COMPANY = os.getenv('COMFORT_CLOUD_NETWORK_COMPANY')
ELECTRICITY_COMPANY = os.getenv('COMFORT_CLOUD_ELECTRICITY_COMPANY')
TEMPERATURE_MIN = int(os.getenv('COMFORT_CLOUD_TEMPERATURE_MIN', "0"))
TEMPERATURE_MAX = int(os.getenv('COMFORT_CLOUD_TEMPERATURE_MAX', "25"))


def main():
    """Main function"""
    session = pcomfortcloud.Session(os.getenv('COMFORT_CLOUD_USERNAME'), os.getenv('COMFORT_CLOUD_PASSWORD'))
    session.login()
    client = pcomfortcloud.ApiClient(session)

    devices = client.get_devices()
    if not devices:
        raise RuntimeError("No devices found")

    device = client.get_device(devices[0]['id'])
    if not device:
        raise RuntimeError("Unable to get device parameters")

    power = device['parameters']['power']
    price = electricity.get_price(AREA, NETWORK_COMPANY, ELECTRICITY_COMPANY)
    if not price:
        raise RuntimeError("Unable to get electricity price")

    temp_inside = device['parameters']['temperatureInside']
    temp_outside = device['parameters']['temperatureOutside']
    print(f"Current price: {price}, temperature inside: {temp_inside}, temperature outside: {temp_outside}")

    if power == pcomfortcloud.constants.Power.On:
        if price > PRICE_MAX or temp_inside >= TEMPERATURE_MAX:
            print(f"Powering off {devices[0]['name']}")
            client.set_device(devices[0]['id'], power=pcomfortcloud.constants.Power.Off)
    elif power == pcomfortcloud.constants.Power.Off: 
        if price <= PRICE_MAX or temp_inside <= TEMPERATURE_MIN:
            print(f"Powering on {devices[0]['name']}")
            client.set_device(devices[0]['id'], power=pcomfortcloud.constants.Power.On)


if __name__ == "__main__":
    main()

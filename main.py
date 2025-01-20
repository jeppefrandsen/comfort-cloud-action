import os
import electricity
import pcomfortcloud

AREA = os.getenv('COMFORT_CLOUD_AREA')
PRICE_MAX = float(os.getenv('COMFORT_CLOUD_PRICE_MAX'))
NETWORK_COMPANY = os.getenv('COMFORT_CLOUD_NETWORK_COMPANY')
ELECTRICITY_COMPANY = os.getenv('COMFORT_CLOUD_ELECTRICITY_COMPANY')


def main():
    session = pcomfortcloud.Session(os.getenv('COMFORT_CLOUD_USERNAME'), os.getenv('COMFORT_CLOUD_PASSWORD'))
    session.login()
    client = pcomfortcloud.ApiClient(session)

    devices = client.get_devices()
    if devices:
        device = client.get_device(devices[0]['id'])
        if device:
            power = device['parameters']['power']
            price = electricity.price(AREA, NETWORK_COMPANY, ELECTRICITY_COMPANY)
            if price:
                print("Current price is {}".format(price))

                if power == pcomfortcloud.constants.Power.On and price > PRICE_MAX:
                    print("Powering off {}".format(devices[0]['name']))
                    session.set_device(devices[0]['id'], power=pcomfortcloud.constants.Power.Off)
                elif power == pcomfortcloud.constants.Power.Off and price <= PRICE_MAX:
                    print("Powering on {}".format(devices[0]['name']))
                    session.set_device(devices[0]['id'], power=pcomfortcloud.constants.Power.On)
            else:
                print("Unable to get electricity price")
        else:
            print("Unable to get device parameters")
    else:
        print("Unable to find device")


if __name__ == "__main__":
    main()

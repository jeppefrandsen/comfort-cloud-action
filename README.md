# comfort-cloud-action

![GitHub release](https://img.shields.io/github/v/release/jeppefrandsen/comfort-cloud-action) ![GitHub](https://img.shields.io/github/license/jeppefrandsen/comfort-cloud-action)

GitHub Actions for controlling a [Panasonic Comfort Cloud](https://www.aircon.panasonic.eu) enabled heatpump based on electricity price.

## Benefits

Using GitHub Actions to control your heatpump has be benefit of not requiring yet another device to control your already Wi-Fi enabled heatpump like [Homey](https://homey.app) and [Home Assistant](https://www.home-assistant.io) and hereby requiring even more electricity :earth_africa:. It is furthermore totally FREE since all GitHub users gets 2000 Actions minutes per month, so no monthly subscriptions and buying of dedicated devices for this purpose.

## Usage

Below is an example of checking the eletricity price for the specified electricity area, network and company every hour and control the heatpump based on the given max price. If you want to disable the control the workflow can be disabled under the "Actions" tab by selecting "Disable workflow".


```yml
name: run

on:
  schedule:
    - cron: 0 * * * *

jobs:
  comfort-cloud:
    runs-on: ubuntu-latest
    steps:  
    - name: Check price and control Panasonic Comfort Cloud
      uses: jeppefrandsen/comfort-cloud-action@v1
      with:
        username: ${{ secrets.COMFORT_CLOUD_USERNAME }}
        password: ${{ secrets.COMFORT_CLOUD_PASSWORD }}
        area: DK1
        network-company: n1_c
        company: nettopower
        price-max: 3.0
```

## Roadmap

Below are some of the identified roadmap items. Let me know if you think something is missing. Pull requests are more than welcome :pray:

- [ ] Add support for miminum temperature (force turn on if temperature is below limit)
- [ ] Add more intelligent control (increase temperature or be more powerful when cheaper than a certain level)

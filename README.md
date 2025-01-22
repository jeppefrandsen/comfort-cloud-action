# comfort-cloud-action

![GitHub release](https://img.shields.io/github/v/release/jeppefrandsen/comfort-cloud-action)

GitHub Actions for controlling a [Panasonic Comfort Cloud](https://www.aircon.panasonic.eu) enabled heatpump based on electricity price.

## Benefits

Using GitHub Actions to control your heatpump has be benefit of not requiring yet another device to control your already Wi-Fi enabled heatpump like [Homey](https://homey.app) and [Home Assistant](https://www.home-assistant.io) and hereby requiring even more electricity. It is furthermore totally **FREE** since all GitHub users gets 2000 Actions minutes per month for free, so no monthly subscriptions and buying of dedicated devices for this purpose.

The idea is also that the main control is still the Panasonic Comfort Cloud App and optimizing cost is just something done in the background. This is why this GitHub Actions is not adjusting temperature, air flow etc. but just controlling the power.

## Usage

Below is an example of checking the eletricity price for the specified electricity area, network and company every hour and control the heatpump based on the given max price. If you want to disable the control the workflow can be disabled under the "Actions" tab by selecting "Disable workflow". I am using starring of my private repo including this action to enable and disable the control since it is easily done in the GitHub App.


```yml
name: run

on:
  schedule:
    - cron: 0 * * * *

jobs:
  comfort-cloud:
    runs-on: ubuntu-latest
    steps:  
    - name: Run
      uses: jeppefrandsen/comfort-cloud-action@v2
      with:
        username: ${{ secrets.COMFORT_CLOUD_USERNAME }}
        password: ${{ secrets.COMFORT_CLOUD_PASSWORD }}
        area: DK1
        network-company: n1_c
        electricity-company: nettopower
        price-max: 3.0
```

## Limitations

It currently only works in Denmark due to the electricity calculations but could be expanded to Norway and Sweden by using https://www.energidataservice.dk/tso-electricity/Elspotprices as the API instead.

## Ideas

Below are some of the identified ideas to be added. Let me know if you think something is missing. Pull requests are more than welcome :pray:

- [ ] Add more intelligent control (increase temperature or be more powerful when cheaper than a certain level)
- [ ] Optimize regulation to avoid letting the temperature adjust more than 1-2 degrees celcius to lower power usage
- [ ] Calculate daily cost (already possible to read out the usage from the heatpump)
- [ ] Optimise control based on outdoor temperature (cheaper to heat when warmer outside)

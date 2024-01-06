# comfort-cloud-action

![GitHub release](https://img.shields.io/github/v/release/jeppefrandsen/comfort-cloud-action) ![GitHub](https://img.shields.io/github/license/jeppefrandsen/comfort-cloud-action)

GitHub Actions for controlling a Panasonic Comfort Cloud enabled heatpump based on electricity price.

## Usage

Below is an example of checking the eletricity price for the specified electricity area, network and company every hour and control the heatpump based on the given max price. If you want to disable the control the workflow can be disabled under "Actions" by selecting "Disable workflow".


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

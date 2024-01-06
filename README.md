# comfort-cloud-action

![GitHub release](https://img.shields.io/github/v/release/jeppefrandsen/comfort-cloud-action) ![GitHub](https://img.shields.io/github/license/jeppefrandsen/comfort-cloud-action)

GitHub Actions for controlling a Panasonic Comfort Cloud enabled heatpump based on electricity price.

## Usage

```yml
name: comfort-cloud

on:
  schedule:
    - cron: 0 * * * *

jobs:
  run:
    runs-on: ubuntu-latest
    steps:  
    - name: Comfort Cloud
      uses: jeppefrandsen/comfort-cloud-action@v1
      with:
        username: ${{ secrets.COMFORT_CLOUD_USERNAME }}
        password: ${{ secrets.COMFORT_CLOUD_PASSWORD }}
        area: DK1
        network-company: n1_c
        company: nettopower
        price-max: 3.0
```

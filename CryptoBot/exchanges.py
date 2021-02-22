import requests
import datetime
import os

class Exchanges:

    def __init__(self):
        self.exchange_url = "https://rest.coinapi.io/v1/exchanges"
        self.header =  {
            'X-CoinAPI-Key': os.environ.get('X-CoinAPI-Key')
        }

    def exc_prices(self, api):
        exc_response = requests.get(self.exchange_url, headers=self.header)
        exc_json = exc_response.json()
        current_time = datetime.datetime.now()
        time_string = current_time.strftime("%m/%d/%Y %H:%M:%S")
        exc_string = f"CURRENT 24 HR EXCHANGE VOLUMES AS OF {time_string} CST\n"
        for i in range(3):
            exc_string += exc_json[i]['name']
            volume = "{:,}".format(exc_json[i]['volume_1day_usd'])
            exc_string += ": $" + volume + "\n"
        exc_string += "#BINANCE #KRAKEN #COINBASEPRO"
        api.update_status(status=exc_string)

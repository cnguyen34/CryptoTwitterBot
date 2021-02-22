import requests
import datetime
import os

class Assets:

    def __init__(self):
        self.url = "https://rest.coinapi.io/v1/assets/?filter_asset_id=BTC;ETH;XLM;DOGE;XTZ"
        self.header = {
            'X-CoinAPI-Key': os.environ.get('X-CoinAPI-Key')
        }
        self.starting_prices = self.beginning_prices()

    def beginning_prices(self):
        starting_prices = []
        response = requests.get(self.url, headers=self.header)
        json = response.json()
        for i in range(5):
            price = float(json[i]['price_usd'])
            price = round(price, 4)
            starting_prices.append(price)
        return starting_prices

    def print_beginning_prices(self, api):
        starting_prices = []
        response = requests.get(self.url, headers=self.header)
        json = response.json()
        current_time = datetime.datetime.now()
        time_string = current_time.strftime("%m/%d/%Y %H:%M:%S")
        beginning_string = f"OPEN PRICES AS OF {time_string} CST \n"
        for i in range(5):
            price = float(json[i]['price_usd'])
            price = round(price, 4)
            starting_prices.append(price)
            beginning_string += json[i]['name']
            beginning_string += ": $" + str(price) + "\n"
        beginning_string += "#BTC #DOGE #ETH #XLM #XTZ"
        api.update_status(status=beginning_string)



    def curr_prices(self, api):
        starting_prices = self.starting_prices
        response = requests.get(self.url, headers=self.header)
        json = response.json()
        current_time = datetime.datetime.now()
        time_string = current_time.strftime("%m/%d/%Y %H:%M:%S")
        string = f"CURRENT PRICES AS OF {time_string} CST\n"
        percent_string = f"Current PERCENTAGE CHANGE AS OF {time_string} CST \n"

        for i in range(5):
            price = float(json[i]['price_usd'])
            price = round(price, 4)
            string += json[i]['name']
            percent_change = (starting_prices[i] - price)/ starting_prices[i]
            percent_change = round(percent_change, 4)
            percent_string += json[i]['name']
            percent_string += ": " + str(percent_change) + "%\n"
            string += ": $" + str(price) + "\n"
        string += "#BTC #DOGE #ETH #XLM #XTZ"
        percent_string += "#BTC #DOGE #ETH #XLM #XTZ"
        api.update_status(status=string)
        api.update_status(status=percent_string)

    def closing_prices(self,api):
        starting_prices = self.starting_prices
        response = requests.get(self.url, headers=self.header)
        json = response.json()
        current_time = datetime.datetime.now()
        time_string = current_time.strftime("%m/%d/%Y")
        string = f"CLOSING PRICES FOR {time_string} \n"
        percent_string = f"CLOSING PERCENTAGE CHANGE FOR {time_string} \n"
        for i in range(5):
            price = float(json[i]['price_usd'])
            price = round(price, 4)
            string += json[i]['name']
            percent_change = (starting_prices[i] - price)/ starting_prices[i]
            percent_change = round(percent_change, 4)
            percent_string += json[i]['name']
            percent_string += ": " + str(percent_change) + "%\n"
            string += ": $" + str(price) + "\n"
        string += "#BTC #DOGE #ETH #XLM #XTZ"
        api.update_status(status=string)
        api.update_status(status=percent_string)


# imports

import sys
import requests
import pprint

#building the URL for this ticker
def ticker_rsi(ticker):
    url = f'https://api.polygon.io/v1/indicators/rsi/{ticker}?timespan=day&adjusted=true&window=14&series_type=close&order=desc&apiKey=qFFLI3NFZJc5e7qifG8bjPd9miTZ0F_l'
    response = requests.get((url))
    if response.status_code != 200:
        print(f'got code {response.status_code} for URL: {url}')
        exit()

#use a get call to pull the URL into the code

#create dict from site pull

    rsidictionary = response.json()

#variables

    ticker_time = float(rsidictionary["values"][0]["timestamp"])
    ticker_value = float(rsidictionary["values"][0]["value"])

    #here is where you will add in underbought / undersold

    return {'Time': ticker_time , 'Value': ticker_value}

#cleans up text return

if __name__ == "__main__":
    clean = pprint.PrettyPrinter(indent = 3)

#beginning user input

userinput = input(f'enter a list of space-seperated stock tickers here:')

tickers = userinput.split(' ')

print(f'\n Here is a list of your securities and the associated values.')

#rsi dictionary

rsi = {}

for ticker in tickers:

    ticker_data = ticker_rsi(ticker)
    rsi [ticker] = ticker_data

#sorting returns underbought to overbought

sorted_rsi = sorted(rsi.items(), key=lambda x: x[1]["values"], reverse=True)

clean.pprint(sorted_rsi)






#bringing in clean formatting

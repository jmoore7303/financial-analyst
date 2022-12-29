import sys
print(f'\nDAILY STOCK ANALYZER')

import requests
import pprint

#when you declare a function, you must do it as "def funtion(arguement)"

def get_ticker_data(ticker):
    #build url for this ticker

    ticker_url = f'https://api.polygon.io/v2/aggs/ticker/{ticker}/prev?adjusted=true&apiKey=qFFLI3NFZJc5e7qifG8bjPd9miTZ0F_l'
    response = requests.get((ticker_url))
    if response.status_code != 200:
        print(f'Got code {response.status_code} for URL: {ticker_url}')
        exit(1)

    #none is null in python

    #make get call on URL

    #pull out only open, and close
    # .json gives you a dictionary assuming that the list was in JSON.

    stock_dict = response.json()
    ticker_open = float(stock_dict["results"][0]["o"])
    ticker_close = float(stock_dict["results"][0]["c"])
    ticker_change = round((((ticker_close / ticker_open) - 1) * 100), 3)


    #calculate the change by dividing close by open

    #return to dict as {'open': 100, 'close':102, 'change': 1.020}

    return {'Open': ticker_open, 'Close':ticker_close, '% Change': ticker_change}


#high-level goal:
# take a list of ticker symbols,
# find previous day open and close, find biggest gainer,
# find biggest percentage gainer,
#find biggest percentage loser,

if __name__ == "__main__":
    gorgeous = pprint.PrettyPrinter(indent = 3)
#assume we start with a list of tickers. All lists are in brackets.

    # tickers = ["AAPL", "AMZN", "MSFT"]

    #allows user to control stock searh

    user_input = input(f'\nPlease enter a list of stock tickers separated by spaces: ')

    tickers = user_input.split(' ')

    print(f'\nWise choices. A report on the following securities:\n{user_input}\nis featured below.')



    prices = {} #curly brackets declares empty dictionary

    ##for each ticker in the tickers variable
    #(which is a code-compatible version of the user input)

    for ticker in tickers:

#we take our function get ticker data, use the API to grab the dictionary from their URL
#Format it assuming JSON compatibility (usually true)

        ticker_data = get_ticker_data(ticker)
        prices [ticker] = ticker_data #this is the syntax to add something to a dictionary in a for loop.


# sort the dictionary by % change
    sorted_prices = sorted(prices.items(), key=lambda x: x[1]["% Change"], reverse=True)

    #to sort a dictionary first convert to list and then sort

    gorgeous.pprint(sorted_prices)

    print(f'The best performer of the day is: {sorted_prices[0][0]}')
    print(f'The worst performer of the day is: {sorted_prices[-1][0]}')



#curleques are used for dictionaries
#I'll call the API to get the open and close. Then I would find the biggest changes percentage wise.

    # prices = {
    #     'AAPL' : {'open': 100, 'close':102, 'change': 1.020},
    #     'AMZN': {'open': 120, 'close': 130, 'change': 1.083},
    #     'MSFT': {'open': 140, 'close': 160, 'change': 1.071}
    # }


#we would use a .json to conveniently format data that's mostly text.
#every peice of data can have a name inside of it, easy to understand.
#data is nested and flexible
#JSON is JavaScript Object Notation. JSON is strings following pattern {key:value, key:value}
    #has to be string, number, another json object, or array
    #It's recursive: any value in JSON can itself be a JSON object.
    #JSON can have lists just like python lists.
#URL is uniform resource locator or "thing that is in the universe and can be called".









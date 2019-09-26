from django.shortcuts import render
import requests
import json


def home(request):
    #Grab crypto price
    price_requests = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,LTC,EOS,BCH,LINK,TRX,ETC,BNB&tsyms=USD')
    price = json.loads(price_requests.content)

    # Grab crypto news
    api_requests = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
    api = json.loads(api_requests.content) #turns json JavaScript(api_requests.content) object into python dictionary
    return render(request, 'home.html', {'api': api, 'price': price})


    #print(api_requests)
    #print(api_requests.content)
    #print('________________________________________________________________________________________________________________')
    #print(api_requests.text)

def prices(request):
    if request.method == 'POST':
        quote = request.POST['quote']
        quote = quote.upper()
        crypto_requests = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms='+quote+'&tsyms=USD')
        crypto = json.loads(crypto_requests.content)
        return render(request, 'prices.html', {'crypto': crypto, 'quote': quote})
    else:
        #notFound = "Welcome"
        price_requests = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,LTC,EOS,BCH,LINK,TRX,ETC,BNB&tsyms=USD')
        price = json.loads(price_requests.content)
        return render(request, 'prices.html', {'price': price})

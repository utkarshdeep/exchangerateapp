from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests

# Create your views here.

def index(request):
    # define the temlate name
    template = 'index.html'
    url = "https://openexchangerates.org/api/latest.json"
    key = "e64888fb29ea48bd8704b52f0cbeb1e3"

    if request.method == 'POST':

        # base currency
        base_currency = request.POST.get('currency1', False)

        # target currency
        target_currency = request.POST.get('currency2', False)

        response = requests.get(f"{url}?app_id={key}&base={base_currency}&symbols={target_currency}")

        # response data convterted to json
        data = response.json()
        rate = data['rates'][target_currency]
        context = {"rate": rate}

        # render the template with the data passed to it
        return render(request, template, context)
    else:
        return render(request, template)

def historical(request):
    # specify the templaet name
    template = 'historical.html'
    url = "https://openexchangerates.org/api/historical"
    key = "e64888fb29ea48bd8704b52f0cbeb1e3"


    if request.method == 'POST':
        # extract date from the post request
        date = request.POST.get('date', False)   

        base_currency = request.POST.get('currency1', False)

        # pass api response to a variable
        response = requests.get(f"{url}/{date}.json?app_id={key}")

        # convert the response data to json
        data = response.json()
        quotes = data['rates']
        context = {'quotes': quotes}

        # Passing the data to the temlate
        return render(request, template, context)
    else:
        return render(request, template)

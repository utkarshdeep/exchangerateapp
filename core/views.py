from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests
from django.conf import settings
import logging

logger = logging.getLogger('exchangerateapp.core.views.py')


try:
    key = settings.APP_ID
    base_url = settings.EXCHANGE_URL
except AttributeError as e:
    logger.error("The key APP_ID and/or EXCHANGE_URL has been incorrectly defined in settings.py file. Kindly correct it and restart. Shutting down.")
    raise SystemExit(e)

def index(request):
    # define the temlate name
    template = 'index.html'
    url = base_url + "latest"

    if request.method == 'POST':

        logger.info("User has requested the latest ER page WITH POST request.")

        # base currency
        base_currency = request.POST.get('currency1', False)

        # target currency
        target_currency = request.POST.get('currency2', False)
        try:
            response = requests.get(f"{url}?app_id={key}&base={base_currency}&symbols={target_currency}")
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            error = response.json()['message']
            logger.error("A HTTPError has been ecountered: "+ error)
            context = {"is_error": True, "rate" : error + ". Please rectify the issue and try again."}
            return render(request, template, context)
        except requests.exceptions.RequestException as err:
            logger.info("An unexpected error has been encoutered: ", err.strerror)
            raise SystemError(err)

        logger.info(f"The API request to external service openexchangerates to get exchange rate of {target_currency} against {base_currency} has been completed successfuly.")
        # response data convterted to json
        data = response.json()
        rate = data['rates'][target_currency]
        context = {"is_error": False, "rate": f"1 {base_currency} = {rate} {target_currency}"}

        # render the template with the data passed to it
        return render(request, template, context)
    else:
        logger.info("User has requested the latest ER page WITHOUT any POST request.")
        return render(request, template)

def historical(request):
    # specify the templaet name
    template = 'historical.html'
    # url = base_url + "historical"

    if request.method == 'POST':

        logger.info("User has requested the latest ER page WITH POST request.")

        # extract date from the post request
        date = request.POST.get('date', False)
        # base currency
        base_currency = request.POST.get('currency1', False)

        # target currency
        target_currency = request.POST.get('currency2', False)   

        try:
            response = requests.get(f"{base_url}/{date}?base={base_currency}&symbols={target_currency}")
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            error = response.json()['message']
            logger.error("A HTTPError has been ecountered: "+ error)
            context = {"is_error": True, "rate" : error + ". Date must lie between 1st Jan 1999 and previous day. Please try again."}
            return render(request, template, context)
        except requests.exceptions.RequestException as err:
            logger.info("An unexpected error has been encoutered: ", err.strerror)
            raise SystemError(err)

        logger.info(f"The API request to external service openexchangerates to fetch exchange rate on {date} against USD has been completed successfuly.")

        # convert the response data to json
        data = response.json()
        quotes = data['rates']
        context = {"is_error": False, 'quotes': quotes}

        # Passing the data to the temlate
        return render(request, template, context)
    else:
        logger.info("User has requested the latest ER page WITHOUT any POST request.")
        return render(request, template)

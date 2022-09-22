import requests


def get_currency_exchange_rate(date: str, bank: str, c1: str, c2: str, ):
    response = requests.get(f'https://api.privatbank.ua/p24api/exchange_rates?json&date={date}')
    json = response.json()
    exchange_rate = json.get('exchangeRate')

    if response.status_code == 200:
        if bank == 'PB':
            for items in range(len(exchange_rate)):
                if exchange_rate[items].get('baseCurrency') == c1 and exchange_rate[items].get('currency') == c2:
                    purchase_rate = exchange_rate[items].get('purchaseRate')
                    sale_rate = exchange_rate[items].get('saleRate')
                    return f'Exchange rate date: {date}; Bank: PrivatBank; Exchange rate {c1} to {c2}; Purchase rate' \
                           f' - {purchase_rate} ; Sale rate - {sale_rate}'
            raise KeyError(f'Currency exchange rate error {c1} to {c2}')
        elif bank == 'NB':
            for items in range(len(exchange_rate)):
                if exchange_rate[items].get('baseCurrency') == c1 and exchange_rate[items].get('currency') == c2:
                    purchase_rate_nb = exchange_rate[items].get('purchaseRateNB')
                    sale_rate_nb = exchange_rate[items].get('saleRateNB')
                    return f'Exchange rate date: {date}; Bank: National Bank; Exchange rate {c1} to {c2}; ' \
                           f'Purchase rate - {purchase_rate_nb} ; Sale rate - {sale_rate_nb}'
            raise KeyError(f'Currency exchange rate error {c1} to {c2}')
        else:
            return f'Bank: {bank} not found!'
    else:
        return f'API Error (status_code: {response.status_code})'

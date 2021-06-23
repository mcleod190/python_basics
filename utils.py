from requests import get, utils
import xml.etree.ElementTree as ET


#helper
def get_all_rates():
    api_url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = get(api_url)
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    xml = ET.fromstring(content)
    server_date = xml.attrib['Date']

    rates = {'server_date': server_date}
    for curr in xml.findall('Valute'):
        currency_code = curr.find('CharCode').text
        rate = curr.find('Value').text
        rates[currency_code] = rate
    return rates


def currency_rates(currency_code):
    all_rates = get_all_rates()
    date = all_rates['server_date']
    currency_rate = all_rates.get(currency_code.upper())
    if not currency_rate:
        return 'error. no such currency {}'.format(currency_code)
    currency_rate = float(currency_rate.replace(',', '.'))
    return(date, currency_rate)


def test():
    for c in ['usd', 'eur']:
        print(currency_rates(c))


if __name__ == '__main__':
    test()

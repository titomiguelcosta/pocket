import requests
import random
import logging

class TransferWise:
    token = "YjRhODM3MWUtZTE3Yi00NTIzLWE2MDgtMGMwNDFmYTBiOTRlOjEwMjIxNDFhLTliZGMtNDNkZS1hZGU0LWVlMzQ4OGNiNmNhZQ=="
    authorisation_key = "dad99d7d8e52c2c8aaf9fda788d8acdc"

    def get_rate(self, source="EUR", target="GBP"):
        rate = None
        headers = self.get_headers()
        headers.update({"x-authorization-key": self.authorisation_key})
        while rate is None:
            r = requests.get(
                "https://transferwise.com/api/v1/payment/calculate",
                headers=headers,
                params={
                    "amountCurrency": "source",
                    "getNoticeMessages": "true",
                    "hasDiscount": "false",
                    "payInMethod": "REGULAR",
                    "sourceCurrency": source,
                    "targetCurrency": target,
                    "amount": random.randint(1000, 9000)
                }
            )
            json = r.json()
            if 200 == r.status_code and "transferwiseRate" in json:
                rate = float(json["transferwiseRate"])
            else:
                logging.getLogger(__name__).warning(str(r.content))

        return rate

    def get_fee(self, amount, source="EUR", target="GBP"):
        fee = None
        headers = self.get_headers()
        headers.update({"x-authorization-key": self.authorisation_key})

        r = requests.post(
            "https://transferwise.com/gateway/v2/quotes/",
            headers=headers,
            json={
                "sourceCurrency": source, 
                "targetCurrency": target, 
                "sourceAmount": amount,
                "preferredPayIn": "BANK_TRANSFER"
            },
        )
        
        if 200 == r.status_code:
            json = r.json()

            for paymentOption in json["paymentOptions"]:
                if not paymentOption["disabled"] and "PERSONAL" in paymentOption["allowedProfileTypes"]:
                    fee = float(paymentOption["fee"]["transferwise"])
                    
                    break
        return fee

    def get_headers(self):
        return {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
            "Referer": "https://transferwise.com",
            "Origin": "https://transferwise.com",
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
            "Accept": "application/json, text/plain, */*",
        }

import requests
import random


class TransferWise:
    token = "YjRhODM3MWUtZTE3Yi00NTIzLWE2MDgtMGMwNDFmYTBiOTRlOjEwMjIxNDFhLTliZGMtNDNkZS1hZGU0LWVlMzQ4OGNiNmNhZQ=="
    authorisation_key = "dad99d7d8e52c2c8aaf9fda788d8acdc"

    def get_rate(self, source="EUR", target="GBP"):
        rate = None
        headers = self.get_headers()
        headers.update({"Authorization": "Basic " + self.token})
        while rate is None:
            r = requests.get(
                "https://api.transferwise.com/v1/comparisons",
                headers=headers,
                params={"source": source, "target": target, "excludeCheaper": "false", "amount": random.randint(1000, 9000)}
            )
            json = r.json()
            if 200 == r.status_code and len(json["providers"]) > 0:
                rate = json["providers"][0]["rate"]

        return rate

    def get_fee(self, amount, source="EUR", target="GBP"):
        fee = None
        headers = self.get_headers()
        headers.update({"x-authorization-key": self.authorisation_key})

        while fee is None:
            r = requests.get(
                "https://transferwise.com/api/v1/pricing/calculateFee",
                headers=headers,
                params={"sourceCurrency": source, "targetCurrency": target, "amount": amount},
            )
            json = r.json()
            if 200 == r.status_code and "fee" in json:
                fee = float(json["fee"])

        return fee

    def get_headers(self):
        return {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
            "Referer": "https://transferwise.com/nz/",
            "Origin": "https://transferwise.com",
        }


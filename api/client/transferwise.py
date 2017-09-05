import requests

class TransferWise:
  url = "https://api.transferwise.com/v1/comparisons"
  token = "YjRhODM3MWUtZTE3Yi00NTIzLWE2MDgtMGMwNDFmYTBiOTRlOjEwMjIxNDFhLTliZGMtNDNkZS1hZGU0LWVlMzQ4OGNiNmNhZQ=="
  user_agent = "Mozilla/5.0"
  referer = "https://transferwise.com/nz/"
  origin = "https://transferwise.com"

  def get_rate(self, source="EUR", target="GBP"):
    r = requests.get(self.url, headers=self.get_headers(), params={"source": source, "target": target, "amount": 1000})
    rate = None
    if 200 == r.status_code:
      rate = r.json()["providers"][0]["rate"]

    return rate
    
  def get_headers(self):
    return {"Authorization": "Basic " + self.token, "User-Agent": self.user_agent, "Referer": self.referer, "Origin": self.origin,}

if __name__ == "__main__":
  c = TransferWise()
  print("Rate from EUR to GBP: %.5f" % c.get_rate())
  print("Rate from NZD to EUR: %.5f" % c.get_rate("NZD", "EUR"))

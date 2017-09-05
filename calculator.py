class Calculator:
  def calculate_rate(self, deposit, fees, cash_out):
    """
    Calculate rate needed to make a certain cash out on a transaction
    """
    return cash_out / (deposit - fees)

  def cash_out(self, deposit, fees, rate):
    """
    Determine how much cash out we get for a transaction
    """
    return (deposit - fees) * rate


if __name__ == "__main__":
  from fees import FeeManager

  c = Calculator()
  f = FeeManager()

  cash_out = c.cash_out(20000, f.fee(5000), 0.55763)
  print("I transfer NZD5000 to GBP with a rate of 0.55763: %.2fGBP" % cash_out)
  print("To profit 50NZD the rate must be at least %.5f" % c.calculate_rate(cash_out, f.fee(cash_out), 20050))
  print("To profit 100NZD the rate must be at least %.5f" % c.calculate_rate(cash_out, f.fee(cash_out), 20100))
  print("To profit 200NZD the rate must be at least %.5f" % c.calculate_rate(cash_out, f.fee(cash_out), 20200))

class TransferWiseFee:
  def __init__(self, percentage):
     self.percentage = percentage

  def fee(self, amount):
     return amount * self.percentage / 100


class FeeManager:
  def __init__(self):
    self.fees = [TransferWiseFee(0.7)]

  def fee(self, amount):
    total = 0.0
    for f in self.fees:
      total += f.fee(amount)

    return total


if __name__ == "__main__":
  f = TransferWiseFee(0.7)
  print("Fee for an amount of 1000: %.2f" % f.fee(1000))

  m = FeeManager()
  print("Fee for an amount of 3000: %.2f" % m.fee(3000))

from api.client.transferwise import TransferWise


class LloydsFee:
    """
    Fees charged by Lloyds
    """
    def fee(self, amount, source="EUR", target="GPB"):

        return 0.0


class BNZFee:
    """
    Fees charged by BNZ
    """
    def fee(self, amount, source="EUR", target="GPB"):

        return 0.0


class MillenniumBcpFee:
    """
    Fees charged by MillenniumBcp
    """
    def fee(self, amount, source="EUR", target="GPB"):

        return 1.57 if source == "EUR" else 0.0


class TransferWiseFee:
    client = TransferWise()

    """
    Fees charged by TransferWise
    """
    def fee(self, amount, source="EUR", target="GPB"):

        return self.client.get_fee(amount, source, target)


class FeeManager:
    def __init__(self, fees=None):
        self.fees = [TransferWiseFee(), MillenniumBcpFee(), BNZFee(), LloydsFee()] if fees is None else fees

    def fee(self, amount, source="EUR", target="GPB"):
        total = 0.0
        for f in self.fees:
            total += f.fee(amount, source=source, target=target)

        return total

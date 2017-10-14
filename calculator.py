class Calculator:
    def calculate_rate(self, amount, fees, cash):
        """
        Calculate rate needed to make a certain cash out on a transaction
        """
        return cash / (amount - fees)

    def cash_out(self, amount, fees, rate):
        """
        Determine how much cash out we get for a transaction
        """
        return (amount - fees) * rate

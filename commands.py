from argparse import ArgumentParser
from fees import FeeManager
from api.client.transferwise import TransferWise
from calculator import Calculator

parser = ArgumentParser(description='Process meter data')


def default_command(args):
    """
    Handler for the default command
    """
    parser.print_help()


def fees_command(args):
    fee_manager = FeeManager()
    amount = float(args.amount)
    print("Amount %.2f%s pay fees of %.2f%s." % (
        amount, args.source, fee_manager.fee(amount, source=args.source, target=args.target), args.source
    ))


def transfer_command(args):
    fee_manager = FeeManager()
    calculator = Calculator()
    transferwise = TransferWise()
    amount = float(args.amount)
    fees = fee_manager.fee(amount, args.source, args.target)
    rate = transferwise.get_rate(args.source, args.target)
    print("By transfering %.2f%s you get %.2f%s (fees of %.2f%s with a rate of %.5f)." % (
        amount, args.source, calculator.cash_out(amount, fees, rate), args.target, fees, args.source, rate
    ))


def rate_command(args):
    transferwise = TransferWise()
    print("Exchange rate of %.5f from %s to %s." % (
        transferwise.get_rate(args.source, args.target), args.source, args.target
    ))


def profit_command(args):
    calculator = Calculator()
    fee_manager = FeeManager()
    transferwise = TransferWise()
    transferred = float(args.transferred)
    profit = float(args.profit)

    if args.cashed is None:
        cashed = calculator.cash_out(
            transferred,
            fee_manager.fee(transferred, args.source, args.target),
            transferwise.get_rate(args.source, args.target)
        )
    else:
        cashed = float(args.cashed)

    amount = transferred + profit
    print("To profit %.2f%s the rate from %s to %s must be at least %.5f (%.5f)" % (
        profit,
        args.source,
        args.target,
        args.source,
        calculator.calculate_rate(cashed, fee_manager.fee(amount, args.target, args.source), amount),
        transferwise.get_rate(args.target, args.source)
    ))
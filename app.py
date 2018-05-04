from flask import Flask
from flask import jsonify
from api.client.transferwise import TransferWise
from calculator import Calculator
from fees import FeeManager

app = Flask(__name__)


@app.route('/rate', defaults={'source': 'EUR', 'target': 'GBP'})
@app.route('/rate/<string:source>', defaults={'target': 'GBP'})
@app.route("/rate/<string:source>/<string:target>")
def rate(source='EUR', target='GBP'):
    transferwise = TransferWise()
    rate = transferwise.get_rate(source, target)
    return jsonify({
        "description": "Exchange rate of %.5f from %s to %s." % (
            rate, source.upper(), target.upper()
        ),
        "rate": rate,
        "source": source.upper(),
        "target": target.upper()
    })


@app.route("/profit/<transferred>/<profit>", defaults={'source': 'EUR', 'target': 'GBP'})
@app.route("/profit/<transferred>/<profit>/<cashed>", defaults={'source': 'EUR', 'target': 'GBP'})
@app.route("/profit/<transferred>/<profit>/<string:source>", defaults={'target': 'GBP'})
@app.route("/profit/<transferred>/<profit>/<cashed>/<string:source>", defaults={'target': 'GBP'})
@app.route("/profit/<transferred>/<profit>/<string:source>/<string:target>")
@app.route("/profit/<transferred>/<profit>/<cashed>/<string:source>/<string:target>")
def profit(transferred, profit, cashed=None, source='EUR', target='GBP'):
    calculator = Calculator()
    fee_manager = FeeManager()
    transferwise = TransferWise()
    transferred = float(transferred)
    profit = float(profit)
    if cashed is None:
        cashed = calculator.cash_out(
            transferred,
            fee_manager.fee(transferred, source, target),
            transferwise.get_rate(source, target)
        )
    else:
        cashed = float(cashed)
    amount = transferred + profit
    rate = calculator.calculate_rate(cashed, fee_manager.fee(cashed, target, source), amount)

    return jsonify({
        "description": "To profit %.2f%s the rate from %s to %s must be at least %.5f" % (
            profit,
            source.upper(),
            target.upper(),
            source.upper(),
            rate
        ),
        "rate": rate,
        "transferred": transferred,
        "profit": profit,
        "cashed": cashed,
        "source": source.upper(),
        "target": target.upper()
    })


@app.route("/balance/<transferred>/<cashed>", defaults={'source': 'EUR', 'target': 'GBP'})
@app.route("/balance/<transferred>/<cashed>/<string:source>", defaults={'target': 'GBP'})
@app.route("/balance/<transferred>/<cashed>/<string:source>/<string:target>")
def balance(transferred, cashed, source='EUR', target='GBP'):
    calculator = Calculator()
    fee_manager = FeeManager()
    transferwise = TransferWise()
    transferred = float(transferred)
    cashed = float(cashed)
    rate = transferwise.get_rate(target, source)

    fees = fee_manager.fee(cashed, source=target, target=source)
    cash_out = calculator.cash_out(cashed, fees, rate)
    balance = cash_out - transferred

    return jsonify({
        "description": "Balance of %.2f%s by transferring back %.2f%s" % (
            balance, source.upper(), cashed, target.upper()
        ),
        "rate": rate,
        "transferred": transferred,
        "cashed": cashed,
        "balance": float(format(balance, ".2f")),
        "source": source.upper(),
        "target": target.upper()
    })

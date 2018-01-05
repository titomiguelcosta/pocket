from flask import Flask
from flask import jsonify
from .api.client.transferwise import TransferWise
from .calculator import Calculator
from .fees import FeeManager

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


@app.route("/outcome/<float:transferred>/<float:cashed>", defaults={'source': 'EUR', 'target': 'GBP'})
@app.route("/outcome/<int:transferred>/<int:cashed>", defaults={'source': 'EUR', 'target': 'GBP'})
@app.route("/outcome/<float:transferred>/<float:cashed>/<string:source>", defaults={'target': 'GBP'})
@app.route("/outcome/<int:transferred>/<int:cashed>/<string:source>", defaults={'target': 'GBP'})
@app.route("/outcome/<float:transferred>/<float:cashed>/<string:source>/<string:target>")
@app.route("/outcome/<int:transferred>/<int:cashed>/<string:source>/<string:target>")
def outcome(transferred, cashed, source='EUR', target='GBP', rate=None):
    calculator = Calculator()
    fee_manager = FeeManager()
    transferwise = TransferWise()
    transferred = float(transferred)
    cashed = float(cashed)
    rate = float(rate) if rate is not None else transferwise.get_rate(target, source)

    fees = fee_manager.fee(cashed, source=target, target=source)
    cash_out = calculator.cash_out(cashed, fees, rate)
    outcome = cash_out - transferred

    return jsonify({
        "description": "Outcome of %.2f%s by transferring back %.2f%s" % (
            outcome, source, cashed, target
        ),
        "rate": rate,
        "transferred": transferred,
        "cashed": cashed,
        "outcome": float(format(outcome, ".2f")),
        "source": source,
        "target": target
    })

from flask import Flask
from flask import jsonify
from api.client.transferwise import TransferWise

app = Flask(__name__)

@app.route('/rate', defaults={'source': 'EUR', 'target': 'GBP'})
@app.route('/rate/<string:source>', defaults={'target': 'GBP'})
@app.route("/rate/<string:source>/<string:target>")
def rate(source='EUR', target='GBP'):
    transferwise = TransferWise()
    rate = transferwise.get_rate(source, target)
    return jsonify({
        "description": "Exchange rate of %.5f from %s to %s." % (
            rate, source, target
        ),
        "rate": rate,
        "source": source,
        "target": target
    })



from flask import Flask


app = Flask(__name__)


@app.route('/query/<symbol>/<timestamp>', methods=['GET'])
def get_data(symbol, timestamp):
    return '{0} {1}'.format(symbol, timestamp)


if __name__ == '__main__':
    app.run()

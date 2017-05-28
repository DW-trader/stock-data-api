
import simplejson as json
from flask import Flask
from influxdb import InfluxDBClient


def _get_data(symbol, timestamp):
    client = InfluxDBClient('localhost', 8086, 'root', 'root', 'test')
    query_str = 'select * from daily_stock_data where symbol = \'{0}\' and time > \'{1}\''.format(symbol, timestamp)

    points = client.query(query_str).get_points()

    result = []
    for point in points:
        result.append(point)

    return result


app = Flask(__name__)


@app.route('/query/<symbol>/<timestamp>', methods=['GET'])
def get_data(symbol, timestamp):
    data = _get_data(symbol, timestamp)
    return json.dumps(data)


if __name__ == '__main__':
    app.run()

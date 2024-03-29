from flask import Flask, render_template, request, jsonify
from flask.helpers import send_from_directory
from arima import arima_predict
from FB_prophet import prophet_predict

app = Flask(__name__)


@app.route('/')
def landing():
    return render_template('index.html')

@app.route('/date', methods=['POST'])
def submit_date():
    if request.method == 'POST':
        start_year = request.form['start_year']
        end_year = request.form['end_year']
    
    if request.form['model'] == 'sarima':
        forecast_dict = arima_predict(start_year, end_year )
        return  jsonify(forecast_dict) 
    elif request.form['model'] == 'prophet':
        forecast_dict = prophet_predict(start_year, end_year )
        return  jsonify(forecast_dict) 
@app.route('/actualPop', methods=['GET'])
def return_actual_population():
    return send_from_directory('static', 'actualUSPopulation.json')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

from flask import Flask, render_template, request, jsonify
from arima import predict

app = Flask(__name__)


@app.route('/')
def landing():
    return render_template('index.html')

@app.route('/date', methods=['POST'])
def submit_date():
    if request.method == "POST":
        start_year = request.form['start_year']
        end_year = request.form['end_year']
    forecast_dict = predict(start_year, end_year )
    return  jsonify(forecast_dict) 


if __name__ == '__main__':
    app.run(debug=True)

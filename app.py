from flask import Flask, render_template, request, jsonify
from arima import predict

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/sub', methods=['POST'])
def submit():
    if request.method == "POST":
        name = request.form['username']
    return render_template('sub.html', n=name)

@app.route('/date', methods=['POST'])
def submit_date():
    if request.method == "POST":
        year = request.form['year_request']
    #return render_template('sub.html', n=json_object)
    forecast_dict = predict('1980', year )
    return  jsonify(forecast_dict) 

@app.route('/myForm', methods=['POST'])
def type_model():
    pass


if __name__ == '__main__':
    app.run(debug=True)

# Importing essential libraries
from flask import Flask, render_template, request
import pandas as pd


app = Flask(__name__ , static_folder="static")

data=pd.read_csv('Forcast predction.csv')
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        time = int(request.form['Time for Forcast'])
        time=time/10
        prediction=data.loc[time]


        return render_template('result.html', prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True)
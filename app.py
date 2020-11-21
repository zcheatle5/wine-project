
# import necessary libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

##############################################################

app = Flask(__name__) #Initialize the flask App
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/tableau')
def tableau():
    return render_template('tableau.html')


@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)
    A = round(prediction[0], 2)
    W = round((prediction *2*756)[0], 2)

    return render_template('index.html', prediction_text=f'The 2020 Napa Valley wine grape yield should be about {A} acres based on 2011-2019 data.', wine_text=f'Assuming a low end yield of 2 tons of wine per acre, this is equivalent to {W} bottles of wine.')

if __name__ == "__main__":
    app.run(debug=True)
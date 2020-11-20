
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

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Next Years Yield Should Be {} Wine Grape Acres', wine_bottle_text='Napa will have ({}*2) bottles of wine next year'.format(output))

if __name__ == "__main__":
    app.run(debug=True)
import numpy as np
from flask import Flask, request, render_template
import pickle


app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
MMS = pickle.load(open('MMS.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    input_list = list(map(int, request.form.values()))
    array = np.array(input_list).reshape(1,12)
    final_array = MMS.transform(array)
    prediction = model.predict(final_array)
    if int(prediction==0):
        output = 'Approved'
    else:
        output = 'Rejected'
        

    return render_template('index.html', prediction_text='Your Credit Card application will get : {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
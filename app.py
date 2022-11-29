import io
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    request_type_str = request.method
    if request_type_str == 'GET':
        return (render_template('index.html'))
    else:
        text = request.form['text']
        text_list = [float(item) for item in text.split(',')]
        model = pickle.load(open('model.sav', 'rb'))
        prediction = model.predict([text_list])
        prediction_perc = model.predict_proba([text_list])

        if (prediction == 0.0):
            return ("This input is not a pulsar. Certainty: " + str((prediction_perc[0][0]) * 100) + "%. Press back to type another input.")
        
        else:
            return ("This input has been detected as a pulsar. Certainty: " + str((prediction_perc[0][0]) * 100) + "%. Press back to type another input.")



if __name__ == "__main__":
    app.run(host="0.0.0.0")
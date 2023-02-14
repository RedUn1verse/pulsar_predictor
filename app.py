from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def pulsar_application():
    request_type_str = request.method

    # Renders the landing page.

    if request_type_str == 'GET':
        return (render_template('index.html', prediction=""))
    else:

        # Renders page on submit with user inputted information.

        meanIntegratedProfile = request.form['meanIntegratedProfile']
        standardDeviationIntegratedProfile = request.form['standardDeviationIntegratedProfile']
        kurtosisIntegratedProfile = request.form['kurtosisIntegratedProfile']
        skewnessIntegratedProfile = request.form['skewnessIntegratedProfile']
        meanDM_SNR = request.form['meanDM_SNR']
        standardDeviationDM_SNR = request.form['standardDeviationDM_SNR']
        kurtosisDM_SNR = request.form['kurtosisDM_SNR']
        skewnessDM_SNR = request.form['skewnessDM_SNR']

        # Ensures data inputs are correctly formatted

        try:
            text_list = [float(meanIntegratedProfile), float(standardDeviationIntegratedProfile), float(kurtosisIntegratedProfile),
                         float(skewnessIntegratedProfile), float(meanDM_SNR), float(standardDeviationDM_SNR),
                           float(kurtosisDM_SNR), float(skewnessDM_SNR)]
        except ValueError:
            return (render_template('index.html', prediction="Invalid input format, Please try again."))

        # Loads logisitic regression model from model.sav and runs data through to make prediction.

        model = pickle.load(open('model.sav', 'rb'))
        prediction = model.predict([text_list])
        prediction_perc = model.predict_proba([text_list])

        # Changes page render according to model prediction.

        if (prediction == 0.0):
            return (render_template('index.html', prediction="This input is not a pulsar. Certainty: " + str((prediction_perc[0][0]) * 100) + "%."))
        elif (prediction == 1.1):
            return (render_template('index.html', prediction="This input has been detected as a pulsar. Certainty: " + str((prediction_perc[0][0]) * 100) + "%."))
        else:
            return (render_template('index.html', prediction="Inconclusive"))
        
if __name__ == "__main__":
    app.run(host="0.0.0.0")
# pulsar_predictor

Made for the MAIS Machine Learning Bootcamp.

Predicts whether a star is a pulsar based off of telescope data. This project employs a logistic regression model to classify inputs as either a pulsar or not a pulsar.

Imports:

- pickle
- from sklearn.linear_model LogisticRegression
- csv
- io
- from Flask Flask, render_template, request

Instructions:

Run app.py to generate the web app. To retrain the model, edit/run pulsar_predictor.py, the new model will be displayed on the webapp the next time that it is run.

This project uses the following dataset: https://archive.ics.uci.edu/ml/datasets/HTRU2

As requested, the following is the citation of the research that gathered this data.

R. J. Lyon, B. W. Stappers, S. Cooper, J. M. Brooke, J. D. Knowles, Fifty Years of Pulsar Candidate Selection: From simple filters to a new principled real-time classification approach, Monthly Notices of the Royal Astronomical Society 459 (1), 1104-1123, DOI: 10.1093/mnras/stw656


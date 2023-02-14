import data_clean as data_clean
from sklearn.linear_model import LogisticRegression
import pickle


## RUN THIS FILE ONCE TO TRAIN LOGISTIC REGRESSION MODEL ##

# Calls the data cleaning functions to load and prepare pulsar data into three datasets.

pulsar_list = data_clean.clean("raw_pulsar_data.csv")
X_list = data_clean.split_data(pulsar_list[0], 5966)
Y_list = data_clean.split_data(pulsar_list[1], 5966)

# Sets hyperparameters as well as train the logistic regression model on the training set.

clf = LogisticRegression(random_state=1, max_iter=1000, penalty='l2', C=500, solver='liblinear').fit(X_list[0], Y_list[0])

# Simple test

results_prob = clf.predict_proba(X_list[1])
results = clf.predict(X_list[2])

result_test = clf.predict([[145.3125,46.60484652,-0.402589353,0.311179659,2.79264214,17.77612015,8.892784928,95.81944158]])
print(result_test)

# Saves model to model.sav to be used by the app.

pickle.dump(clf, open('model.sav', 'wb'))

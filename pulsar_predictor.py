import data_clean
from sklearn.linear_model import LogisticRegression
pulsar_list = data_clean.clean("raw_pulsar_data.csv")
X_list = data_clean.split_data(pulsar_list[0], 5966)
Y_list = data_clean.split_data(pulsar_list[1], 5966)

clf = LogisticRegression(random_state=0, max_iter=1000).fit(X_list[0], Y_list[0])

results = clf.predict(X_list[1])

#print (list(results))
print (clf.score(X_list[1], Y_list[1]))
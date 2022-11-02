import data_clean
from matplotlib import pyplot as plt

def plot_data(x, y):
	plt.xlabel('score of test-1')
	plt.ylabel('score of test-1')
	for i in range(x.shape[0]):
		if y[i] == 1:
			plt.plot(x[i,0], x[i,1], 'gX')
		else:
			plt.plot(x[i,0], x[i,1], 'mD')
	plt.show()


pulsar_list = data_clean.clean("raw_pulsar_data.csv")
X_list = data_clean.split_data(pulsar_list[0], 5966)
Y_list = data_clean.split_data(pulsar_list[1], 5966)

dataset = [[0,2,0],
	[2,0,0],
	[3,0,0],
	[0,2,0],
	[2,2,0],
	[5,1,1],
	[5,2,1],
	[2,4,1],
	[4,4,1],
	[5,5,1]]



def predict(row, weights):
	activation = weights[0]
	for i in range(len(row)-1):
		activation += weights[i + 1] * row[i]
	return 1.0 if activation >= 0.0 else 0.0


# Estimate Perceptron weights using stochastic gradient descent
def train_weights(train, n_epoch):
	weights = [0.0 for i in range(len(train[0]))]
	for epoch in range(n_epoch):
		sum_error = 0.0
		for row in train:
			prediction = predict(row, weights)
			error = row[-1] - prediction
			sum_error += error**2
			weights[0] = weights[0] * error
			for i in range(len(row)-1):
				weights[i + 1] = weights[i + 1] * error * row[i]
		print('>epoch=%d, error=%.3f' % (epoch, sum_error))
	return weights

l_rate = 0
n_epoch = 15
weights = train_weights(dataset,n_epoch)
print(weights)
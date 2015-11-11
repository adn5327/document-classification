import read_training as rtrain

# this function doesn't actually care if bernoulli or not
# that only matters for training
def testdata(test_filename, train_filename, bernoulli):
	train_data = rtrain.read_file(train_filename, bernoulli)


if __name__ == '__main__':
	testdata('spam_detection/test_email.txt', 'spam_detection/train_email.txt', False)


import read_training as rtrain

def testdata(test_filename, train_filename, bernoulli):
	train_data = rtrain.read_file(train_filename, bernoulli)


if __name__ == '__main__':
	testdata('spam_detection/test_email.txt', 'spam_detection/train_email.txt', False)
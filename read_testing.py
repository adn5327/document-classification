import read_training as rtrain
import math
import infrastructure as infra
import operator

def figure_out_class(a, train_data, movie):
	#go to each dictionary
	prob_per_class = list()
	for j in range(len(train_data.dicts)):
		pclass = train_data.num_per_class[j] / (1.0 * sum(train_data.num_per_class))
		cur_total = math.log(pclass)
		cur_dict = train_data.dicts[j]
		for i in range(1,len(a)):
			cur_element = a[i].split(':')
			key = cur_element[0]
			value = cur_element[1]
			if key in cur_dict:
				cur_prob = (cur_dict[key] + 1) / (1.0 * (train_data.total_counts[j] + len(cur_dict)))
				cur_total += math.log(cur_prob)
			else:
				cur_prob = 1 / (1.0 * (train_data.total_counts[j] + len(cur_dict)))
				cur_total += math.log(cur_prob)

		prob_per_class.append(cur_total)
	max_val = max(prob_per_class)
	max_idx = prob_per_class.index(max_val)
	if movie:
		if max_idx == 0:
			return -1
	return max_idx

# this function doesn't actually care if bernoulli or not
# that only matters for training
def testdata(test_filename, train_filename, bernoulli = False, movie = False, num_categories = 2):
	train_data = rtrain.read_file(train_filename, bernoulli, num_categories)
	test_file = open(test_filename, 'r')
	lines = test_file.readlines()

	correct_count = 0
	total_count = 0

	for line in lines:
		total_count+=1
		a = line.split()
		correct_label = int(a[0])
		predicted_label = figure_out_class(a, train_data, movie)

		if correct_label == predicted_label:
			correct_count+=1

	print "Accuracy {0:.5%}".format((correct_count*1.0)/total_count)
	print '\n'

	for i in range(len(train_data.dicts)):
		cur_dict = train_data.dicts[i]
		if i == 0 and movie == True:
			print -1
		else:
			print i
		for j in range(20):
			key = max(cur_dict.iteritems(), key=operator.itemgetter(1))[0]
			print key
			del cur_dict[key]
		print '\n'
	test_file.close()
	print '\n\n\n'


if __name__ == '__main__':

	print 'SPAM DATA SET\n'
	print 'Multinomial'
	testdata('spam_detection/test_email.txt', 'spam_detection/train_email.txt', False, False, 2)
	print 'Bernoulli'
	testdata('spam_detection/test_email.txt', 'spam_detection/train_email.txt', True, False, 2)

	print 'MOVIE DATA SET\n'
	print 'Multinomial'
	testdata('sentiment/rt-test.txt', 'sentiment/rt-train.txt', False, True, 2)
	print 'Bernoulli'
	testdata('sentiment/rt-test.txt', 'sentiment/rt-train.txt', True, True, 2)

	print '8 CATEGORY DATA SET\n'
	print 'Multinomial'
	testdata('8category/8category.testing.txt', '8category/8category.training.txt', False, False, 8)
	print 'Bernoulli'
	testdata('8category/8category.testing.txt', '8category/8category.training.txt', True, False, 8)

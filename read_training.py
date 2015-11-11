import infrastructure as infra

def read_file(filename):
	init_obj = infra.classes(2)
	labels = open(filename)

	lines = labels.readlines()
	count = 0
	for line in lines:
		count+=1
		a = line.split()
		review_num = int(a[0])
		if review_num == -1:
			review_num = 0

		total_cts = init_obj.total_counts
		dict_itself = init_obj.dicts[review_num]


		for i in range(1,len(a)):
			cur_element = a[i].split(':')
			key = cur_element[0]
			value = int(cur_element[1])
			total_cts[review_num]+=value

			if key in dict_itself:
				x = dict_itself[key]
				dict_itself[key] = x + value
			else:
				dict_itself[key] = value

	print init_obj.total_counts

# the challenge here is that:
# 		positive review --> 1
# 		negative review --> -1
#		will zero index the negative review


if __name__ == '__main__':
	read_file('spam_detection/train_email.txt')
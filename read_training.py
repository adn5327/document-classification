import infrastructure as infra

def read_file(filename, bernoulli):
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
		init_obj.num_per_class[review_num] +=1
		
		total_cts = init_obj.total_counts

		if(bernoulli):
			total_cts[review_num] += 1
		
		
		dict_itself = init_obj.dicts[review_num]


		for i in range(1,len(a)):
			cur_element = a[i].split(':')
			key = cur_element[0]
			value = int(cur_element[1])

			# for bernoulli -- values are purely boolean
			# does it exist in the doc or not?
			if(bernoulli):
				value = 1
			else:
				total_cts[review_num]+=value

			if key in dict_itself:
				x = dict_itself[key]
				dict_itself[key] = x + value
			else:
				dict_itself[key] = value
		# print(dict_itself)
	# print(init_obj.total_counts)
	# print(init_obj.num_per_class)
	# print(sum(init_obj.num_per_class))
	labels.close()
	# print(init_obj.dicts[0])
	# print("\n\n\n\n!!!!!!!!!!\n\n\n\n\n")
	# print(init_obj.dicts[1])
	# quit()
	return init_obj

# the challenge here is that:
# 		positive review --> 1
# 		negative review --> -1
#		will zero index the negative review


if __name__ == '__main__':
	read_file('spam_detection/1train.txt', False)
	# read_file('spam_detection/train_email.txt', False)
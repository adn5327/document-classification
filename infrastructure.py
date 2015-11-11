import numpy as np

class classes(object):

	def __init__(self, num_categories):
		self.num_categories = num_categories
		self.total_counts = list()
		self.dicts = list()
		for i in range(num_categories):
			self.dicts.append(dict())
			self.total_counts.append(0)

def main():
	a = classes(2)
	a.dicts[0]['hello'] = 2
	a.dicts[1]['hi'] = 1
	print type(a.dicts[0])
	print a.dicts[1]

if __name__ == '__main__':
	main()
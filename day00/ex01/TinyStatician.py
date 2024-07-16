import math
class TinyStatistician():
	def __init__(self):
		print("start")\

	def means(self,argument):
		if not isinstance(argument, (list, tuple)):
			return None
		if len(argument) == 0 :
			return None
		sum = 0
		for item in argument :
			sum += item
		return sum / len(argument)

	def median(self, argument):
		if not isinstance(argument, (list, tuple)):
			return None
		if len(argument) == 0 :
			return None
		sorted_arg =  sorted(argument)
		n = len(argument)
		mid = n // 2
		if n % 2 == 0:
			return ((sorted_arg[mid] - sorted_arg[mid - 1]) / 2)
		else :
			return sorted_arg[mid]

	def quartile(self, argument):
		if not isinstance(argument, (list, tuple)):
			return None
		if len(argument) == 0:
			return None
		sorted_arg = sorted(argument)
		n = len(argument)
		print(n)
		q1 = n * 0.25
		q3 = n * 0.75
		if int(q1) >= n or int(q3) >= n :
			return None
		return [sorted_arg[int(q1)], sorted_arg[int(q3)]]

	def percentile(self, array, x):
		if not isinstance(array, (list, tuple)) or len(array) == 0:
			return None
		sorted_arg = sorted(array)
		index = (x / 100) * (len(sorted_arg) - 1)
		if index >= len(sorted_arg) :
			return None
		if index.is_integer():
			return float(sorted_arg[int(index)])
		else:
			lower = int(index)
			upper_index = index + 1
			# interpolation = (sorted_arg[upper_index] - sorted_arg[lower] * (index - lower))
			interpolation = sorted_arg[lower] + (sorted_arg[int(upper_index)] - sorted_arg[lower]) * (float(index) - lower)
			print (float(index))
			return float(interpolation)


	def var(self, x):
		if not isinstance(x, (list, tuple)) or len(x) == 0:
			return None
		means = self.means(x)
		variance = sum((value - means) ** 2 for value in x ) / (len(x) - 1)
		return variance

	def std(self, x):
		if not isinstance(x, (list, tuple)) or len(x) == 0:
			return None
		variance = self.var(x)
		return math.sqrt(variance)







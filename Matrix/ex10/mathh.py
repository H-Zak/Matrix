import math
class Matrix:
	def __init__(self, input=None):
		if isinstance(input,list) :
			if not all(isinstance(row, list) for row in input):
				raise ValueError("Input must be a either a list of lists or a tuple for the shape2")
			if not all(len(row) == len(input[0]) for row in input):
				raise ValueError("All the row have not the same length")
			if not all(all(isinstance(item, (int, float)) for item in sublist) for sublist in input ):
				raise ValueError("must be numeric 2")
			self._data = input
			self._shape = (len(input), len(input[0]) if input else 0)
		elif isinstance(input, tuple):
			if not all(isinstance(row, tuple) for row in input):
				raise ValueError("Input must be a either a list of lists or a tuple for the shape2")
			if not all(len(row) == len(input[0]) for row in input):
				raise ValueError("All the row have not the same length")
			if not all(all(isinstance(item, (int, float)) for item in sublist) for sublist in input ):
				raise ValueError("must be numeric 2")
			self._data = input
			self._shape = (len(input), len(input[0]) if input else 0)
		else:
			raise ValueError("Input must be a either a list of lists or a tuple for the shape3")

	@property
	def data(self):
		return self._data

	@data.setter
	def data(self, value):
		if not isinstance(value, list) or not all(isinstance(row, list) for row in value):
			raise ValueError("Matrix must be a list of list")
		self._data = value
		self._shape = (len(value), len(value[0]) if value else 0)

	@property
	def shape(self):
		return self._shape

	@shape.setter
	def shape(self, value):
		if not isinstance(value, tuple):
			raise ValueError("Shape must be a tuple")


	def _add_matrix(self, new):
		data = self._check_list_or_matrix(new)
		create = [[self._data[i][j] + data[i][j]  for j in range(len(self._data[0]))] for i in range(len(self._data))]
		print("\nadd :",create)
		return Matrix(create)

	def __radd__(self, new):
		return self._add_matrix(new)

	def __add__(self, new):
		return self._add_matrix(new)

	def __sub__(self, new):
		data = self._check_list_or_matrix(new)
		create = [[self._data[i][j] - data[i][j]  for j in range(len(self._data[0]))] for i in range(len(self._data))]
		print("\nsub : ", create)
		return Matrix(create)

	def __rsub__(self, new):
		data = self._check_list_or_matrix(new)
		create = [[data[i][j] - self._data[i][j]   for j in range(len(self._data[0]))] for i in range(len(self._data))]
		print("sub : ", create)
		return Matrix(create)


	def _check_list_or_matrix(self, new):
		if isinstance(new, Matrix):
			if self._shape != new._shape:
				raise ValueError("Must have the same shape")
			data = new.data
			return data
		elif isinstance(new, list) and all(isinstance(raw, list) for raw in new):
			data = new
			shape = (len(new), len(new[0]) if new[0] else 0)
			if shape != self._shape:
				raise ValueError("Must have the same shape")
			return data
		else:
			raise ValueError("You must send a Matrix or a list of lists")

	def __truediv__(self, other):
		print(type(other))
		if not isinstance(other, (int, float)):
			raise ValueError("Need an int or float")
		create = [[self._data[i][j] / other for j in range(len(self._data[i]))] for i in range(len(self._data))]
		print("div :", create, "\n")
		return Matrix(create)



	def __rtruediv__(self, other):
		if not isinstance(other, (int, float)):
			raise ValueError("Need an int or float")
		create = [[other / self._data[i][j] for j in range(len(self._data[i]))] for i in range(len(self._data))]
		print("div :", create, "\n")
		return Matrix(create)

	def __mul__(self, other):
		if isinstance(other, (Matrix, Vector)):
			if self._shape[1] != other.shape[0]:
				print(self._shape[1], other.shape[0])
				raise ValueError("number of Matrix1 line should be equal to columm of matrix 2 ()")
			create = [[sum(a * b for a, b in zip(row, col)) for col in zip(*other._data)] for row in self._data]
		elif isinstance(other, (float, int)):
			create = [[other * self._data[i][j] for j in range(len(self._data[i]))] for i in range(len(self._data))]
		else:
			raise ValueError("Must be multiple by a int or a float or a Matrix or a Vector")
		print("mul : ", create)
		return Matrix(create)
	
	def trace(self):
		if not isinstance(self, Matrix) or self.shape[0] != self.shape[1] or self.is_empty():
			raise ValueError("It must be a square of a matrice ")
		return sum(self.data[i][i] for i in range(self.shape[0]))
		
	def __rmul__(self, other):
		if isinstance(other, (Matrix, Vector)):
			if other.shape[1] != self._shape[0] :
				raise ValueError("number of Matrix1 line should be equal to columm of matrix 2")
			create = [[sum(a * b for a, b in zip(row, col)) for col in zip(*self._data)] for row in other._data]
		elif isinstance(other, (float, int)):
			create = [[other * self._data[i][j] for j in range(len(self._data[i]))] for i in range(len(self._data))]
		else:
			raise ValueError("Must be multiple by a int or a float or a Matrix or a Vector")
		print("mul : ", create)
		return Matrix(create)

	def T(self):
		self._data = [list(row) for row in zip(*self._data)]

	def __str__(self):
		result = ""
		for row in self.data:
			row_str = " ".join(str(item) for item in row)
			result += row_str + "\n"
		return result.strip()

	def __repr__(self):
		return f"Matrix({self._data})"
	
	def dot(self, v):
		if type(self) != Vector or type(v) != Vector :
			raise ValueError("Must be vector")
		if self.shape != v.shape:
			raise ValueError("Not the same shape")
		size = self.shape
		result = 0
		for i in range(size[0]):
			for j in range(size[1]):
					result += self.data[i][j] * v.data[i][j]
		return result
	
	def norm_1(self):
		if(isinstance(self, Vector)):
			return sum(abs(x) for sublist in self.data for x in sublist)
		else:
			raise ValueError("Must be a vector")

	def norm_2(self):
		if isinstance(self, Vector):
			return math.sqrt(sum(pow(x , 2) for sublist in self.data for x in sublist))
		else:
			raise ValueError("Must be a Vector")

	
	def normal_inf(self):
		if (isinstance(self, Vector)):
			return max(abs(x) for sublist in self.data for x in sublist)
		else:
			raise ValueError("Must be a vector")
	
	def is_empty(self):
		return all(len(sublist) == 0 for sublist in self.data)

	def transpose(self):
		m ,n = self.shape
		transposed = [[0 for _ in  range(m) ] for _ in range(n) ]
		for i in range(m):
			for j in range(n):
				transposed[j][i] = self.data[i][j]
		return Matrix(transposed)
	
	def row_echelon(self):
		if not isinstance(self, (Vector, Matrix)) :
			raise ValueError("it must be a vector or Matrix")
		if self.is_empty():
			return self
		if self.shape[0] == 1 or self.shape[1] == 1:
			return self
		col = 0
		self.swap_max_first_row()
		for i in range(self.shape[0]):
			while col < self.shape[1] and self.data[i][col] == 0:
				col += 1
			if col >= self.shape[1]:
				continue
			new_i = i
			while (new_i < self.shape[0]):
				divisor = self.data[new_i][col]
				if divisor != 0:
					self.data[new_i] = [x / divisor  for x in self.data[new_i]]
				new_i += 1

			for j in range (i + 1, self.shape[0]):
				if (j < self.shape[0]):
					factor = self.data[j][col]
					self.data[j] = [round(current_row - factor * self.data[i][k], 6) for k, current_row in enumerate(self.data[j])]

		for i in range(self.shape[0] - 1,-1, -1):
			for j in range(self.shape[1]):
				if self.data[i][j] == 1:
					for row in range(i - 1, -1 ,-1):
						if self.data[row][j] != 0:
							factor = self.data[row][j]
							self.data[row] = [round(current_row - factor * self.data[i][k], 6) for k,current_row in enumerate(self.data[row])]
		return self

	def swap_max_first_row(self):
		start = 0
		for j in range(self.shape[1]):
			max_row_index = -1
			row = -1
			for i in range(start, self.shape[0]):
				if self.data[i][j] == 0 and row == -1:
					row = i
				elif self.data[i][j]!= 0:
					max_row_index = i
					break
			if max_row_index != row and max_row_index != -1 and row != -1:
				self.data[row], self.data[max_row_index] = self.data[max_row_index], self.data[row]
			start += 1
	
	def reduced(self):
		for i in range(min(self.shape[0], self.shape[1]-1, -1, -1 )):
			pivot= self.data[i][i]
			







class Vector(Matrix):
	def __init__(self, elements):
		if not elements :
			raise ValueError("The list cannot be empty")
		if isinstance(elements, list):
			# print("here i am")
			if not all(isinstance(row, list) for row in elements):
				raise ValueError("Input must be a either a list of lists or a tuple for the shape2")
			if len(elements) != 1 and any(len(item) != 1 for item in elements):
				raise ValueError("Vector must have only one dimension")
			if all(isinstance(elements, (int, float)) for item in elements):
				raise ValueError("only numeric")
			# print(len(elements), elements )
			super().__init__(elements)
		elif isinstance(elements, tuple):
			if not all(isinstance(row, tuple) for row in elements):
				raise ValueError("Input must be a either a list of lists or a tuple for the shape21")
			if len(elements) != 1 and any(len(item) != 1 for item in elements):
				raise ValueError("Vector must have only one dimension")
			if all(isinstance(elements, (int, float)) for item in elements):
				raise ValueError("only numeric")
			# print(len(elements), elements )
			super().__init__(elements)
		else:
			raise ValueError("vector must be one list or tuple, with at list one value")



		# a verifier, faire la difference entre vecteur ligne et vecteur colonne 
		def dot(self, v):
			# Step 1: Check if the input is a Vector
			if not isinstance(v, Vector):
				raise ValueError("The argument must be an instance of Vector.")

			# Step 2: Check if shapes match
			if self.shape[1] != v.shape[0]:
				raise ValueError("Shapes do not match for dot product.")

			# Step 3: Compute the dot product
			result = sum(a * b for a, b in (zip(row, col) for col in self._data for row in v.data))

			return result








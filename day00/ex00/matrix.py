# je ne gere pas le cas ou 2 vector multiplie entre eux renvoie un Vector et non pas une matrix

class Matrix:
	def __init__(self, input=None):
		print("here", type(input), input)
		if isinstance(input,list) :
			if not all(isinstance(row, list) for row in input):
				raise ValueError("Input must be a either a list of lists or a tuple for the shape2")
			if not all(len(row) == len(input[0]) for row in input):
				raise ValueError("All the row have not the same length")
			self._data = input
			self._shape = (len(input), len(input[0]) if input else 0)
		elif isinstance(input, tuple):
			if len(input) != 2:
				raise ValueError("length of the tuple must be 2")
			self._shape = input
			self._data = [[0.0 for _ in range(input[1])] for _ in range(input[0]) ]
		else:
			raise ValueError("Input must be a either a list of lists or a tuple for the shape3")
		# print(self._data)

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


class Vector(Matrix):
	def __init__(self, elements):
		if isinstance(elements, list):
			if not all(isinstance(row, list) for row in elements):
				raise ValueError("Format issue")
			if len(elements) != 1 and len(elements[0]) != 1 :
				raise ValueError("It's not a vector")
			print(type(elements), elements )
			super().__init__(elements)
		elif isinstance(elements, tuple):
			if len(elements) != 2 or 1 not in elements:
				raise ValueError("Must have only 2 element and one of the valeur must be one ")
			super().__init__(elements)
		else:
			raise ValueError("Input must be a either a list of lists or a tuple for the shape")



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








class Matrix:
	def __init__(self, input=None):

		if isinstance(input,list) :
			if len(input) == 0:
				self._data = []
				self._shape = (0, 0)
				return
			if not all(isinstance(row, list) for row in input):
				raise ValueError("Input must be a either a list of lists or a tuple for the shape2")
			if not all(len(row) == len(input[0]) for row in input):
				raise ValueError("All the row have not the same length")
			if not all(all(isinstance(item, (int, float)) for item in sublist) for sublist in input ):
				raise ValueError("must be numeric 2")
			self._data = input
			self._shape = (len(input), len(input[0]) if input else 0)
		elif isinstance(input, tuple):
			if len(input) == 0:
				self._data = []
				self._shape = (0, 0)
				return
			if not all(isinstance(row, tuple) for row in input):
				raise ValueError("Input must be a either a list of lists or a tuple for the shape2")
			if not all(len(row) == len(input[0]) for row in input):
				raise ValueError("All the row have not the same length")
			if not all(all(isinstance(item, (int, float)) for item in sublist) for sublist in input ):
				raise ValueError("must be numeric 2")
			self._data = [list(row) for row in input]
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

	def _add_matrix(self, new):
		data = self._check_list_or_matrix(new)
		create = [[self._data[i][j] + data[i][j]  for j in range(len(self._data[0]))] for i in range(len(self._data))]
		return Matrix(create)

	def __radd__(self, new):
		return self._add_matrix(new)

	def __add__(self, new):
		return self._add_matrix(new)

	def __sub__(self, new):
		data = self._check_list_or_matrix(new)
		create = [[self._data[i][j] - data[i][j]  for j in range(len(self._data[0]))] for i in range(len(self._data))]
		return Matrix(create)

	def __rsub__(self, new):
		data = self._check_list_or_matrix(new)
		create = [[data[i][j] - self._data[i][j]   for j in range(len(self._data[0]))] for i in range(len(self._data))]
		return Matrix(create)


	def _check_list_or_matrix(self, new):
		if isinstance(new, Matrix):
			if self._shape != new._shape:
				raise ValueError("Must have the same shape")
			return new.data

		elif isinstance(new, list) and all(isinstance(row, list) for row in new):
			data = new

			rows = len(data)
			cols = len(data[0]) if rows > 0 else 0
			shape = (rows, cols)

			if rows > 0 and any(len(row) != cols for row in data):
				raise ValueError("All rows must have the same length")

			if shape != self._shape:
				raise ValueError("Must have the same shape")

			return data

		else:
			raise ValueError("You must send a Matrix or a list of lists")

	def __truediv__(self, other):
		if not isinstance(other, (int, float)):
			raise ValueError("Need an int or float")
		create = [[self._data[i][j] / other for j in range(len(self._data[i]))] for i in range(len(self._data))]
		return Matrix(create)



	def __rtruediv__(self, other):
		if not isinstance(other, (int, float)):
			raise ValueError("Need an int or float")
		create = [[other / self._data[i][j] for j in range(len(self._data[i]))] for i in range(len(self._data))]
		return Matrix(create)

	def __mul__(self, other):
		if isinstance(other, (Matrix, Vector)):
			if self._shape[1] != other.shape[0]:
				raise ValueError("number of Matrix1 line should be equal to columm of matrix 2 ()")
			create = [[sum(a * b for a, b in zip(row, col)) for col in zip(*other._data)] for row in self._data]
		elif isinstance(other, (float, int)):
			create = [[other * self._data[i][j] for j in range(len(self._data[i]))] for i in range(len(self._data))]
		else:
			raise ValueError("Must be multiple by a int or a float or a Matrix or a Vector")
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
		return Matrix(create)

	def T(self):
		self._data = [list(row) for row in zip(*self._data)]
		self._shape = (len(self._data), len(self._data[0]) if self._data else 0)

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
		if not elements :
			raise ValueError("The list cannot be empty")
		if isinstance(elements, list):
			if not all(isinstance(row, list) for row in elements):
				raise ValueError("Input must be a list of lists")
			if len(elements) == 1 and len(elements[0]) >= 1:
				pass
			elif len(elements) >= 1 and all(len(row) == 1 for row in elements):
				pass
			else:
				raise ValueError("Vector must be a row vector (1×n) or column vector (n×1)")
			super().__init__(elements)
		elif isinstance(elements, tuple):
			if not all(isinstance(row, tuple) for row in elements):
				raise ValueError("Input must be a tuple of tuples")
			if len(elements) == 1 and len(elements[0]) >= 1:
				pass
			elif len(elements) >= 1 and all(len(row) == 1 for row in elements):
				pass
			else:
				raise ValueError("Vector must be a row vector (1×n) or column vector (n×1)")
			super().__init__(elements)
		else:
			raise ValueError("vector must be one list or tuple, with at list one value")



	def dot(self, v):
		if not isinstance(v, Vector):
			raise ValueError("The argument must be an instance of Vector.")

		#  Flat les vecteurs
		self_flat = [item for row in self._data for item in row]
		v_flat = [item for row in v._data for item in row]

		# verif dimension
		if len(self_flat) != len(v_flat):
			raise ValueError("Vectors must have the same dimension for dot product.")

		# dot
		result = sum(a * b for a, b in zip(self_flat, v_flat))

		return result

	def norm_1(self):
		return sum(x if x >= 0 else -x for sublist in self.data for x in sublist)

	def norm(self):
		return pow(sum(pow(x , 2) for sublist in self.data for x in sublist), 0.5)

	def norm_inf(self):
		return max(x if x >= 0 else -x for sublist in self.data for x in sublist)


def angle_cos(u, v):
	if not isinstance(u, Vector) or not isinstance(v, Vector):
		raise ValueError("One of the argument is not Vector")
	u_size = u.shape[0] * u.shape[1]
	v_size = v.shape[0] * v.shape[1]
	if u_size != v_size:
		raise ValueError("Vector must have the same dimension")
	if u.norm() == 0 or v.norm() == 0:
		raise ValueError("cannot divide by 0")
	cos = u.dot(v) / (u.norm() * v.norm())
	return cos






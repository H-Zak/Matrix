from mathh import Matrix, Vector

def linear_combination(u, coefs):
	# print(u[0].shape)
	if u:
		shaping = u[0].shape
		if any(shaping != vecteur.shape for vecteur in u ):
			raise ValueError("All vector must have the same shape")
		len_vecteur = shaping[1] if shaping[0] == 1 else shaping[0]
		if (len_vecteur != len(coefs) ):
			raise ValueError("coefs must have the same number of valeur than vector")
		result = Vector([[0.0 for _ in range(shaping[1])] for _ in range(shaping[0])])

		print(result)

		len_1 = 0
		for i in range(shaping[0]):
			for j in range(shaping[1]):
				for z in range(len(u)):
					result.data[i][j] += u[z].data[i][j] * coefs[len_1]
				len_1 += 1
		print(result)	
	else:
		raise ValueError("There is no vector")
		

def main():
	try :
		e1 = Vector([[1., 0., 0.]])
		e2 = Vector([[0., 1., 0.]])
		e3 = Vector([[0., 0., 1.]])
		e4 = Vector([[1], [0], [0]])
		e5 = Vector([[0], [1], [0]])
		e6 = Vector([[0], [0], [1]])
		# linear_combination([e1,e2,e3], [10, -2, 0.5])
		# linear_combination([e4,e5,e6], [10, -2, 0.5])


		v1 = Vector([[1., 2., 3.]])
		v2 = Vector([[0., 10., -100.]])
		linear_combination([v1,v2], [10., -2.])
	except ValueError as e :
		print(e)		



if __name__ == "__main__":
	main()
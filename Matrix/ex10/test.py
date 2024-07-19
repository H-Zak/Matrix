from mathh import Matrix, Vector

def main():
	try :
		e1 = Vector([[4, 2]])
		e2 = Vector([[4], [2]])


		m1 = Matrix([[1., 0], [0, 1]])
		m2 = Matrix([[2,0], [0, 2]])
		m3 = Matrix([[1., 2.],[3., 4.]])
		m4 = Matrix([[-2., -8., 4.],[1., -23., 4.],[0., 6., 4.],])
		m5 = Matrix([[8., 5., -2., 4., 28.],[4., 2.5, 20., 4., -4.], [8., 5., 1., 4., 17.]])


		print(m5.inverse())
		# print(m3.inverse())


		# print(m4.transpose())
		# print(m4.trace())
		# print(m5.trace())

	
	except ValueError as e :
		print(e)		



if __name__ == "__main__":
	main()
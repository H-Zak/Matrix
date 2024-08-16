from mathh import Matrix, Vector


def main():
	try :
		e1 = Vector([[4, 2]])
		e2 = Vector([[4], [2]])


		m1 = Matrix([[1., -1], [-1, 1]])
		m4 = Matrix([[2., 0., 0.],[0., 2., 0.],[0., 0, 2],])
		m3 = Matrix([[8., 5., -2. ],[4., 7, 20], [7., 6., 1.]])
		m5 = Matrix([[8., 5., -2., 4. ],[4., 2.5, 20., 4.],[8., 5., 1.,4], [28., -4., 17.,1]])

		# m5.inverse()
		print(m1.determinant())
		print(m4.determinant())
		print(m5.determinant())
		# print(m3.inverse())


		# print(m4.transpose())
		# print(m4.trace())
		# print(m5.trace())

	
	except ValueError as e :
		print(e)		



if __name__ == "__main__":
	main()
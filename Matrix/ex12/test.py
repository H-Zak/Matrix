from mathh import Matrix, Vector
import pdb
import numpy as np

def main():
	try :
		e1 = Vector([[4, 2]])
		e2 = Vector([[4], [2]])


		m1 = Matrix([[1., -1], [-1, 1]])
		m4 = Matrix([[1, 2., 3.],[0., 1., 4.],[5., 6, 0]])
		m3 = Matrix([[2., 0., 0. ],[0., 3, 0], [0., 0., 4.]])
		m5 = Matrix([[8., 5., -2., 4. ],[4., 2.5, 20., 4.],[8., 5., 1.,4], [28., -4., 17.,1]])
		m6 = Matrix([[8., 5., -2.],[4., 7., 20.],[7., 6., 1.]])
		m7 = Matrix([[8., 5., -2.],[4., 7., 20.],[7., 6., 1.]])
		m8= Matrix([[0.649425287, 0.097701149, -0.655172414],[-0.781609195, -0.126436782, 0.965517241], [0.143678161, 0.074712644, -0.206896552]])
		# m7 = np.array([[8., 5., -2.], [4., 7., 20.], [7., 6., 1.]])
		# m8 = np.array([[0.649425287, 0.097701149, -0.655172414], [-0.781609195, -0.126436782, 0.965517241], [0.143678161, 0.074712644, -0.206896552]])

		# m5.inverse()
		# print(m1.determinant())
		# print(m4.real_inverse())
		print(m6.real_inverse())
		# print(m3.real_inverse())
		# mm = Matrix(m6.real_inverse())
		# mmm = mm * m7
		# print(mmm)


	
	except ValueError as e :
		print(e)		



if __name__ == "__main__":
	main()
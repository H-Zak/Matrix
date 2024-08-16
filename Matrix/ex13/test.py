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
		m8= Matrix([[0.649425287, 0.097701149, -0.655172414],[-0.781609195, -0.126436782, 0.965517241], [0.143678161, 0.074712644, -0.206896552]])

		m6 = Matrix([[1., 0., 0.],[0., 1., 0.],[0, 0., 1.]])
		m7 = Matrix([[1., 2., 0., 0],[2., 4., 0., 0],[-1., 2., 1.,1]])
		m5 = Matrix([[ 8., 5., -2.],[ 4., 7., 20.],[ 7., 6., 1.],[21., 18., 7.],])
		print(m6.rank())
		print(m7.rank())
		print(m5.rank())

	
	except ValueError as e :
		print(e)		



if __name__ == "__main__":
	main()
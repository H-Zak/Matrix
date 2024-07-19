from ex07.mathh import Matrix, Vector

# que se passe t il si vector est vide 
def main():
	try :
		e1 = Vector([[0., 0., 0]])
		e2 = Vector([[1., 2, 3]])
		e3 = Vector([[-1, -2.]])
		e4 = Vector([[1], [1]])
		e5 = Vector([[-1], [6], [0]])
		e6 = Vector([[3], [2], [1]])


		m1 = Matrix([[1., 2.], [3., 4.]])
		m2 = Matrix([[5.,6.], [7., 8.]])

		print("first test e1 :",e1.norm_1(),e1.norm_2(), e1.normal_inf())
		print("second test e2 :",e2.norm_1(),e2.norm_2(), e2.normal_inf())
		print("third test e3 :",e3.norm_1(),e3.norm_2(), e3.normal_inf())

		print("first error test m1 :",m1.norm_1(),m1.norm_2(), m1.normal_inf())
		print("second error test m2 :",m2.norm_1(),m2.norm_2(), m2.normal_inf())

	
	except ValueError as e :
		print(e)		



if __name__ == "__main__":
	main()
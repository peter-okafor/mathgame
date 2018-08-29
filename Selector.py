from MathGame import *
goagain = 1
while goagain == 1:
	ans = input("select a game by entering the number 1 or 2. \n 1) Addition 2) Multiplication\n")
	ans = int(ans)
	if ans==1:
		addition()
	if ans==2:
		multiplication()
	
	print('''Do you want to play again?''')
	print('1) yes 2) no')
	response=input()
	response=int(response)
	
	if response==2 or response!=1:
		print('bye')
		goagain=0
	if response==1:
		print('ok')
		goagain=1

driving = input('請問是否開過車?')
if driving != 'yes' and driving != 'no':
	print('only type yes/no')
	raise SystemExit
age = input('請問年齡?')
age = int(age)
if driving == 'yes':
	if age >= 18:
		print('PASS')
	else:
		print('FAIL')
elif driving == 'no':
	if age >= 18:
		print('可以考駕照')
	else:
		print('還不行考駕照')
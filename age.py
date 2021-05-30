driving = input('請問你有沒有開過車?')
if driving != '有' and driving != '沒有':
	print('只能輸入 有 / 沒有')
	raise SystemExit
	
age = input('請輸入你的年齡: ')
age = int(age)
if driving == '有':
	if age >= 18:
		print('恭喜妳通過驗證')
	else:
		print('你還不能考駕照,怎麼可以開車')
elif driving == '沒有':
	if age >= 18:
		print('你可以考駕照了,怎麼還不去考')
	else:
		print('再過幾年就可以去考駕照了')

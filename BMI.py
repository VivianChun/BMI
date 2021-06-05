w=float(input('Please enter your weight: '))
h=float(input('Please enter your height: '))
BMI= w / (h * h)
if BMI <= 18.5:
	print('過輕')
elif BMI >= 18.5 and BMI < 24:
	print('正常')
elif BMI >= 24 and BMI < 27:
	print('過重')
elif BMI >= 27 and BMI < 30:
	print ('輕度肥胖')
elif BMI >= 30 and BMI < 35:
	print ('中度肥胖')
else:
	print('重度肥胖')
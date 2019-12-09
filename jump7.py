a = 0
for i in range(0,101):
	if i%7==0:
		continue
	elif i%10==7:
		continue
	elif i//10==7:
		continue
	print(i)

password = 'a123456'
x = 3
while x > 0:
	put = input('請輸入密碼: ')
	if put == password:
		print('登入成功')
		break
	elif x == 1:
		print('即將關閉')
		break
	else:
		print('密碼錯誤!還有', x-1, '次機會')
		x = x-1

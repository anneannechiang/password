# 密碼重試程式

# 預設密碼等於 a123456
# 使用者【最多輸入3次密碼】
# 不對的話, 顯示【密碼錯誤, 還有＿次機會】
# 對的話, 顯示【登入成功！】


password = 'a123456'
i = 3

while True:
	pw = input('Enter your password ' )
	if pw == password:
		print('Success Login!!')
		break
	else:
		i = i - 1
		print('Error password!', i ,'chance left! ')
		if i == 0:
			break
		



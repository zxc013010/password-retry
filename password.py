# 密碼重式程式
# password = 'a123456'
# 讓使用者重複輸入密碼
# 最多輸入三次
# 如果正確 印出 "登入成功"
# 如果不正確就印出 "密碼錯誤! 還有__次機會"

password = 'a123456'
i = 3 #剩餘機會
while i > 0:
	i -= 1
	pwd = input('請輸入密碼: ')
	if pwd == password:
		print('登入成功')
		break #逃出迴圈
	else:
		if i > 0:
			print('密碼錯誤! 還有', i, '次機會')
		else:
			print('沒機會嘗試了! 鎖帳號已上鎖啦')
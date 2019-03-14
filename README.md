# selenium-weibo
使用python + selenium模拟登陆微博
环境：windos
Python3.6

用户名和密码
username = "xxxxx"
password = "xxxxx"

def login_weibo():
	driver = webdriver.Chrome()
	#窗口最大化
	driver.maximize_window()
	driver.get('http://www.weibo.com')
	#显示等待
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.presence_of_element_located((By.ID, 'loginname')))
	#登陆
	#输入用户名
	input_name = driver.find_element_by_xpath('//*[@id="loginname"]')
	input_name.send_keys(username)
	#输入密码
	input_passwork = driver.find_element_by_xpath('//input[@type="password"]')
	input_passwork.send_keys(password)
	#点击登陆
	login = driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a')
	time.sleep(5)
	login.click()
	#无论需不需要验证码，src都会有一个值，当有验证码时，值为验证码图片链接，没有验证码时src=“about:blank”
	imgsrc = driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[3]/a/img').get_attribute('src')
	time.sleep(1)
	print(imgsrc)
	#通过正则表达式判断src
	if re.match(r'https://login.sina.com.cn/cgi/pin.php?.*', imgsrc):
		print('需要验证码')	
		identifying_code = True
		while identifying_code:
			code = input("输入验证码：")
			input_code = driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[3]/div/input')
			input_code.send_keys(code)
			time.sleep(1)
			login = driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a')
			time.sleep(5)
			login.click()	
			time.sleep(1)
			login_page = driver.page_source
			#判断验证码输入是否正确
			yes_no = re.compile('span node-type="text">(.*?)</span>', re.S)
			code_yes_no = re.search(yes_no, login_page)
			if not code_yes_no:
				identifying_code = False
			else:
				print(code_yes_no)
	else:
		print('不需要验证码')
	
	driver.close()


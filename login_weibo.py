import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

username = "xxxxx"
password = "xxxxx"
driver = webdriver.Chrome()
driver.maximize_window()

def login_weibo():
	driver.get('http://www.weibo.com')
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.presence_of_element_located((By.ID, 'loginname')))
	input_name = driver.find_element_by_xpath('//*[@id="loginname"]')
	input_name.send_keys(username)
	input_passwork = driver.find_element_by_xpath('//input[@type="password"]')
	input_passwork.send_keys(password)
	login = driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a')
	time.sleep(5)
	login.click()
	imgsrc = driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[3]/a/img').get_attribute('src')
	time.sleep(1)
	print(imgsrc)
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
			yes_no = re.compile('span node-type="text">(.*?)</span>', re.S)
			code_yes_no = re.search(yes_no, login_page)
			if not code_yes_no:
				identifying_code = False
			else:
				print(code_yes_no)
	else:
		print('不需要验证码')
	
	driver.close()
	
	

if __name__ == '__main__':
	login_weibo()
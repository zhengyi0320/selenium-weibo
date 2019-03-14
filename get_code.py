import time
import re
from selenium import webdriver
import tesserocr
from PIL import Image

#截图储存的目录
screenImg = "xxx.png"
driver = webdriver.Chrome()
driver.maximize_window()
#打开一个验证码的url
driver.get('http://my.cnki.net/elibregister/commonRegister.aspx#')
time.sleep(3)
#截取整个网页
driver.get_screenshot_as_file(screenImg)
#定位验证码所在位置
location = driver.find_element_by_id('checkcode').location
size = driver.find_element_by_id('checkcode').size
left = location['x']
top =  location['y']
right = location['x'] + size['width']
bottom = location['y'] + size['height']
time.sleep(1)
#截取验证码图片
img = Image.open(screenImg).crop((left,top,right,bottom))
img.save(screenImg)
image = Image.open(screenImg)
#将图片转化为灰度图像
image = image.convert('L')
#指定二值化阈值
threshold = 150
table = []
for i in range(256):
	if i < threshold:
		table.append(0)
	else:
		table.append(1)
#识别验证码		
image = image.point(table, '1')
result = tesserocr.image_to_text(image)
print(result)	
driver.close()

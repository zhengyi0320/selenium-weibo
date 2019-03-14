import time
import re
from selenium import webdriver
import tesserocr
from PIL import Image

screenImg = "F:/python_test/selenium_weibo/tesserocr/1.png"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://my.cnki.net/elibregister/commonRegister.aspx#')
time.sleep(3)
driver.get_screenshot_as_file(screenImg)
location = driver.find_element_by_id('checkcode').location
size = driver.find_element_by_id('checkcode').size
left = location['x']
top =  location['y']
right = location['x'] + size['width']
bottom = location['y'] + size['height']
time.sleep(1)
img = Image.open(screenImg).crop((left,top,right,bottom))
img.save(screenImg)
image = Image.open(screenImg)
image = image.convert('L')
threshold = 127
table = []
for i in range(256):
	if i < threshold:
		table.append(0)
	else:
		table.append(1)
		
image = image.point(table, '1')
result = tesserocr.image_to_text(image)
print(result)	
driver.close()

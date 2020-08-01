from selenium import webdriver
import time

path = 'D:\實驗爬蟲\chromedriver.exe'
seek = webdriver.Chrome(path)

url = 'https://artsfungo.moc.gov.tw/promote_s/public/store'
seek.get(url)

tag = seek.find_element_by_css_selector('#inpage > div > div > div.row > div:nth-child(1) > div > button')
# for i in tag:
#     if len(i.text):
#         print(i.text)
print(tag.text)
time.sleep(0.5)
tag.click()

tag = seek.find_element_by_css_selector('#inpage > div > div > div.row > div:nth-child(1) > div > div > ul > li:nth-child(2) > a')
time.sleep(0.5)
tag.click()

tag = seek.find_element_by_css_selector('#div-result > div > a > i')
time.sleep(0.5)
tag.click()

time.sleep(2)
tag = seek.find_element_by_css_selector('#inpage > div > div > div.rim > div > table > tbody > tr:nth-child(1) > td:nth-child(2)')
print(tag.text)

# tag = seek.find_element_by_css_selector('#inpage > div > div > div.rim > div > table > tbody')
# tag2 = tag.find_element_by_tag_name('td')
# for i in tag2:
#     if len(i.text):
#         print(i.text)
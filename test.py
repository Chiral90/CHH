import time

# import selenium
from selenium import webdriver # webdriver를 이용해 해당 브라우저를 열기 위해
from selenium.webdriver import ActionChains # 일련의 작업들을(ex.아이디 입력, 비밀번호 입력, 로그인 버튼 클릭...) 연속적으로 실행할 수 있게 하기 위해
from selenium.webdriver.common.keys import Keys # 키보드 입력을 할 수 있게 하기 위해
from selenium.webdriver.common.by import By # html요소 탐색을 할 수 있게 하기 위해
from selenium.webdriver.support.ui import WebDriverWait # 브라우저의 응답을 기다릴 수 있게 하기 위해
from selenium.webdriver.support import expected_conditions as EC # html요소의 상태를 체크할 수 있게 하기 위해
from selenium.webdriver.support.select import Select

# 이 외에도 필요한 모듈이 있다면 따로 호출해준다.

# Importing BeautifulSoup class from the bs4 module
from bs4 import BeautifulSoup

# Importing date
from datetime import date

# Beginning day
bDay = date(2023, 8, 16)
# Get today
today = date.today()

# Opening the html file
HTMLFile = open("target.html", "r", encoding='UTF8')

# Reading the file
index = HTMLFile.read()

# Creating a BeautifulSoup object and specifying the parser
Parse = BeautifulSoup(index, 'html.parser')

# Using the select method
# Prints the second element from the li tag
ol = Parse.find('ol', start=(today - bDay).days, type="1")

lis = ol.find_all('li')

titleText = lis[1].text
contentText = lis[2].text
refText = lis[3].text


contentText = contentText + "\n" + " - " + refText

h1 = Parse.find('h1')
print('제목 : ' + titleText)
print('내용 : ' + contentText)
referece = Parse.find('p', id="75f587b1-2d3f-4705-af73-e9c2c477ab9f")
refereceText = "출처 : 니체, \"" + h1.text + "\", " + referece.text

print(refereceText)


#URL = "https://chimhaha.net"
try:
    dr = webdriver.Chrome("C:/ZTOA/Util/chromedriver-win64/chromedriver-win64/chromedriver.exe")
    dr.get(URL)

    time.sleep(3)

    login = dr.find_element(By.XPATH, "/html/body/header/section[1]/ul/li[2]/a")
    login.click()

    time.sleep(3)

    naverLogin = dr.find_element(By.XPATH, "/html/body/main/div/form/section/a")
    naverLogin.click()

    time.sleep(3)

    id = dr.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/form/ul/li/div/div[2]/div[1]/input")
    id.click()
    id.send_keys("dozos")

    time.sleep(3)

    pw = dr.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/form/ul/li/div/div[2]/div[2]/input")
    pw.click()
    pw.send_keys("Dongjin90!@")

    time.sleep(3)

    naverLoginButton = dr.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/form/ul/li/div/div[8]/button")
    naverLoginButton.click()

    #----
    new = "https://chimhaha.net/recommend_comics/new"

    select = Select(dr.find_element_by_xpath("/html/body/main/article/form/div[1]/div[1]/div[2]/select"))
    select.select_by_value('72')

    time.sleep(1)

    title = dr.find_element_by_xpath("/html/body/main/article/form/div[2]/input")
    title.click()
    title.send_keys(titleText)

    time.sleep(1)

    content = dr.find_element_by_xpath("/html/body/main/article/form/div[3]/div/div[1]/div[2]/div/p")
    content.click()
    content.send_keys(contentText)
except:
    print("error...")


from selenium import webdriver as wd
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

main_url = 'https://21ict.elice.io'
driver = wd.Chrome(executable_path='chromedriver.exe')
driver.get(main_url)
time.sleep(1)

username = 'kangeun@naver.com'
password = os.environ['ictpass']

"""
try:
    element = WebDriverWait(driver, 10).until(
        # 지정한 한 개 요소가 올라오면 웨이트를 종료
        EC.presence_of_element_located((By.CLASS_NAME, "oTravelBox"))
    )
    # 대기 시간 10초, 끝나면 10초 전이라도 실행함.
except Exception as e:
    print('오류 발생', e)
"""

driver.implicitly_wait(10)
user_id_path = driver.find_element_by_xpath('//*[@id="eacc-root"]/div/main/div/div/div[3]/form/div[1]/div/div[2]/input')
user_id_name = user_id_path.get_attribute('id')
element = driver.find_element_by_id(user_id_name)

# clear placeholder string already entered. use below instead .clear() it does not work properly.
from selenium.webdriver.common.keys import Keys
element.send_keys(Keys.CONTROL, 'a')
element.send_keys(Keys.DELETE)

element.send_keys(username)
time.sleep(1)

pass_id_path = driver.find_element_by_xpath(
    '//*[@id="eacc-root"]/div/main/div/div/div[3]/form/div[2]/div/div[1]/div/div[2]/input')
pass_id_name = pass_id_path.get_attribute('id')

driver.find_element_by_id(pass_id_name).send_keys(password)
time.sleep(1)

login_click = driver.find_element_by_xpath('//*[@id="eacc-root"]/div/main/div/div/div[3]/form/button/div')
login_click.click()

mystudy_url = 'https://21ict.elice.io/courses/learn?tab=in_progress'
driver.get(mystudy_url)

# url_all = 'https://21ict.elice.io/courses/15634/lectures/all'
# driver.get(url_all)

chapter_root = 'https://21ict.elice.io/courses/15634/lectures/'
chapter_num = ['129862', '129863']

for lec in chapter_num:
    driver.get(chapter_root+lec)
    time.sleep(1)

driver.close()

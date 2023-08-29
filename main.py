import time
import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# from openpyxl import Workbook
# warnings.filterwarnings('ignore')

SEARCH_KEYWORD = "개발자"
LINK = "https://m.saramin.co.kr/search?searchType=search&searchword="+SEARCH_KEYWORD+"&is_detail_search=y&list_type=unified&page=1"


res = requests.get(LINK+SEARCH_KEYWORD)

options = Options()
options.add_argument("headless")
options.add_experimental_option("excludeSwitches", ["enable-logging"]) #크롬 종료되지 않는 상태 유지

driver = webdriver.Chrome() ## 크롬 드라이버가 위치한 경로 대입 필요
driver.get(LINK) 

time.sleep(2)

driver.find_element(By.XPATH, '//div[@id="list_46427076"]/a').click()  # 회사 링크로 이동
time.sleep(2)
# driver.find_element(By.XPATH, '//*[@id="card_set"]/div[1]/div/section[6]/a').send_keys(Keys.PAGE_DOWN)
# time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="card_set"]/div[1]/div/div[1]/div/span/a').click() # 더보기 이동
time.sleep(1)

corp = driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[1]/div[1]/div[1]/h1').text
sector = driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[1]/div[2]/section/div[2]/div/dl/dd[1]').text
bi = driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[1]/div[2]/section/div[2]/div/dl/dd[3]').text
print(corp, sector, bi)

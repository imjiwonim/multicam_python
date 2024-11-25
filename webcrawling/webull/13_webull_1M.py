from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chrome 옵션 설정
chrome_options = Options()
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

# 웹 드라이버 초기화
driver = webdriver.Chrome(options=chrome_options)
url = "https://www.webull.com/quote/us/gainers/1m"
driver.get(url)

# WebDriverWait으로 데이터 로드 대기
wait = WebDriverWait(driver, 10)
wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.table-body'))
)

# 데이터 추출
TopGainerStockList = []
rows = driver.find_elements(By.CSS_SELECTOR, '.table-body > div')  # 테이블의 모든 행 찾기

for row in rows:
    try:
        no = int(row.find_element(By.CSS_SELECTOR, 'div:nth-child(1)').text)
        name = row.find_element(By.CSS_SELECTOR, 'div:nth-child(2)').text.replace('\n','(')+')'.strip()
        percent_change = row.find_element(By.CSS_SELECTOR, 'div:nth-child(4)').text.replace("+", "").replace("%","").strip()
        last_price = round(float(row.find_element(By.CSS_SELECTOR, 'div:nth-child(5)').text),2)
        high_price = round(float(row.find_element(By.CSS_SELECTOR, 'div:nth-child(6)').text),2)
        low_price = round(float(row.find_element(By.CSS_SELECTOR, 'div:nth-child(7)').text),2)
        volume = row.find_element(By.CSS_SELECTOR, 'div:nth-child(8)').text

        # 데이터 추가
        TopGainerStockList.append([no, name, percent_change, last_price, high_price, low_price, volume])
    except Exception as e:
        print(f"에러 발생: {e}")

# 출력 데이터 확인
for row in TopGainerStockList:
    print(row)

# 드라이버 종료
driver.quit()


import pandas as pd
df_books = pd.DataFrame(TopGainerStockList, columns = ['no','name','percent_change','last_price','high_price','low_price','volume'])
df_books.to_csv('TopGainerStockList.csv', index =False, encoding='utf-8-sig')

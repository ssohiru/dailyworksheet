import streamlit as st

st.header("특수학급 학생들을 위한 매일 학습지 생성기")

st.text("매일 학습지를 만드시나요?")
st.text("이 프로그램이 있으면 학생들을 위한 맞춤형 학습지가 생성됩니다!!")

# 이미지 URL
image_url_1 = "https://drive.google.com/uc?id=1w8CI_1ZwiwKvCrgR08vjglJ710JOFyIZ"
image_url_2 = "https://drive.google.com/uc?id=1hFHElRXYfFWzculdbrSgBfO-IwVWWpz4"
image_url_3 = "https://drive.google.com/uc?id=1aJ_4B9CtWhp5XKAK4j42H6sDN_JN_1yS"
image_url_4 = "https://drive.google.com/uc?id=1KbKRBQaNQxR-f0tpCuYuf9LaYaFQIgwo"

# 이미지를 2x2로 배치
col1, col2 = st.columns(2)

with col1:
    st.image(image_url_1, use_column_width=True)

with col2:
    st.image(image_url_2, use_column_width=True)

col3, col4 = st.columns(2)

with col3:
    st.image(image_url_3, use_column_width=True)

with col4:
    st.image(image_url_4, use_column_width=True)

import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.dates import MO, TU, WE, TH, FR, SA, SU
from datetime import datetime, timedelta
import calendar
import numpy as np
import streamlit as st
import gspread

import streamlit as st

## 달력 관련 함수 정의
def get_calendar_rows_and_columns(year, month, day):
        # 입력받은 년월일을 기준으로 calendar 객체 생성
        cal = calendar.Calendar(firstweekday=6)  # 일요일이 1열이 되도록 firstweekday 설정

        # 해당 월의 모든 날짜를 리스트로 가져옴
        month_days = cal.monthdayscalendar(year, month)
    
        # 첫째 날의 요일 구하기
        first_day_of_month = calendar.weekday(year, month, 1)
    
        # 주어진 날짜의 행과 열 위치 찾기
        row, col = -1, -1
        for i, week in enumerate(month_days):
            for j, weekday in enumerate(week):
                if day == weekday:
                    row, col = i, j

        if row == -1 or col == -1:
            return None  # 유효하지 않은 날짜

        # 출력할 행과 열 숫자 반환
        return row + 1, col + 1

################
# 구글 스프레드 시트랑 연동하기
#pip install google_images_download
import gspread #구글 스프레드 시트

gc = gspread.service_account(filename='C:/Users/sohi9/OneDrive/바탕 화면/specialt.json')
doc = gc.open_by_url("https://docs.google.com/spreadsheets/d/1qhw7uZFqmOqciVHGfbJmtNpNrDj_ZDfuWTWPgeTEBP4/edit?usp=sharing")
worksheet = doc.worksheet("Daily Learning Log")

try:
    worksheet = doc.worksheet("Daily Learning Log")
    print("Found the worksheet!")
except gspread.exceptions.WorksheetNotFound as e:
    print(f"Worksheet not found: {e}")

# Streamlit 앱 설정
st.title("매일학습지 생성기")

# 사용자로부터 학습지 데이터를 입력받음
year = st.slider("년도를 선택하세요", 2000, 2030, 2023)
month = st.slider("월을 선택하세요", 1, 12, 1)
day = st.slider("일자를 선택하세요", 1, 31)
word1 = st.text_input("쓰기 학습 할 단어(1)를 입력하세요. (4글자 이하): ")
word2 = st.text_input("쓰기 학습 할 단어(2)를 입력하세요. (3글자 이하): ")
result = None

###############
message = st.text_input("오늘의 메세지를 입력하세요:")

# 버튼 추가하여 선택한 날짜에 대한 캘린더 표시
if st.button("캘린더 저장 및 달력/식단표 생성"):
     # 년, 월, 일을 입력받음
    year = int(year)
    month = int(month)
    day = int(day)

    result = get_calendar_rows_and_columns(year, month, day)

    if result:
        print("유효한 날짜 입니다.")
        
        # 데이터 쓰기 (월은 D7, E7에, 일자는 B9:H13에 쓰기)
        # D7, E7에 월 데이터 쓰기
        worksheet.update('D7', month)

        # B9:H13 범위의 데이터 비우기
        clear_range = 'B9:H14'
        clear_cells = worksheet.range(clear_range)
        for cell in clear_cells:
            cell.value = ''

        # B9에부터 일자 데이터 쓰기
        start_row, start_col = 9, 2  # B9의 좌표
        rows, cols = 6, 7  # B9부터 H14까지 6행 7열
        c = calendar.TextCalendar(calendar.SUNDAY)
        s = c.formatmonth(year, month)
        first_day_of_month = calendar.weekday(year, month, 1) # 첫째 날의 요일 구하기
        data = s.split('\n')[2:]  # 첫 두 줄은 요일 표시이므로 제외
        for i in range(rows):
            for j in range(cols):
                day_value = i * cols + j - first_day_of_month
                cell_value = str(day_value) if 1 <= day_value <= calendar.monthrange(year, month)[1] else ''
                worksheet.update_cell(start_row + i, start_col + j, cell_value)

        st.write(f"{year}년 {month}월 {day}일의 달력이 스프레드시트에 저장되었습니다. 식단을 저장중입니다...")

    else:
        print("유효하지 않은 날짜입니다.")

    from selenium import webdriver
    import time
    from selenium.webdriver.common.by import By
    import chromedriver_autoinstaller
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import Select
    from selenium.common.exceptions import NoSuchElementException


    chromedriver_autoinstaller.install()

    driver = webdriver.Chrome()

    driver.get("https://konghang.sen.es.kr/20791/subMenu.do")

    time.sleep(2)

    #년월일 지정

    #년도 클릭
    selector_year = "#srhMlsvYear"
    group_navi_year = driver.find_element(By.CSS_SELECTOR, selector_year)
    group_navi_year.click()


    selector_year = "#srhMlsvYear > option:nth-child("+str(year-2016)+")"
    group_navi_year = driver.find_element(By.CSS_SELECTOR, selector_year)
    group_navi_year.click()

    #월 클릭
    selector_month = "#srhMlsvMonth"
    group_navi_month = driver.find_element(By.CSS_SELECTOR, selector_month)
    group_navi_month.click()

    selector_month = "#srhMlsvMonth > option:nth-child("+str(month)+")"
    group_navi_month = driver.find_element(By.CSS_SELECTOR, selector_month)
    group_navi_month.click()

    #선택확인 클릭
    selector_Ok = "#searchForm > div > button"
    group_navi_Ok = driver.find_element(By.CSS_SELECTOR, selector_Ok)
    group_navi_Ok.click()

    time.sleep(2)

    #해당 날짜 점심 클릭 - 해당 날짜에 급식이 없을 경우, 실행 종료
    selector = "#contents_135161 > div.calendar_type01 > div.calendar_box > div > table > tbody > tr:nth-child("+str(result[0])+") > td:nth-child("+str(result[1])+") > ul > li > a"

    try:
        group_navi = driver.find_element(By.CSS_SELECTOR, selector)
        group_navi.click()
    except NoSuchElementException:
        print("해당 날짜에는 급식이 없습니다.")

    time.sleep(1)


    # 점심 메뉴 불러오기
    selector2 = "#detailFrm > table > tbody > tr:nth-child(4) > td"
    group_navi2 = driver.find_element(By.CSS_SELECTOR, selector2)



    ####################
    # 식단데이터 처리

    import re

    ac = str(group_navi2.text)

    # 띄어쓰기를 기준으로 문자열을 리스트로 분할
    list_data1 = ac.split()
    list_data2 = list(filter(lambda item: not item.startswith("("), list_data1))


    # 정규표현식을 사용하여 괄호로 묶인 부분 삭제
    pattern = re.compile(r'\([^)]*\)')  # 괄호로 묶인 부분을 찾는 정규표현식
    filtered_list = [pattern.sub('', item) for item in list_data2]

    # 2차원 리스트로 변환
    values_to_update = [filtered_list]
    print(values_to_update)

    # 워크시트에 입력
    if worksheet.update('B20:H20', values_to_update):
        st.write(f"{year}년 {month}월 {day}일의 식단이 스프레드시트에 저장되었습니다.")

    
import random
def generate_random_problem():
    # 두 개의 한 자리 수 랜덤 생성
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    # 연산자 랜덤 선택
    operator = random.choice(['+', '-', '*', '/'])

    # 음수가 나오지 않도록 조건 추가
    if operator == '-':
        # 뺄셈일 경우 num1이 num2보다 큰 경우로 제한
        num1, num2 = max(num1, num2), min(num1, num2)
    
    return num1, num2

##### 사칙연산 함수정의
def generate_random_minus_problem():
    while True:
        # 두 개의 한 자리 수 랜덤 생성
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        num3 = random.randint(1, 9)
        num4 = random.randint(1, 9)
        
        

         # 뺄셈일 경우 num1이 num2보다 큰 경우로 제한
        num1, num2 = max(num1, num2), min(num1, num2)
        num3, num4 = max(num3, num4), min(num3, num4)

        # 같은 숫자가 나오지 않도록 확인
        if num1 != num2 and num3 != num4 and (num1 != num3 and num2 != num4):
            break
    
    return num1, num2, num3, num4

def generate_random_plus_problem():

    while True:
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        num3 = random.randint(1, 9)
        num4 = random.randint(1, 9)
        num5 = random.randint(1, 9)
        num6 = random.randint(1, 9)

        # 중복 검사
        if (num1, num2) != (num3, num4) and (num1, num2) != (num5, num6) and (num3, num4) != (num5, num6):
            break
    
    return num1, num2, num3, num4, num5, num6

if st.button("오늘의 메세지 입력/사칙연산/시계학습 생성"):
    worksheet.update('E17:H17', message)

    num1, num2, num3, num4 = generate_random_minus_problem()
    worksheet.update('C42',num1)
    worksheet.update('E42',num2)
    worksheet.update('D42',"-")
    worksheet.update('F42',"=")
    worksheet.update('C43',num3)
    worksheet.update('E43',num4)
    worksheet.update('D43',"-")
    worksheet.update('F43',"=")

    num5, num6, num7, num8, num9, num10 = generate_random_plus_problem()
    worksheet.update('C39',num5)
    worksheet.update('E39',num6)
    worksheet.update('D39',"+")
    worksheet.update('F39',"=")
    worksheet.update('C40',num7)
    worksheet.update('E40',num8)
    worksheet.update('D40',"+")
    worksheet.update('F40',"=")
    worksheet.update('C41',num9)
    worksheet.update('E41',num10)
    worksheet.update('D41',"+")
    worksheet.update('F41',"=")

    worksheet.update('B47:C47',random.randint(1, 12))
    worksheet.update('B48:C49',random.choice(['00', '30']))

    st.write("오늘의 메세지, 사칙연산과 시계학습이 스프레드시트에 저장되었습니다.")

# 5. 단어 입력

# word1을 B32:E32에 넣기
if st.button("오늘의 단어 입력"):
    # word1을 B32:E32에 넣기
    for col, char in enumerate(word1, start=2):
        worksheet.update_cell(32, col, char)

    # word2를 F32:H32에 넣기
    for col, char in enumerate(word2, start=6):
        worksheet.update_cell(32, col, char)

    st.write("단어가 스프레드시트에 저장되었습니다.")

st.markdown("[학습지 바로가기](https://docs.google.com/spreadsheets/d/1qhw7uZFqmOqciVHGfbJmtNpNrDj_ZDfuWTWPgeTEBP4/edit?usp=sharing)")

import streamlit as st
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time
import json
import os

import matplotlib.pyplot as plt
from matplotlib.dates import MO, TU, WE, TH, FR, SA, SU
from datetime import datetime, timedelta
import calendar
import numpy as np
import streamlit as st
import gspread

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys 

import os
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import streamlit as st

def show():
    st.title("Settings Page")
    st.write("Welcome to the Settings Page!")
    # 설정 페이지에 필요한 내용을 추가할 수 있습니다.

# Streamlit 애플리케이션 정의
st.title("급식 메뉴와 이미지 다운로더")

# 사용자 입력을 받아옴
year = st.number_input("년도를 선택하세요:", 2016, 2100, step=1)
month = st.number_input("월을 선택하세요:", 1, 12, step=1)
day = st.number_input("일자를 선택하세요:", 1, 31, step=1)

def get_calendar_rows_and_columns(year, month, day):

    # 입력받은 년월일을 기준으로 calendar 객체 생성
    cal = calendar.Calendar(firstweekday=6)  # 일요일이 1열이 되도록 firstweekday 설정

    # 해당 월의 모든 날짜를 리스트로 가져옴
    month_days = cal.monthdayscalendar(year, month)

    # 첫째 날의 요일 구하기
    first_day_of_month = calendar.weekday(year, month, 1)

    # 주어진 날짜의 행과 열 위치 찾기
    row, col = -1, -1
    for i, week in enumerate(month_days):
        for j, weekday in enumerate(week):
            if day == weekday:
                row, col = i, j

    if row == -1 or col == -1:
        return None  # 유효하지 않은 날짜

    # 출력할 행과 열 숫자 반환
    return row + 1, col + 1

result = get_calendar_rows_and_columns(year, month, day)


# 버튼을 눌러 크롤링 시작
if st.button("입력 날짜의 급식 메뉴 및 이미지 다운로드"):
   
    ## 2. 급식 크롤링
    chromedriver_autoinstaller.install()

    driver = webdriver.Chrome()

    driver.get("https://konghang.sen.es.kr/20791/subMenu.do")

    time.sleep(2)

    #년월일 지정

    #년도 클릭
    selector_year = "#srhMlsvYear"
    group_navi_year = driver.find_element(By.CSS_SELECTOR, selector_year)
    group_navi_year.click()


    selector_year = "#srhMlsvYear > option:nth-child("+str(year-2016)+")"
    group_navi_year = driver.find_element(By.CSS_SELECTOR, selector_year)
    group_navi_year.click()

    #월 클릭
    selector_month = "#srhMlsvMonth"
    group_navi_month = driver.find_element(By.CSS_SELECTOR, selector_month)
    group_navi_month.click()

    selector_month = "#srhMlsvMonth > option:nth-child("+str(month)+")"
    group_navi_month = driver.find_element(By.CSS_SELECTOR, selector_month)
    group_navi_month.click()

    #선택확인 클릭
    selector_Ok = "#searchForm > div > button"
    group_navi_Ok = driver.find_element(By.CSS_SELECTOR, selector_Ok)
    group_navi_Ok.click()

    time.sleep(2)

    #해당 날짜 점심 클릭 - 해당 날짜에 급식이 없을 경우, 실행 종료
    selector = "#contents_135161 > div.calendar_type01 > div.calendar_box > div > table > tbody > tr:nth-child("+str(result[0])+") > td:nth-child("+str(result[1])+") > ul > li > a"

    try:
        group_navi = driver.find_element(By.CSS_SELECTOR, selector)
        group_navi.click()
    except NoSuchElementException:
        print("해당 날짜에는 급식이 없습니다.")

    time.sleep(1)


    # 점심 메뉴 불러오기
    selector2 = "#detailFrm > table > tbody > tr:nth-child(4) > td"
    group_navi2 = driver.find_element(By.CSS_SELECTOR, selector2)

    ####################
    # 식단데이터 처리

    import re

    ac = str(group_navi2.text)

    # 띄어쓰기를 기준으로 문자열을 리스트로 분할
    list_data1 = ac.split()
    list_data2 = list(filter(lambda item: not item.startswith("("), list_data1))


    # 정규표현식을 사용하여 괄호로 묶인 부분 삭제
    pattern = re.compile(r'\([^)]*\)')  # 괄호로 묶인 부분을 찾는 정규표현식
    filtered_list = [pattern.sub('', item) for item in list_data2]

    # 2차원 리스트로 변환
    values_to_update = [filtered_list]
    print(values_to_update)

    # 워크시트에 입력
    # if worksheet.update('B20:H20', values_to_update):
    #    st.write(f"{year}년 {month}월 {day}일의 식단이 스프레드시트에 저장되었습니다.")

    time.sleep(1)

    # 점심 메뉴 가져오기
    selector2 = "#detailFrm > table > tbody > tr:nth-child(4) > td"
    group_navi2 = driver.find_element(By.CSS_SELECTOR, selector2)

    import re
    import os
    import urllib.request
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context

    # 이미지를 저장할 폴더 생성
    img_folder = 'imgs/'
    os.makedirs(img_folder, exist_ok=True)

   # 이미지 다운로드 및 저장
    for idx, searchKey in enumerate(values_to_update[0], start=1):
        driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
        elem = driver.find_element("name", "q")
        elem.send_keys(searchKey)
        elem.send_keys(Keys.RETURN)

        SCROLL_PAUSE_TIME = 1
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSE_TIME)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                try:
                    driver.find_element(By.CSS_SELECTOR, ".mye4qd").click()
                except:
                    break
            last_height = new_height

        images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")
        count = 1
        max_images = 2  # 각 메뉴당 2개의 이미지만 다운로드
        for image in images[:max_images]:
            try:
                image.click()
                time.sleep(0.5)

                imgUrl = driver.find_element(
                    By.XPATH,
                    '//*[@id="Sva75c"]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div/div[3]/div[1]/a/img[1]'
                ).get_attribute("src")

                print(f"Download URL: {imgUrl}")

                # 이미지 저장 폴더 열기 (Windows)
                if os.name == 'nt':
                    img_folder_absolute = 'C:/Users/sohi9/OneDrive/바탕 화면/test/imgs/'
                    os.startfile(img_folder_absolute)

                img_filename = f"{year}_{month}_{day}_{idx}_{count}.jpg"
                img_path = os.path.join(img_folder_absolute, img_filename)

                opener = urllib.request.build_opener()
                opener.addheaders = [
                    ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')
                ]
                urllib.request.install_opener(opener)
                urllib.request.urlretrieve(imgUrl, img_path)
                count += 1
                print(f"{year}년 {month}월 {day}일의 {idx}번째 메뉴 이미지를 저장했습니다.")

            except Exception as e:
                print('e : ', e)
                pass

    # 브라우저 닫기
    driver.quit()

    # 결과를 Streamlit 화면에 표시
    st.success(f"{year}년 {month}월 {day}일의 급식 메뉴 및 이미지 다운로드가 완료되었습니다.")

    






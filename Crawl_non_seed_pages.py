import urllib.request
from bs4 import BeautifulSoup
from lxml import html
import requests
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait


def crawl_url(my_urls):
    start_time = time.time()

    list_of_data = []

    with open('Data/Metadata.txt', 'r') as file:
        webdriver_chrome = file.read().rsplit('\n')[0]
        # print('webdriver_chrome : ', webdriver_chrome)
    driver = webdriver.Chrome(
        executable_path=webdriver_chrome)

    # with webdriver.Chrome() as driver:
    #     wait = WebDriverWait(driver, 10)

    # driver = webdriver.Chrome(
    #     executable_path=r"C:\ProgramData\chocolatey\bin\chromedriver.exe")
    driver.get(my_urls)
    html = driver.page_source
    soup = BeautifulSoup(html)
    for tag in soup.find_all('div'):
        if tag not in list_of_data:
            list_of_data.append(str(tag))
    initialed_data = []
    for item in list_of_data:
        new_item = item.split('\n')
        for term in new_item:
            initialed_data.append(term)
    try:
        comment = get_comment(initialed_data)
    except:
        f = open('Data/Failed Crawled Iran Hotels Data.csv', 'a', encoding='utf-8')
        f.write(
            '\n' + str(my_urls))
        f.close()
        comment = []

    driver.close()
    print("--- %s seconds ---" % (time.time() - start_time))
    return comment


def get_comment(list_of_data):
    comment = {}
    not_iterated = []
    for i in range(len(list_of_data)):
        if '<span class="subject-review">' in list_of_data[i]:
            comm = ""
            flag = 0
            counter = i + 4
            while flag == 0:
                if '</p>' not in list_of_data[counter]:
                    comm = comm + list_of_data[counter]
                    counter += 1
                else:
                    flag = 1
            comm = str(comm.split('   ')[-1])
            if list_of_data[i] not in not_iterated:
                not_iterated.append(list_of_data[i])
                subject = list_of_data[i].split('"subject-review">')[1].split('</span>')[0]
                score = list_of_data[i - 1].split('"score-badge">')[1].split('</span>')[0].split(' ')[0]
                comment_time = list_of_data[i - 6].split('<label>')[1].split('</label>')[0].split('تاریخ درج نظر : ')[1]
                stay_duration = \
                    list_of_data[i - 13].split('<label>')[1].split('</label>')[0].split(' شب اقامت  ')[0]
                permanent_residence = list_of_data[i - 17].split('<label>')[1].split('</label>')[0]
                travel_type = list_of_data[i - 21].split('<label>')[1].split('</label>')[0]
                enter_time = \
                    list_of_data[i - 30].split('date-review">')[1].split('</span')[0].split('ورود')[1].split(': ')[1]
                comment[i] = {'comment': comm, 'subject': subject, 'user_score': score, 'comment_time': comment_time,
                              'stay_duration': stay_duration, 'permanent_residence': permanent_residence,
                              'travel_type': travel_type, 'enter_time': enter_time}
    return comment

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
        comment, flag_end = get_comment(initialed_data)
    except:
        f = open('Data/Failed Crawled Iran Hotels Data.csv', 'a', encoding='utf-8')
        f.write(
            '\n' + str(my_urls))
        f.close()
        comment = []

    driver.close()
    print("--- %s seconds ---" % (time.time() - start_time))
    return comment, flag_end


def get_comment(list_of_data):
    comment = {}
    not_iterated = []
    num_of_comments = 0
    flag_end = 0
    flag_empty_page = 1
    for i in range(len(list_of_data)):
        if '<span id="ctl00_ContentPlaceHolder1_sp1"><nav><ul class="pagination">' in list_of_data[
            i] and ' title="صفحه بعد"' not in list_of_data[i]:
            flag_end = 1
            flag_empty_page = 0
        elif '<span class="subject-review">' in list_of_data[i]:
            flag_empty_page = 0
            comm = ""
            flag = 0
            counter = i + 4
            while flag == 0:
                if '</p>' not in list_of_data[counter] and list_of_data[counter] != '':
                    comm = comm + list_of_data[counter]
                    counter += 1
                    # print(list_of_data[counter - 1])
                    # print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
                else:
                    # print(list_of_data[counter - 1])
                    # print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
                    flag = 1
            comm = str(comm.split('   ')[-1])
            # print('list of data : ')
            # print(list_of_data[i])

            if comm not in not_iterated:
                # print(list_of_data[i])
                num_of_comments += 1
                not_iterated.append(comm)
                subject = list_of_data[i].split('"subject-review">')[1].split('</span>')[0]
                # print(subject)
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
    # print('num_of_comments : ', num_of_comments)
    # print(comment)
    # print(flag_end)
    if flag_empty_page == 1:
        flag_end = 1
    return comment, flag_end

# crawl_url('https://www.iranhotelonline.com/yazd-hotels/%D9%87%D8%AA%D9%84-%D8%AF%D8%A7%D8%AF/%D9%86%D8%B8%D8%B1%D8%A7%D8%AA/?p=3')

# crawl_url('https://www.iranhotelonline.com/yazd-hotels/%D8%A7%D9%82%D8%A7%D9%85%D8%AA%DA%AF%D8%A7%D9%87-%D8%B3%D9%86%D8%AA%DB%8C-%D9%BE%D8%A7%D8%B1%D8%B3%DB%8C%DA%A9/%D9%86%D8%B8%D8%B1%D8%A7%D8%AA/?p=1')

# crawl_url('https://www.iranhotelonline.com/yazd-hotels/%D9%87%D8%AA%D9%84-%D8%A2%D9%88%D8%A7%D8%B3%D8%A7/%D9%86%D8%B8%D8%B1%D8%A7%D8%AA/')


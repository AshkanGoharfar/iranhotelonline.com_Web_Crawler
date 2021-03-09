import pandas as pd
from Crawl_non_seed_pages import *

df = pd.read_csv('Data/Seed_pages.csv')

# category -> comment_page_url

f = open('Data/Iran Hotels Data.csv', 'w+')
f.write('hotel,city,subject,comment_time,enter_time,stay_duration,permanent_residence,travel_type,comment,user_score,')

f.close()

# print(df)
for i in range(len(df['comment_page_url'])):
    # print(df['comment_page_url'][i])
    comment = crawl_url(df['comment_page_url'][i])
    print(comment)
    for key in comment:
        f = open('Data/Iran Hotels Data.csv', 'a', encoding='utf-8')
        # f.write('hotel,city,subject,time,comment,user_score')
        f.write('\n' + str(df['hotel'][i]) + ',' + str(df['city'][i]) + ',' + str(comment[key]['subject']) + ',' + str(
            comment[key][
                'comment_time']) + ',' + str(comment[key]['enter_time']) + ',' + str(
            comment[key]['stay_duration']) + ',' + str(comment[key]['permanent_residence']) + ',' + str(
            comment[key]['travel_type']) + ',' + str(comment[key]['comment']) + ',' + str(comment[key]['user_score']))
        f.close()
        # 'comment': comm, 'subject': subject, 'user_score': score, 'time': time
    # f.close()

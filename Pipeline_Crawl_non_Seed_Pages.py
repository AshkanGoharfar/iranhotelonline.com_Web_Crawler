import sys

import pandas as pd
from Crawl_non_seed_pages import *
import multiprocessing


# multi-processing

# split a list into evenly sized chunks
def chunks(l, n):
    return [l[i:i + n] for i in range(0, len(l), n)]


def do_job(job_id, data_slice):
    for comment_url in data_slice:
        print(comment_url)
        crawl_comment_page(comment_url)


def dispatch_jobs(data, job_number):
    total = len(data)
    chunk_size = total / job_number
    slice = chunks(data, int(chunk_size))
    jobs = []
    for i, s in enumerate(slice):
        j = multiprocessing.Process(target=do_job, args=(i, s))
        jobs.append(j)
    for j in jobs:
        j.start()


def crawl_comment_page(comment_detail):
    all_comments = []
    flag_end_pages = 0
    page_counter = 1
    while flag_end_pages == 0:
        comment = crawl_url(comment_detail[0] + '?p=' + str(page_counter))
        if comment:
            page_counter += 1
            if len(comment) < 19:
                flag_end_pages = 1
            for key in comment:
                if comment[key]['comment'] not in all_comments:
                    f = open('Data/Iran Hotels Data.csv', 'a', encoding='utf-8')
                    for item in comment[key]:
                        if comment[key][item] == '':
                            comment[key][item] = 'NaN'
                    f.write(
                        '\n' + str(comment_detail[1]) + ',' + str(comment_detail[2]) + ',' + str(
                            comment[key]['subject']) + ',' + str(
                            comment[key][
                                'comment_time']) + ',' + str(comment[key]['enter_time']) + ',' + str(
                            comment[key]['stay_duration']) + ',' + str(comment[key]['permanent_residence']) + ',' + str(
                            comment[key]['travel_type']) + ',' + str(comment[key]['comment']) + ',' + str(
                            comment[key]['user_score']) + ',' + str(comment_detail[3]))
                    f.close()
                    all_comments.append(comment[key]['comment'])
                else:
                    flag_end_pages = 1


def run_non_seed_pipeline(num_of_threads):
    if __name__ == "__main__":
        print('num_of_threads : ', num_of_threads)

        df = pd.read_csv('Data/Seed_pages.csv')
        # category -> comment_page_url

        # f = open('Data/Iran Hotels Data.csv', 'w+')
        # f.write(
        #     'hotel,city,subject,comment_time,enter_time,stay_duration,permanent_residence,travel_type,comment,user_score,hotel_star')
        # f.close()
        #
        # f = open('Data/Failed Crawled Iran Hotels Data.csv', 'w+', encoding='utf-8')
        # f.write('url')
        # f.close()

        comments_urls = list(zip(df['comment_page_url'], df['hotel'], df['city'], df['hotel_star']))
        comments_urls = comments_urls[:len(comments_urls) - len(comments_urls) % num_of_threads]
        dispatch_jobs(comments_urls, num_of_threads)


if __name__ == '__main__':
    with open('Data/Metadata.txt', 'r') as file:
        num_of_threads = int(file.read().rsplit('\n')[1])
    # num_of_threads = 2
    run_non_seed_pipeline(num_of_threads)

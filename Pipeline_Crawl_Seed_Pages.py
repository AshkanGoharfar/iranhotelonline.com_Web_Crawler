import multiprocessing

from Crawl_seed_pages import *
import sys


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


def run_seed_pipeline(num_of_threads):
    if __name__ == "__main__":
        cities = crawl_seeds()
        cities = cities[:len(cities) - len(cities) % num_of_threads]
        dispatch_jobs(cities, num_of_threads)


if __name__ == '__main__':
    with open('Data/Metadata.txt', 'r') as file:
        num_of_threads = int(file.read().rsplit('\n')[1])
        # num_of_threads = 10
        run_seed_pipeline(num_of_threads)

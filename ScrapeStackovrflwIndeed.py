import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import csv
import wget
import os

if os.path.exists("OverallStackOverFlowStats.csv"):
    os.remove("OverallStackOverFlowStats.csv")
if os.path.exists("StackOverFlowStatsByYear.csv"):
    os.remove("StackOverFlowStatsByYear.csv")
if os.path.exists("StackOverFlowStatsByYearTemp.csv"):
    os.remove("StackOverFlowStatsByYearTemp.csv")
technology_stack = []
YearWiseli = []
url = 'https://data.stackexchange.com/stackoverflow/csv/1575412'
wget.download(url, 'OverallStackOverFlowStats.csv')
with open('OverallStackOverFlowStats.csv', 'r') as file:
    reader = csv.reader(file)
    file_rcd_cnt = 0
    tech_cnt = 0
    for row in reader:
        file_rcd_cnt += 1
        if file_rcd_cnt == 1:
            continue
        tech = row[1]
        classification = row[0]
        technology_stack.append(tech)
        if classification == 'Programming Lang':
            tech_cnt += 1
            if tech_cnt == 10:
                break
url = 'https://data.stackexchange.com/stackoverflow/csv/1575269'
wget.download(url, 'StackOverFlowStatsByYearTemp.csv')
with open('StackOverFlowStatsByYearTemp.csv', 'r') as file:
    reader = csv.reader(file)
    file_rcd_cnt = 0
    tech_cnt = 0
    for row in reader:
        file_rcd_cnt += 1
        if file_rcd_cnt == 1:
            continue
        if row[2] in technology_stack:
            YearWiseli.append(row)
        else:
            continue
with open('StackOverFlowStatsByYear.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(YearWiseli)
data_row_li = []
addr_li = [{'country': 'USA', 'addr': 'https://www.indeed.com'}, {'country': 'Canada', 'addr': 'https://ca.indeed.com'},
           {'country': 'Australia', 'addr': 'https://au.indeed.com'},
           {'country': 'Singapore', 'addr': 'https://sg.indeed.com'},
           {'country': 'United Kingdom', 'addr': 'https://www.indeed.co.uk'},
           {'country': 'India', 'addr': 'https://www.indeed.co.in'}]
for tech in technology_stack:
    for web_addr_dict in addr_li:
        country = web_addr_dict['country']
        web_addr = web_addr_dict['addr']
        web_page_counter = 0
        prev_page_count = 0
        job_count = None
        print(country, tech)
        while True:
            start_param = web_page_counter * 10
            URL = f"{web_addr}/jobs?q={tech}&start={start_param}"
            # conducting a request of the stated URL above:
            page = requests.get(URL)
            # specifying a desired format of “page” using the html parser - this allows python to read the various components of the page, rather than treating it as one long string.
            soup = BeautifulSoup(page.text, "html.parser")
            # printing soup in a more structured tree format that makes for easier reading
            # print(soup.prettify())

            for x in soup.find_all(name="div", attrs={"id": "searchCountPages"}):
                if web_page_counter == 0:
                    job_count = x.contents[0].strip().split('of')[-1].strip().split('jobs')[0].replace(',', '')
                page_count = int(x.contents[0].strip().split('of')[0].strip().split(' ')[1])
            if job_count is None:  # If no jobs found
                break

            if prev_page_count >= page_count:
                break
            for div in soup.find_all(name="div", attrs={"class": "sjcl"}):
                for a in div.find_all(name="div", attrs={"class": "recJobLoc"}):
                    job_loc = a["data-rc-loc"]
                    data_row_li.append([classification,tech, country, job_count.strip(), job_loc])
            prev_page_count = page_count
            web_page_counter += 1

with open('IndeedJobPostings.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter='|')
    writer.writerows(data_row_li)

os.remove("StackOverFlowStatsByYearTemp.csv")

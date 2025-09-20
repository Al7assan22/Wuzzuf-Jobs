import bs4 
import requests
import os
import pandas as pd
import urllib.parse
import dateparser 
from bs4 import BeautifulSoup as bs

jobs_name=["Data analyst","Data Engineer","Ai Engineer"]

job_titles,job_links,companies,companies_links,Employment_Types,work_locations,locations=[],[],[],[],[],[],[]

for job_name in jobs_name:
    job_name_URL=urllib.parse.quote(job_name)

    for i in range(0,15) :

        URL=f'https://wuzzuf.net/search/jobs/?a=hpb&q={job_name_URL}&start={i}'
        print(URL)

        response=requests.get(URL)
        soup=bs(response.content,'html.parser')

        containers=soup.find_all("div",class_="css-ghe2tq e1v1l3u10")

        for container in containers:
            job_title=container.find("h2",class_="css-193uk2c")
            job_titles.append(job_title.text.strip())

            job_link = container.find("h2",class_="css-193uk2c").find("a")
            job_links.append(job_link['href'])

            company=container.find("div",class_="css-1k5ee52").find("a")
            companies.append(company.text.strip())

            company_links=container.find("div",class_="css-1k5ee52").find("a")
            companies_links.append(company_links.get('href'))

            employment_type = container.find("span", {"class": "css-uc9rga"})
            Employment_Types.append(employment_type.text.strip() if employment_type else None)

            work_location = container.find("span", {"class": "css-uofntu"})
            work_locations.append(work_location.text.strip() if work_location else None)

            location=container.find("span",class_="css-16x61xq")
            locations.append(location.text.strip())


file_name = r"C:\Users\AL HASSAN\OneDrive\Desktop\Pyth\Wuzzuf_jobs.csv"
df=pd.DataFrame({
    'job_titles':job_titles,
    'job_links':job_links,
    'companies':companies,
    'companies_links':companies_links,
    'Employment_Types':Employment_Types,
    'work_locations':work_locations,
    'locations':locations
})

if not os.path.exists(file_name):
    df.to_csv(file_name, index=False, encoding='utf-8-sig')
else:
    df_old = pd.read_csv(file_name, encoding='utf-8-sig')
    df_new = df[~df['job_links'].isin(df_old['job_links'])]
    if not df_new.empty:
        df_new.to_csv(file_name, index=False, encoding='utf-8-sig', mode='a', header=False)

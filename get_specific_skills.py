from bs4 import  BeautifulSoup
import requests
import pandas as pd
import csv


def find_jobs():
    html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Data+Analyst&txtLocation=india&cboWorkExp1=0").text
    soup = BeautifulSoup(html_text,'lxml')
    jobs =  soup.find_all('li', class_= 'clearfix job-bx wht-shd-bx')
    data = []
    for job in jobs:
        published_date = job.find('span', class_= 'sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace('  ','')
            skills =job.find('span',class_='srp-skills').text.replace('  ','')
            more_info = job.header.h2.a['href']
            for skill in familiar_skills:
                if skill in skills:
                    data.append([company_name.strip(),skills.strip(),more_info.strip()])
    # Converting and saving the data into a csv format
    dframe = pd.DataFrame(data,columns=['company Name', 'Skills', 'Link'])
    # Modify the 'Link' column to include clickable links
    dframe['Link'] = dframe['Link'].apply(lambda x: f'=HYPERLINK("{x}", "Link to more info")')

    # Specify the CSV file path
    csv_file = 'Current_analyst_jobs_specific_skills.csv'

    # Save the DataFrame to the CSV file
    dframe.to_csv(csv_file, index=False, quoting=csv.QUOTE_ALL)
    print('All done. check csv file for results')

# Taking input from the user
Numberofskills = int(input("put the number of skills you want to crosscheck : "))
familiar_skills = []
for i in  range(Numberofskills):
    skills = input('> ')
    familiar_skills.append(skills)
print('Cross checking skils ...')

# running the function
find_jobs()





















from bs4 import  BeautifulSoup
import requests
import pandas as pd
import csv

def find_jobs(job_title, search_location, work_experience):
    job_title_encoded = '+'.join(job_title.split())
    print(f"Searching for {job_title_encoded} jobs in {search_location} with {work_experience} years of experience...")

    data = []
    page = 1
    while True:
        print(f"Fetching page {page}...")

        url = f"https://www.timesjobs.com/candidate/job-search.html"
        params = {
                "searchType": "personalizedSearch",
                "from": "submit",
                "postWeek": "7",                  # Show only jobs from the last 7 days
                "pDate": "I",                     # Internal flag for TimesJobs to apply date filter
                "luceneResultSize": "500",        # Page size (25 jobs)
                "txtKeywords": job_title_encoded,
                "txtLocation": search_location,
                "cboWorkExp1": work_experience,
                "startPage": page
            }

        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        # print("Requesting full url with params:", url + str(params))
        response = requests.get(url, params=params, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
        # print("found some jobs:", jobs)
        jobs_count = 0
        print(f"Found {len(jobs)} jobs on page {page}...")
        # for job in jobs:
        for job in jobs:
            jobs_count += 1
            print(f"Processing job {jobs_count } on page {page}...")
            job_title_tag = job.find('h2', class_='heading-trun')
            job_title_clean = job_title_tag['title'].strip() if job_title_tag else 'N/A'
            link_tag = job_title_tag.find('a') if job_title_tag else None
            job_link = link_tag['href'].strip() if link_tag else 'N/A'

            company_name_tag = job.find('h3', class_='joblist-comp-name')
            company_name = company_name_tag.text.strip() if company_name_tag else 'N/A'

            posted_tag = job.find('span', class_='sim-posted')
            posted_date = posted_tag.span.text.strip() if posted_tag and posted_tag.span else 'N/A'

            # Extract skills
            skills_div = job.find('div', class_='more-skills-sections')
            if skills_div:
                skills = [span.text.strip() for span in skills_div.find_all('span')]
                skills_text = ', '.join(skills)
            else:
                skills_text = 'N/A'

            # Extract job description
            desc_li = job.find('li', class_='job-description__')
            job_description = desc_li.text.strip() if desc_li else 'N/A'

            # Extract location, experience, salary
            top_details = job.find_all('li')
            location = experience = salary = 'N/A'
            for li in top_details:
                icon = li.find('i')
                if icon:
                    class_list = icon.get('class', [])
                    if 'location' in class_list:
                        location = li.text.strip()
                    elif 'experience' in class_list:
                        experience = li.text.strip()
                    elif 'salary' in class_list:
                        salary = li.text.strip()

            data.append([
                job_title_clean, company_name, job_link, posted_date,
                location, experience, salary, skills_text, job_description
            ])
       
        page += 1  # move to next page
        if len(jobs) < 25:
            print(f"Less than 25 jobs found on page {page - 1}. Stopping search.")
            break
    # Convert to DataFrame
    df = pd.DataFrame(data, columns=[
        'Job Title', 'Company Name', 'Job Link', 'Posted Date',
        'Location', 'Experience', 'Salary', 'Skills', 'Description'
    ])

    # Make clickable links
    df['Job Link'] = df['Job Link'].apply(lambda x: f'=HYPERLINK("{x}", "Apply Now")')

    # Save to CSV
    csv_file = f'csv_files/{job_title_encoded}_{search_location}_{work_experience}_all_pages.csv'
    df.to_csv(csv_file, index=False, quoting=csv.QUOTE_ALL)
    print(f'All done. Saved {len(df)} jobs to {csv_file}')


def main():
    job_title = 'Data Analyst'
    location = 'India'
    work_experience = '3'
    # print(f"Searching for {job_title} jobs in {location} with {work_experience} years of experience...")

    find_jobs(job_title, location, work_experience)


if __name__ == "__main__":
    main()























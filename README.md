
# 💼 Job Listings Webscraper

This project is a Python-based web scraper designed to collect and organize job listings from online job portals. It extracts key information such as job title, company, location, and summary, making it easier to analyze or filter openings based on user preferences.

## 📌 Features

- Scrapes job listings from a targeted website (e.g., Indeed, LinkedIn)
- Extracts:
  - Job title
  - Company name
  - Location
  - Job link
- Saves data in a structured format (e.g., CSV)
- Designed for easy extension or automation

## 🔧 Tech Stack

- **Python**
- **BeautifulSoup** for HTML parsing
- **CSV** for data export

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Samuel-Muchai-Kuria/Webscaping-project-for-jobs.git
   cd Webscaping-project-for-jobs
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the scraper:
   ```bash
   python get_all_skills.py
   ```
   or 
   ```
   python get_specific_skills.py
   ```

4. View results:
   - Output is saved to a `.csv` file in the project directory.

## 📝 Notes

- This is a learning project focused on web scraping basics and job data automation.
- Can be extended with filters, email alerts, or integration into dashboards.


## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

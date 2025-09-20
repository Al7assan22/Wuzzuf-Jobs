
# 🕸️ Wuzzuf Jobs Web Scraping & Analysis

## 📌 Project Overview
This project showcases my experience with **Web Scraping, Data Cleaning, and Automation**.  
I built a Python script to scrape job postings from **[Wuzzuf](https://wuzzuf.net)**, store them in a structured CSV file, and then analyzed the data as a Data Analyst.  

The idea started with curiosity about job market trends in Egypt. Instead of manually browsing, I automated the process to collect and analyze job postings in one place.

---

## ⚙️ Tools & Libraries
- **requests** → fetch HTML pages  
- **BeautifulSoup (bs4)** → extract job details from HTML  
- **pandas** → clean, transform, and export data into CSV  
- **os** → check file existence and avoid duplicates  
- **urllib.parse** → encode job titles in the URL  

---

## 🗂 Data Collected
- Job Titles  
- Job Links  
- Company Names  
- Company Links  
- Employment Type  
- Work Location  
- Location  

All results are exported into a CSV file for further analysis.

---

## 🤖 Automation with n8n
Running the script manually every day wasn’t practical.  
To solve this, I automated the workflow using **[n8n](https://n8n.io/)**:  

1. **Schedule Trigger** → runs the script every morning  
2. **Execute Command** → executes the Python scraper automatically  
3. **Duplicate Check** → prevents inserting the same jobs again  
4. **CSV Update** → new jobs are appended automatically  

---

## 📊 Insights & Dashboard
After collecting the data, I cleaned and analyzed it in Python, then built an **interactive Power BI dashboard** to visualize:  
- Top job titles in demand  
- Most common required skills  
- Job distribution by location  
- Employment type breakdown (Full-time, Part-time, Remote)  

---

## 🚀 Key Takeaways
- **Web Scraping** is a powerful way to collect real-world data.  
- **Automation** is not a luxury — it saves time and ensures data freshness.  
- The project workflow can be expanded to other platforms and use cases (e.g., LinkedIn, Indeed).  

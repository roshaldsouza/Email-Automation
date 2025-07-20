import requests
from bs4 import BeautifulSoup
import yagmail
import schedule
import time
from datetime import datetime

# Modify your keywords and email
KEYWORDS = ['entry level software developer', 'full stack', 'frontend', 'backend']
EMAIL = 'roshalds789@gmail.com'

def search_jobs():
    print(f"[{datetime.now()}] Searching jobs...")

    jobs_found = []

    for keyword in KEYWORDS:
        # Example search on Wellfound (AngelList)
        url = f"https://wellfound.com/jobs#find/f!f={keyword.replace(' ', '%20')}"
        jobs_found.append(f"🔍 {keyword.title()}:\n{url}\n")

    # Email the compiled list
    email_results(jobs_found)

def email_results(job_list):
    content = "\n\n".join(job_list)
    yag = yagmail.SMTP("roshalds789@gmail.com", "Rose.ds234")
    yag.send(
        to=EMAIL,
        subject="🔥 Daily Entry-Level Job Listings",
        contents=content
    )
    print("✅ Email sent!")

# Schedule job at 12 PM every day
schedule.every().day.at("12:00").do(search_jobs)

print("📅 Job automation started. Waiting for 12PM daily execution...")

while True:
    schedule.run_pending()
    time.sleep(60)

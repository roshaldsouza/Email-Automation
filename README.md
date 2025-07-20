📬 Daily Job Alert Automation – Entry-Level Software Roles
This Python script automates the process of finding entry-level software development jobs (Full Stack, Frontend, Backend, etc.) at top startups and emails you the latest job listings every day at 12 PM.

🚀 Features
Searches for job keywords like:

entry level software developer

full stack developer

frontend developer

backend developer

Uses job search URLs (e.g., Wellfound/AngelList)

Sends a daily email with job links

Runs every day at 12:00 PM using schedule

🛠️ Setup Instructions
1. Clone the Repository
bash
Copy code
git clone https://github.com/yourusername/daily-job-alerts.git
cd daily-job-alerts
2. Install Dependencies
bash
Copy code
pip install -r requirements.txt
Or install manually:

bash
Copy code
pip install requests beautifulsoup4 schedule yagmail
3. Configure Email (Gmail)
Go to Google App Passwords

Generate a new app password for Gmail

Update the email config in the script:

python
Copy code
yag = yagmail.SMTP("your_email@gmail.com", "your_app_password")
4. Run the Script
bash
Copy code
python main.py
This keeps running in the background and checks every minute for the 12 PM job to trigger.

🧠 Example Output
Your inbox will receive emails like this:

bash
Copy code
Subject: 🔥 Daily Entry-Level Job Listings

🔍 Entry Level Software Developer:
https://wellfound.com/jobs#find/f!f=entry%20level%20software%20developer

🔍 Full Stack:
https://wellfound.com/jobs#find/f!f=full%20stack

🔍 Frontend:
https://wellfound.com/jobs#find/f!f=frontend

🔍 Backend:
https://wellfound.com/jobs#find/f!f=backend

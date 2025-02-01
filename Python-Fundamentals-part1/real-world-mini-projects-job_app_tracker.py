## 🛠️ **7. Real-World Mini Project: Job Application Tracker (20 mins)**

### ✅ **Objective:**

# Create a script to track job applications.

jobs_applied = []

def add_job(job_title, company):
    jobs_applied.append({"title": job_title, "company": company})

def list_jobs():
    for job in jobs_applied:
        print(f"Applied to {job['title']} at {job['company']}")

add_job("Python Developer", "TechCorp")
list_jobs()


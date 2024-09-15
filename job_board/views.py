from django.shortcuts import render

jobs = [
    {
        "job_title": "Software Engineer",
        "description": "Develop, test, and maintain software applications. Work with a team to design scalable systems and write efficient code.",
        "location": "San Francisco, CA",
        "company": "Tech Innovators Inc.",
        "date_posted": "2024-08-25",
        "slug": "software-engineer",
        "pay_rate": "$120,000 - $140,000 per year"
    },
    {
        "job_title": "Marketing Manager",
        "description": "Plan and execute marketing campaigns, analyze market trends, and manage social media platforms. Collaborate with sales teams to drive brand awareness.",
        "location": "New York, NY",
        "company": "Creative Solutions LLC",
        "date_posted": "2024-08-26",
        "slug": "marketing-manager",
        "pay_rate": "$85,000 - $100,000 per year"
    },
    {
        "job_title": "Data Analyst",
        "description": "Collect, process, and analyze large datasets to provide actionable insights. Prepare reports and dashboards for stakeholders.",
        "location": "Austin, TX",
        "company": "Data Insights Corp.",
        "date_posted": "2024-08-24",
        "slug": "data-analyst",
        "pay_rate": "$70,000 - $85,000 per year"
    },
    {
        "job_title": "Project Manager",
        "description": "Oversee projects from initiation to completion, ensuring timely delivery within scope and budget. Coordinate between teams and stakeholders.",
        "location": "Chicago, IL",
        "company": "Management Experts Ltd.",
        "date_posted": "2024-08-27",
        "slug": "project-manager",
        "pay_rate": "$95,000 - $110,000 per year"
    },
    {
        "job_title": "Graphic Designer",
        "description": "Create visual content for print and digital media. Work with marketing teams to develop cohesive branding strategies.",
        "location": "Los Angeles, CA",
        "company": "Creative Minds Studio",
        "date_posted": "2024-08-23",
        "slug": "graphic-designer",
        "pay_rate": "$50,000 - $65,000 per year"
    },
    {
        "job_title": "Sales Executive",
        "description": "Identify and pursue new sales opportunities, build relationships with clients, and achieve sales targets.",
        "location": "Miami, FL",
        "company": "Global Sales Partners",
        "date_posted": "2024-08-28",
        "slug": "sales-executive",
        "pay_rate": "$60,000 - $80,000 per year + commission"
    },
    {
        "job_title": "Human Resources Manager",
        "description": "Manage HR operations including recruitment, employee relations, and performance management. Ensure compliance with labor laws.",
        "location": "Boston, MA",
        "company": "PeopleFirst HR Solutions",
        "date_posted": "2024-08-22",
        "slug": "human-resources-manager",
        "pay_rate": "$90,000 - $105,000 per year"
    },
    {
        "job_title": "Financial Analyst",
        "description": "Analyze financial data, create financial models, and provide recommendations to improve company profitability.",
        "location": "Dallas, TX",
        "company": "Finance Experts Inc.",
        "date_posted": "2024-08-29",
        "slug": "financial-analyst",
        "pay_rate": "$80,000 - $95,000 per year"
    },
    {
        "job_title": "Customer Service Representative",
        "description": "Assist customers with inquiries, resolve complaints, and provide product information. Maintain a high level of customer satisfaction.",
        "location": "Phoenix, AZ",
        "company": "CustomerFirst Solutions",
        "date_posted": "2024-08-20",
        "slug": "customer-service-representative",
        "pay_rate": "$18 - $22 per hour"
    },
    {
        "job_title": "Content Writer",
        "description": "Create engaging and informative content for websites, blogs, and social media. Collaborate with marketing teams to align content with brand voice.",
        "location": "Seattle, WA",
        "company": "Content Creators Co.",
        "date_posted": "2024-08-21",
        "slug": "content-writer",
        "pay_rate": "$45,000 - $60,000 per year"
    }
]


# Create your views here.
def starting_page(request):
    return render(request, "jobs/index.html")

def jobs(request):
    return render(request, "jobs/all-jobs.html")

def job_detail(request, slug):
    return render(request, "jobs/job-detail.html")
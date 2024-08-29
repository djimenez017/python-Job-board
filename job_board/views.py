from django.shortcuts import render

# Create your views here.
def starting_page(request):
    return render(request, "jobs/index.html")

def jobs(request):
    return render(request, "jobs/all-jobs.html")

def job_detail(request, slug):
    return render(request, "jobs/job-detail.html")
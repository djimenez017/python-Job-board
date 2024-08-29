from django.urls import path 

from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("jobs", views.jobs, name="jobs"),
    path("jobs/<slug:slug>", views.job_detail, name="job-detail-page")
]

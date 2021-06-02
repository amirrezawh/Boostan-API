from django.urls import path
from .views import (
    CourseView,
    ProfessorView,
    PollView,
    PollListView,
    ProfessorDataView, 
    GetCourseView
)

app_name = "Vote"


urlpatterns = [
    path('course/', CourseView.as_view(),
    name="course-create"),

    path('course/get/', GetCourseView.as_view(),
    name='get-course'),

    path('professor/', ProfessorView.as_view(),
    name="professor-create"),

    path('professor/list/', ProfessorDataView.as_view(),
    name="professor-data"),

    path('', PollView.as_view(),
    name="vote-view"),

    path('list/', PollListView.as_view(),
    name="vote-list"),
]
from django.shortcuts import render
from django.http import HttpResponse
from courses.models import Course, Major
# Create your views here.


def index(request):
    return render(request, "core/index.html")


def updateindex(request):
    Majors = Major.objects.all()
    Courses = Course.objects.all()

    results = request.GET['SelectedMajor']
    return render(request, "core/updateindex.html",
                  {'SelectedMajor': results,
                   'Majors': Majors,
                   'Courses': Courses
                   })

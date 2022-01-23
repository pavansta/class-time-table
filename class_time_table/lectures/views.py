from django.shortcuts import render
from .models import Lecture


def lectures(request):
    all_lectures = Lecture.objects.all
    return render(request, 'lectures.html', {'all': all_lectures})


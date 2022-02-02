
from django.shortcuts import render
from .models import Lecture


def lectures(request):
    all_lectures = Lecture.objects.all
    return render(request, 'lectures.html', {'all': all_lectures})

def add_lectures(request):
    Lecture(name='Pandu', lecturer_code='p01').save()
    batch = [
        Lecture(name='Pandu', lecturer_code='p01'),
        Lecture(name='Pandu', lecturer_code='p01'),
        Lecture(name='Pandu', lecturer_code='p01')
    ]
    Lecture.objects.bulk_create(batch)
    return redirect('/lectures/')
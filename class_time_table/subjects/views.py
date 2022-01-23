from django.shortcuts import render
from .models import Subject


def subjects(request):
    all_subjects = Subject.objects.all
    return render(request, 'subjects.html',{'all': all_subjects})







from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from rest_framework.parsers import JSONParser
import random

from .models import TimeTable
from subjects.models import Subject
from periods.models import Period
from days.models import Day
from .utils import create_table
import json

@csrf_exempt
def submit(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        # print(data)
        batch = []
        for val in data:
            batch.append(TimeTable(department_id=1, day_id=val['day'], period_id=val['period'], subject_id=val['subject']))
        print(batch)
        TimeTable.objects.bulk_create(batch)
    return JsonResponse(data, safe=False)


@login_required()
def index(request):
    osubjects = Subject.objects.values()
    operiods = Period.objects.values()
    odays = Day.objects.values()
    table = create_table(odays, operiods, osubjects)
    return render(request, "time-table.html", {'time_table': table['display_table'], 'db_table': table['db_table']})


def details(request):
    osubjects = Subject.objects.values()
    operiods = Period.objects.values()
    odays = Day.objects.values()
    table1 = create_table(odays, operiods, osubjects)
    table2 = create_table(odays, operiods, osubjects)
    table3 = create_table(odays, operiods, osubjects)
    print(table1, table2, table3)
    return JsonResponse({'test': 'test'}, safe=False)






















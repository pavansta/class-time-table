from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import TimeTable
from subjects.models import Subject
from periods.models import Period
from days.models import Day
from .utils import create_table


@csrf_exempt
def submit(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        batch = []
        for val in data:
            batch.append(
                TimeTable(department_id=1, day_id=val['day'], period_id=val['period'], subject_id=val['subject']))
        TimeTable.objects.bulk_create(batch)
    return JsonResponse(data, safe=False)


@csrf_exempt
def delete_everything(request):
    TimeTable.objects.all().delete()
    return JsonResponse({'message': 'data deleted successfully.'}, safe=False)


@login_required()
def index(request):
    time_table = TimeTable.objects.all()
    if time_table.exists():
        table = []
        day = {}
        i = 0
        for val in time_table:
            if i % 6 == 0:
                day = {'name': val.day.name}
            day[val.period.name] = val.subject.name
            i = i + 1
            if i % 6 == 0:
                table.append(day)
        return render(request, "time-table.html", {'time_table': table, 'is_db': True})
    else:
        osubjects = Subject.objects.values()
        operiods = Period.objects.values()
        odays = Day.objects.values()
        table = create_table(odays, operiods, osubjects)
        return render(request, "time-table.html",
                      {'time_table': table['display_table'], 'db_table': table['db_table'], 'is_db': False})


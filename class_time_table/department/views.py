from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def index(request):
    time_table = [
        {
            'name': 'MONDAY',
            'periods': {
                'period1': 'English',
                'period2': 'kannada',
                'period3': 'maths',
                'period4': 'cultural',
                'period5': 'd e',
                'period6': 'c p'
            }
        },
        {
            'name': 'TUESDAY',
            'periods': {
                'period1': 'kannada',
                'period2': 'english',
                'period3': 'd e',
                'period4': 'c p',
                'period5': 'cultural',
                'period6': 'maths'
            }
        },
        {
            'name': 'WEDNESDAY',
            'periods': {
                'period1': 'maths',
                'period2': 'c p',
                'period3': 'kannada',
                'period4': 'cultural',
                'period5': 'd e',
                'period6': 'english'
            }
        },
        {
            'name': 'THURSDAY',
            'periods': {
                'period1': ' d e ',
                'period2': 'cultural',
                'period3': 'english',
                'period4': 'c p',
                'period5': 'kannada',
                'period6': 'maths'
            }
        },
        {
            'name': 'FRIDAY',
            'periods': {
                'period1': ' maths ',
                'period2': 'kannada',
                'period3': 'c p',
                'period4': 'english',
                'period5': 'cultural',
                'period6': 'd e'
            }
        }

    ]
    return render(request, "department.html", {'time_table': time_table})
# Create your views here.

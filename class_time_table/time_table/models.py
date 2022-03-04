from django.db import models

from subjects.models import Subject
from periods.models import Period
from days.models import Day
from department.models import Department


class TimeTable(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('day', 'period', 'day')

    def __str__(self):
        return f"{self.day} - {self.period.name} - {self.subject.name}"


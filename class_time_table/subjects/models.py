from django.db import models

from lectures.models import Lecture


class Subject(models.Model):
    name = models.CharField(max_length=25)
    subject_code = models.CharField(max_length=20)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


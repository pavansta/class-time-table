from django.db import models


class Lecture(models.Model):
    name = models.CharField(max_length=20)
    lecturer_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"

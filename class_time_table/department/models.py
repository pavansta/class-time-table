from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"


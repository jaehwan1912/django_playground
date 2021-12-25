from django.db import models


class Ratable(models.Model):
    name = models.CharField(max_length=160)
    reg_date = models.DateTimeField('date registered')

    def __str__(self):
        return self.name


class Rating(models.Model):
    ratable = models.ForeignKey(Ratable, on_delete=models.CASCADE)
    grade = models.IntegerField(default=10)
    detail = models.CharField(max_length=320)

    def __str__(self):
        return "Rating for " + self.ratable.name + " : " + str(self.grade)

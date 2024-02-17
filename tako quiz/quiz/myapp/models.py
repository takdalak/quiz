from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    stack = models.CharField(max_length=100)
    team_lead = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.surname}"

class Stack(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
from django.db import models


class Patient(models.Model):
    patientId = models.IntegerField()
    userName = models.CharField(max_length=20)
    password = models.CharField(max_length=10)



    def _str_(self):
        return self.userName;

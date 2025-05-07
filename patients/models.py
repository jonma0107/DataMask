from django.db import models

class PatientRecord(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    diagnosis = models.TextField()

    def __str__(self):
        return f"Patient: {self.name}"
from rest_framework import viewsets
from .models import PatientRecord
from .serializers import PatientRecordSerializer

class PatientRecordViewSet(viewsets.ModelViewSet):
    queryset = PatientRecord.objects.all()
    serializer_class = PatientRecordSerializer
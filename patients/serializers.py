from rest_framework import serializers
from .models import PatientRecord
from faker import Faker

fake = Faker()

class PatientRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientRecord
        fields = '__all__'

    def to_representation(self, instance):
        # Enmascarar solo al serializar (GET)
        rep = super().to_representation(instance)
        rep['name'] = fake.name()
        rep['diagnosis'] = fake.catch_phrase()
        return rep

    # El método create ya no enmascara, solo guarda los datos reales
from rest_framework import serializers
from .models import PatientRecord
from faker import Faker

fake = Faker()

class PatientRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientRecord
        fields = '__all__'

    def create(self, validated_data):
        # Mask sensitive data
        validated_data['name'] = fake.name()
        validated_data['diagnosis'] = fake.catch_phrase()

        # Create the PatientRecord instance with masked data
        return PatientRecord.objects.create(**validated_data)
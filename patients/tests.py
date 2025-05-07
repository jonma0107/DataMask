from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from patients.models import PatientRecord
from patients.serializers import PatientRecordSerializer
from rest_framework import status

class PatientRecordAPITestCase(APITestCase):

    def test_create_patient_record_masks_data(self):
        """
        Test that creating a PatientRecord object masks the name and diagnosis fields.
        """
        url = reverse('patientrecord-list') # Assuming your router creates a name like 'patientrecord-list'
        sample_data = {
            'name': 'Pablo',
            'age': 35,
            'diagnosis': 'Acute Appendicitis'
        }

        response = self.client.post(url, sample_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PatientRecord.objects.count(), 1)

        created_patient = PatientRecord.objects.get(id=response.data['id'])

        # Assert that name and diagnosis are masked
        self.assertNotEqual(created_patient.name, sample_data['name'])
        self.assertNotEqual(created_patient.diagnosis, sample_data['diagnosis'])

        # Assert that age is not masked
        self.assertEqual(created_patient.age, sample_data['age'])
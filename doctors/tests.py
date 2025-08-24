from django.test import TestCase
from patients.models import Patient
from doctors.models import Doctor
from rest_framework.test import APIClient


class DoctorViewSetTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.patient = Patient.objects.create(
            first_name="John",
            last_name="Doe",
            date_of_birth="1990-01-01",
            contact_number="1234567890",
            email="john.doe@example.com",
            address="123 Main St",
            medical_history="No known allergies",
        )
        self.doctor = Doctor.objects.create(
            first_name="Jane",
            last_name="Smith",
            qualification="Cardiology",
            contact_number="0987654321",
            email="jane.smith@example.com",
            address="456 Elm St",
            biography="Experienced cardiologist",
            is_on_vacation=False,
        )

    def test_list_should_return_200(self):
        response = self.client.get("/doctors/")
        self.assertEqual(response.status_code, 200)

from time import timezone
from rest_framework import serializers

from bookings.serializers import AppointmentSerializer
from .models import Patient, Insurance, MedicalRecord


class PatientSerializer(serializers.ModelSerializer):

    appointments = AppointmentSerializer(many=True, read_only=True)
    age = serializers.SerializerMethodField()

    def get_age(self, obj):
        if obj.date_of_birth:
            return (timezone.now().date() - obj.date_of_birth).days // 365
        return None

    class Meta:
        model = Patient
        fields = [
            "id",
            "first_name",
            "last_name",
            "age",
            "date_of_birth",
            "contact_number",
            "email",
            "address",
            "medical_history",
            "appointments",
        ]


class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = "__all__"


class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = "__all__"

from attr import attrs
from rest_framework import serializers

from bookings.serializers import AppointmentSerializer

from .models import Doctor, Department, DoctorAvailability, MedicalNote


class DoctorSerializer(serializers.ModelSerializer):
    appointments = AppointmentSerializer(
        many=True, read_only=True
    )  # Citas del doctor (relación con citas)

    class Meta:
        model = Doctor
        fields = [
            "id",
            "first_name",
            "last_name",
            "qualification",
            "contact_number",
            "email",
            "address",
            "biography",
            "appointments",
        ]

        def validate(self, attrs):
            if len(attrs["contact_number"]) > 10 and attrs["is_on_vacation"] == True:
                raise serializers.ValidationError(
                    "El número de contacto no puede tener más de 10 dígitos si el doctor está en vacaciones"
                )
            return super().validate(attrs)


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class DoctorAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorAvailability
        fields = "__all__"


class MedicalNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalNote
        fields = "__all__"

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response

from bookings.serializers import AppointmentSerializer
from .models import Doctor
from .serializers import DoctorSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=["post"], url_path="set_on_vacation")
    def set_on_vacation(self, request, pk=None):
        doctor = self.get_object()
        doctor.is_on_vacation = True
        doctor.save()
        return Response({"status": "El doctor está en vacaciones"})

    @action(detail=True, methods=["post"], url_path="set_off_vacation")
    def set_off_vacation(self, request, pk=None):
        doctor = self.get_object()
        doctor.is_on_vacation = False
        doctor.save()
        return Response({"status": "El doctor no está en vacaciones"})

    @action(
        detail=True, methods=["POST", "GET"], serializer_class=AppointmentSerializer
    )
    def appointments(self, request, pk):
        doctor = self.get_object()
        if request.method == "POST":
            data = request.data.copy()
            data["doctor"] = doctor.id
            serializer = AppointmentSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=201)

        if request.method == "GET":
            appointments = AppointmentSerializer.objects.filter(doctor=doctor)
            serializer = AppointmentSerializer(appointments, many=True)
            return Response(serializer.data)

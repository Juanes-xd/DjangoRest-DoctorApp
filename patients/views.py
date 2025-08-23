from .models import Patient
from .serializers import PatientSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

# Create your views here.


class ListPatientView(ListAPIView, CreateAPIView):
    allowed_methods = ["GET", "POST"]
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class DetailPatientView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ["GET", "PUT", "DELETE"]
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

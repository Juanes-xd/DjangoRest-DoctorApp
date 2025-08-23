from django.shortcuts import render
from .models import Patient, Insurance, MedicalRecord
from .serializers import PatientSerializer, InsuranceSerializer, MedicalRecordSerializer
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


class ListPatientView(ListAPIView):
    allowed_methods = ["GET", "POST"]
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class DetailPatientView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ["GET", "PUT", "DELETE"]
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class DetailPatientView(APIView):
    allowed_methods = ["GET", "PUT", "DELETE"]

    def get(self, request, pk):
        try:
            patient = Patient.objects.get(pk=pk)
            serializer = PatientSerializer(patient)
            return Response(serializer.data)
        except Patient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            patient = Patient.objects.get(pk=pk)
            serializer = PatientSerializer(patient, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        except Patient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            patient = Patient.objects.get(pk=pk)
            patient.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Patient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

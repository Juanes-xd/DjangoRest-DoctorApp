from django.urls import path
from .views import ListPatientView, DetailPatientView

urlpatterns = [
    path("patients/", ListPatientView.as_view(), name="patient-list"),
    path("patients/<int:pk>/", DetailPatientView.as_view(), name="patient-detail"),
]

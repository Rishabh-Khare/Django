from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.views import status

from .models import Patient
from .serializer import PatientSerializers


# Create your views here.


@api_view(['GET'])
def get_patient(request, id):
    patient_list = Patient.objects.filter(patientId=id)
    serializer = PatientSerializers(patient_list, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
@csrf_exempt
def add_patient(request):
    patient_data = JSONParser().parse(request)
    serial_patient_data = PatientSerializers(data=patient_data)
    if serial_patient_data.is_valid():
        serial_patient_data.save()
        return JsonResponse(serial_patient_data.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serial_patient_data.errors, status=status.HTTP_400_BAD_REQUEST)

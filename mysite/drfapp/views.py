from django.shortcuts import render
from .models import Student
from rest_framework.views import APIView
from django.http import HttpResponse
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer

from rest_framework.response import Response


# Create your views here.


def student_details(request):
    stu = Student.objects.get(name='Sam')
    serializer = StudentSerializer(stu)
    json_data = JSONRenderer().render(serializer.data)

    return HttpResponse(json_data)

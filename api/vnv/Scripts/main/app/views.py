from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from app import models

from app.models import Soil
import json
# Create your views here.


def show_data(request):
    response = {}

    try:
        soil = Soil.objects.filter()
        response['all'] = json.loads(serializers.serialize("json", soil))
        response['msg'] = 'success'
        response['error_num'] = 0

    except Exception as e :
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

def add(request):
    response = {}
    print(request.GET)
    try:
        soil = Soil()

        airhum = request.GET.get('airhum')
        sun = request.GET.get('sun')
        soilhum = request.GET.get('soilhum')
        temp = request.GET.get('temp')

        soil.airhum = airhum
        soil.sun = sun
        soil.soilhum = soilhum
        soil.temp = temp
        soil.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e :
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)
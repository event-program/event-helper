from django.shortcuts import render
from django.http import JsonResponse
from .library import *


def test_view(request):
    return JsonResponse({'status':'200', 'code':'only for test'})


def qr_view(request):
    return qr_function.view(request)


def user_view(request):
    return user_function.view(request)


def gps_view(request):
    return gps_function.view(request)


def translate_view(request):
    return translate_function.view(request)

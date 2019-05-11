from django.shortcuts import render
from django.http import JsonResponse


def test_view(request):
    return JsonResponse({'status':'200', 'code':'only for test'})


def qr_view(request):
    return JsonResponse({'status': '200', 'code': 'only for qr test'})


def user_view(request):
    return


def gps_view(request):
    return


def translate_view(request):
    return

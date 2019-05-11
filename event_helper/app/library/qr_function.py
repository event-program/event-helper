import requests
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from .models import User, Event


def view(request):
    if request.method == 'GET':
        user_id = request.POST.get('user_id', '')
        now_user = get_object_or_404(User, user_id=user_id)
        response = requests.get("https://pierre2106j-qrcode.p.rapidapi.com/api?type=text&text={0}".format(user_id),
                               headers={
                                   "X-RapidAPI-Host": "pierre2106j-qrcode.p.rapidapi.com",
                                   "X-RapidAPI-Key": "dd3add1c5emsh2be6cdb031c24cep13c2d4jsnbc187ba7e275"
                               }
                               )
        return JsonResponse({'status_code': '200', 'qr_image':response.text})
    else:
        return HttpResponseBadRequest()

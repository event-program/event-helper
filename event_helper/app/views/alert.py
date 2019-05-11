import requests
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from ..models import Participant, Event, Alert

def alert_view(request):
    if request.method == 'POST':
        #user_id = request.POST.get('user_id', '')
        #now_user = get_object_or_404(Participant, user_id=user_id)
        response = requests.get("https://pierre2106j-qrcode.p.rapidapi.com/api?type=text&text={0}".format(user_id),
                               headers={
                                   "X-RapidAPI-Host": "pierre2106j-qrcode.p.rapidapi.com",
                                   "X-RapidAPI-Key": "dd3add1c5emsh2be6cdb031c24cep13c2d4jsnbc187ba7e275"
                               }
                               )
        #now_user.qr_code = response.text
        #print(now_user.qr_code)
        return JsonResponse({'status_code': '200'})
    else:
        return HttpResponseBadRequest()
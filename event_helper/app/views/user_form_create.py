from django.http import JsonResponse
from ..models import Participant, Event
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def user_forms_create(request):
    req = dict(json.loads(request.body.decode('utf-8')))
    participant_instance = Participant(id=str(req['id']), language=str(req['language']), country=str(req['country']), phone=str(req['phonenumber']))
    participant_instance.save()

    return JsonResponse({'status_code': '200'})
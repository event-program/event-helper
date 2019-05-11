from django.http import JsonResponse
from ..models import Participant, Event
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def user_forms_create(request):
    req = dict(json.loads(request.body.decode('utf-8')))
    print(req)
    print(req['country'])
    participant_instance = Participant(id=str(req['id']), language=str(req['language']), country=str(req['country']), phone=str(req['phonenumber']))

    #Ent = Event.objects.all().filter(name=req['event_name'])
    #Ent.objects.entry.add(Participant)

    participant_instance.save()

    return 200
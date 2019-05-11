import json

from ..models import Participant, Event
from django.http import JsonResponse
from django.utils import timezone

def event_view(request):
    if request.method == 'GET':
        event_name = request.GET.get('event', '')
        now_event = Event.objects.filter(name=event_name)
        return JsonResponse({
                                'status_code': '200',
                                'event_name': now_event.name,
                                'entry': [ i.id for i in now_event.entry.all()],
                                'start_date': now_event.start_date.strftime("%Y,%m,%d,%H,%M,%S") ,
                                'end_date': now_event.end_date.strftime("%Y,%m,%d,%H,%M,%S"),
                                'location': now_event.location,
                                'description': now_event.description,
                            })
    pass

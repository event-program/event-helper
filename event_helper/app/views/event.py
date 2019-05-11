import json

from ..models import Participant, Event
from django.http import JsonResponse
from django.utils import timezone
from datetime import datetime


def event_view(request):
    if request.method == 'GET':
        event_name = request.GET.get('event', '')
        now_event = Event.objects.filter(name=event_name)[0]
        return JsonResponse({
            'status_code': '200',
            'event_name': now_event.name,
            'entry': [i.id for i in now_event.entry.all()],
            'start_date': now_event.start_date.strftime("%Y,%m,%d,%H,%M,%S"),
            'end_date': now_event.end_date.strftime("%Y,%m,%d,%H,%M,%S"),
            'location': now_event.location,
            'description': now_event.description,
        })
    if request.method == 'POST':
        req = json.loads(request.text)
        event_instance = Participant(name=request['name'], start_date=timezone.make_aware(
            datetime.strptime(request['start_date'], '%Y,%m,%d,%H,%M,%S')), end_date=timezone.make_aware(
            datetime.strptime(request['end_date'], '%Y,%m,%d,%H,%M,%S')), location=request['location'],
                                     country=request['country'])

        event_instance.save()

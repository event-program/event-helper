from django.http import JsonResponse
from ..models import Participant
import json

def views(request):
    """
    {
        "event_name"
        "name":"",
        "id":"",
        "phonenumber":"",
        "language":"",
        "country": "",
    }
    """

    req = json.loads(request.text)
    participant_instance = Participant(id=request['id'],name=request['name'] \
            , phone=request['phonenumber'], language=request['language'], \
                country=request['country'])

    participant_instance.save()
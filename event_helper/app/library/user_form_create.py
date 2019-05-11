from django.http import JsonResponse
from models import Participant
import json

def views(request):
    """
    {
        "name":"",
        "id":"",
        "phonenumber":"",
        "language":"",
        "nation": "",
    }
    """

    req = json.loads(request.text)
    participant_instance = Participant(id=request['id'])
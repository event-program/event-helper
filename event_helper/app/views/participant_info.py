from django.http import JsonResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from ..models import Participant, Event
from .qr_function import qr_view    

def participant_view(request):
    # return Dict.

    if request.method == "GET":
        event_name = request.GET.get('event_name')
        
        if not event_name:
            return [None,None]

        this_event = get_object_or_404(Event, name=event_name)

        #print(this_event.entry.all()[0].username)

        return_data = {"username":[],"phone":[]}

        for i in this_event.entry.all():
            #print(i.username)
            #return_data.append([str(i.username),str(i.phone)])
            return_data["username"].append(i.username)
            return_data["phone"].append(i.phone)
        #print(return_data)
        #return this_event.entry.order_by('user_id').

        return JsonResponse(return_data)

    else:
        return HttpResponseNotFound

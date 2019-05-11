from django.http import JsonResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from ..models import Participant, Event
from .qr_function import qr_view
def gps_view(request):
    # return Dict.

    if request.method == "POST":
        longitude = request.POST.get('longitude')
        latitude = request.POST.get('latitude')
        user_id = request.POST.get('user_id','')

        now_event = get_object_or_404(Event, name="정션X")
        now_user = get_object_or_404(Participant, user_id=user_id)
        # 이벤트 1개 임시
        event_la, event_lo = now_event.location.split(' ')

        if not now_user.qr_code:
            if (abs(float(event_lo) - float(longitude)) > 0.0001) or (abs(float(event_la) - float(latitude)) > 0.0001) :
                return JsonResponse({'status_code':'404','qr_image':''})

        return qr_view(request)

    else:
        return HttpResponseNotFound

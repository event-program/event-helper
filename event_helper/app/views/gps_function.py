from django.http import JsonResponse
from django.shortcuts import get_object_or_404


def gps_view(request):
    # return Dict.

    if request.method == "POST":
        longitude = request.POST.get('longitude')
        latitude = request.POST.get('latitude')

        return {"longitude": longitude, "latitude":latitude}

    else:
        return 404

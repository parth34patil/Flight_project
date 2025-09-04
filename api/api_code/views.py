from urllib import request
from django.shortcuts import render 
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status  # ✅ Correct import
from .models import flight  # ✅ Capitalize model name
from .serializers import FlightSerializer
from datetime import datetime

# ✅ GET method: Fetch flights by origin and destination
@api_view(['GET'])
def get_items(request):
    origin = request.GET.get('from')
    destination = request.GET.get('to')

    if origin and destination:
        flights = flight.objects.filter(origin=origin, destination=destination)
        serializer = FlightSerializer(flights, many=True)
        return Response(serializer.data)
    else:
        return Response({'error': 'Please provide both "from" and "to" parameters.'}, status=404)

# ✅ POST method: Add a flight entry
@api_view(['POST'])
def create_flight(request):
    serializer = FlightSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def flight_form(requst):
    return render(request,'flight_form.html')

def search_flight(request):
    origin = request.GET.get('from')
    destination = request.GET.get('to')
    departure_date = request.GET.get('departure_date')

    api_url = 'http://127.0.0.1:8000/get_items/'
    params = {'from':origin, 'to':destination, 'departure_date': departure_date}

    try:
        response = requests.get(api_url, params=params)
        flights = response.json()
        # Convert departure_time to datetime object for each flight
        for f in flights:
            if isinstance(f.get('departure_time'), str):
                try:
                    f['departure_time'] = datetime.fromisoformat(f['departure_time'].replace('Z', '+00:00'))
                except Exception:
                    f['departure_time'] = None
    except:
        flights = []

    return render(request, 'flight_result.html', {'flights': flights})



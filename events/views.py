from django.shortcuts import render
from events.models import Event


# Create your views here.
def home(request):
    events = Event.objects
    return render(request, 'events/event1.html', {'events': events})
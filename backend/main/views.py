from django.http import HttpResponse
from django.shortcuts import render
from .models import Ticket

# Create your views here.
def test(request):
    
    return HttpResponse(str(Ticket.objects.get(ticket_id=1).price   ))
from django.http import HttpResponse
from django.shortcuts import render
from .models import Ticket
from main.repository.MainPoint import MainPoint


# Create your views here.
def add(request):

    return HttpResponse(str(Ticket.objects.get(ticket_id=1).price))


def read(request):
    try:
        a = request.GET["id"]
        return HttpResponse(str(MainPoint().directors.get_by_id(int(request.GET["id"])).biography))
    except Exception:
        return HttpResponse(
            "\n".join(list(map(lambda x: str(x.biography), MainPoint().directors.get_all())))
        )

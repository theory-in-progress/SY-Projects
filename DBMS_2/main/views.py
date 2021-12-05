from django.shortcuts import render
from accounts.models import *
from django.http import HttpResponseRedirect
# Create your views here.


def index(request):
    movies = Movie.objects.all()
    context = {
        'mov': movies
    }
    return render(request,"index.html", context)

def movies(request, id):
    #cin = Cinema.objects.filter(shows__movie=id).distinct()
    movies = Movie.objects.get(movie=id)
    cin = Cinema.objects.filter(cinema_show__movie=movies).prefetch_related('cinema_show').distinct()  # get all cinema
    show = Shows.objects.filter(movie=id)
    context = {
        'movies':movies,
        'show':show,
        'cin':cin,
    }
    return render(request, "movies.html", context )

def seat(request, id):
    show = Shows.objects.get(shows=id)
    seat = Bookings.objects.filter(shows=id)
    return render(request,"seat.html", {'show':show, 'seat':seat})    

def booked(request):
    if request.method == 'POST':
        user = request.user
        seat = request.POST.get('SeatNo.')
        show = request.POST['show']
        book = Bookings(useat=seat, shows_id=show, user=user)
        # book_total = ticket(request='POST')
        book.save()

        # ticket = Bookings.objects.get(id=id)
        # count=0
        # for seat in book.useat:
        #     if seat=='#':
        #         count=count+1
        # price_t=book.shows.price*count
        # book.price_total = price
        return render(request,"booked.html", {'book':book})
        

def ticket(request, id):
    ticket = Bookings.objects.get(id=id)
    count=0
    for seat in ticket.useat:
        if seat=='#':
            count=count+1
    price=ticket.shows.price*count
    return render(request,"ticket.html", {'ticket':ticket,'price':price})


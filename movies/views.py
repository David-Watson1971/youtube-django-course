from django.http import HttpResponse
from django.shortcuts import render

data = {
    'movies':[
        {
            'id': 5,
            'title': 'Jaws',
            'Year': 1669
        },
        {
            'id': 6,
            'title': 'Sharknado',
            'Year': 1600
        },
        {
            'id': 7,
            'title': 'The Meg',
            'Year': 2000
        }   

    ]
}

def home(request):
    return HttpResponse("Hello there!!!!")
    
def movies(request):
    return render(request, 'movies/movies.html', data) 
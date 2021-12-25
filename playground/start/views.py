from django.http import HttpResponse
from django.template import loader

from .models import *


def index(request):
    return HttpResponse("This is a toy project. you're at 'start'.")


def ratables(request):
    ratables_from_latest = Ratable.objects.order_by('-reg_date')

    template = loader.get_template('start/ratables.html')

    context = {
        'ratables_from_latest': ratables_from_latest,
    }

    return HttpResponse(template.render(context, request))


def ratings(request, ratable_id):
    ratable = None
    try:
        ratable = Ratable.objects.get(id=ratable_id)
    except:
        pass

    ratings_for_a_ratable = Rating.objects.filter(ratable__id=ratable_id)

    template = loader.get_template('start/ratings.html')

    context = {
        'ratable': ratable,
        'ratings_for_a_ratable': ratings_for_a_ratable,
    }

    return HttpResponse(template.render(context, request))


def rating(request, ratable_id, rating_id):
    rating = None
    try:
        rating = Rating.objects.get(id=rating_id)
        if rating.ratable.id != ratable_id:
            rating = None
    except:
        pass

    template = loader.get_template('start/rating.html')

    context = {
        'rating': rating
    }

    return HttpResponse(template.render(context, request))


def rate(request, ratable_id):
    response = "Vote for {}"
    return HttpResponse(response.format(ratable_id))


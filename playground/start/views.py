from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

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
        'ratings_for_a_ratable': reversed(ratings_for_a_ratable),
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
    ratable = get_object_or_404(Ratable, pk=ratable_id)
    context = {
        'ratable': ratable,
        'error_msgs': [],
    }

    if request.method == "POST":
        error = False
        score = request.POST['score']
        detail = request.POST['detail']
        if not score:
            context['error_msgs'].append("You must provide a score")
            error = True
        if not detail:
            context['error_msgs'].append("You must provide details")
            error = True

        if error:
            return render(request, 'start/rate.html', context)
        else:
            rating = Rating(ratable=ratable, grade=score, detail=detail)
            rating.save()
        return HttpResponseRedirect(reverse('start:result', args=(ratable.id, rating.id)))
        
    else:
        return render(request, 'start/rate.html', context)

def result(request, ratable_id, rating_id):
    ratable = get_object_or_404(Ratable, pk=ratable_id)
    rating = get_object_or_404(Rating, pk=rating_id)
    return render(request, 'start/result.html', {'ratable': ratable, 'rating': rating,})


class GenericRatables(generic.ListView):
    template_name = 'start/ratables.html'
    context_object_name = 'ratables_from_latest'

    def get_queryset(self):
        return Ratable.objects.order_by('-reg_date')


class GenericRatings(generic.DetailView):
    model = Ratable
    template_name = 'start/ratings.html'
    

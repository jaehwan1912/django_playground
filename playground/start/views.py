from django.http import HttpResponse


def index(request):
    return HttpResponse("This is a toy project. you're at 'start'.")


def ratables(request):
    response = "Currently ratable things are : \n"
    return HttpResponse(response)


def ratings(request, ratable_id):
    response = "Ratings for {}"
    return HttpResponse(response.format(ratable_id))


def rate(request, ratable_id):
    response = "Vote for {}"
    return HttpResponse(response.format(ratable_id))


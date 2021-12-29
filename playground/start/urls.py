from django.urls import path

from . import views

app_name = 'start'

urlpatterns = [
    path('', views.ratables, name='ratables'),
    path('<int:ratable_id>/', views.ratings, name='ratings'),
    path('<int:ratable_id>/<int:rating_id>/', views.rating, name='rating'),
    path('<int:ratable_id>/rate/', views.rate, name='rate'),
    path('<int:ratable_id>/<int:rating_id>/result/', views.result, name='result'),
    path('generic/', views.GenericRatables.as_view(), name='generic_ratables'),
    path('generic/<int:pk>/', views.GenericRatings.as_view(), name='generic_ratings'),
]

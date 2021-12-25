from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('ratables/', views.ratables, name='ratables'),
    path('<int:ratable_id>/', views.ratings, name='ratings'),
    path('<int:ratable_id>/rate/', views.rate, name='rate'),
]

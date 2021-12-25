from django.urls import path

from . import views


urlpatterns = [
    path('', views.ratables, name='ratables'),
    path('<int:ratable_id>/', views.ratings, name='ratings'),
    path('<int:ratable_id>/<int:rating_id>/', views.rating, name='rating'),
    path('<int:ratable_id>/rate/', views.rate, name='rate'),
]

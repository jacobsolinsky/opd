from django.urls import path

from . import views

urlpatterns = [
    path('search', views.regular_search),
    path('main-entry/<entry>', views.main_entry),
    path('', views.homepage)
]

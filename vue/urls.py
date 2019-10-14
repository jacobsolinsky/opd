from django.urls import path

from . import views

urlpatterns = [
    path('search', views.regular_search),
    path('main-entry/<entry>', views.main_entry),
    path('get-csrf-token', views.get_csrf_token),
    path('login', views.login),
    path('', views.homepage),
]

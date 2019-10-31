from django.urls import path, re_path

from . import views

urlpatterns = [
    path('json/search', views.regular_search),
    path('json/main-entry/<entry>', views.main_entry),
    path('json/collection/<id>', views.collection),
    path('json/all-parts-of-speech', views.all_parts_of_speech),
    path('json/word-part/<entry>', views.word_part),
    path('get-csrf-token', views.get_csrf_token),
    re_path(r'^.*$', views.homepage),
]

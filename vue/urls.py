from django.urls import path, re_path, include
from rest_framework.routers import SimpleRouter

from . import views
from .viewsets import router




urlpatterns = router.urls + [
    path('login', views.login),
    path('json/search', views.regular_search),
    path('json/main-entry/<entry>', views.main_entry),
    path('json/collection/<id>', views.collection),
    path('json/word-part/<entry>', views.word_part),
    path('get-csrf-token', views.get_csrf_token),
    path('logout', views.logout_),
    path('am-i-authenticated', views.am_i_authenticated),
    path('api/', include(router.urls)),
    re_path(r'^.*$', views.homepage),
]

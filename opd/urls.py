"""opd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from dictionary import views
from django.shortcuts import render
urlpatterns = [
    path('admin/', admin.site.urls),
    path('main-entry/<entry>', views.main_entry),
    path('advanced_search', views.advanced_search_front),
    path('search', views.regular_search),
    path('speaker/<speaker>', views.speaker),
    path('help/ojibwe-parts-of-speech', views.ojibwe_parts_of_speech),
    path('why-we-need-ojibwe-peoples-dictionary', lambda request: render(request, "dictionary/why-we-need-ojibwe-peoples-dictionary.html")),
    path('content/project-sponsors', lambda request: render(request, 'dictionary/content/project-sponsors.html')),
    path('understanding-audio-and-example-sentences', lambda request: render(request, 'dictionary/understanding-audio-and-example-sentences.html')),
    path('understanding-word-stems-word-parts-and-word-families', lambda request: render(request, '/ictionary/understanding-word-stems-word-parts-and-word-families.html')),
    path('news/dictionary', lambda request: render(request, 'dictionary/news/dictionary.html')),
    path('contact', lambda request: render(request, "dictionary/contact.html")),
    path('vue/', include('vue.urls')),
    path('', views.homepage)
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

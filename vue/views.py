from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse
from conjugator.htmlmaker import conj_call
from conjugator.morphemes import ojibwe_lev, todoublevowel
from django.core import serializers
from dictionary.models import *
from rest_framework.renderers import JSONRenderer
from django.contrib.auth import authenticate, login as authlogin, logout
from dictionary.serializers import *
import django.middleware.csrf
import re
import json


def homepage(request):
    return render(request, "dictionary/base-vue.html")
def regular_search(request):
  query = request.GET.get('q')
  type = request.GET.get('type')
  if type == 'ojibwe':
      entries = MainEntry.objects.filter(head_lemma=query)
  else:
      all = MainEntry.objects.all()
      entries = [a for a in all if
                 re.search(rf"\b{re.escape(query)}\b", a.gloss)]
  return HttpResponse(JSONRenderer().render(SearchLinkSerializer(entries, many=True).data), content_type="application/json")
def main_entry(request, entry):
    m_e = MainEntry.objects.get(pk="/main-entry/" + entry)
    conjugation = conj_call(m_e)
    m_e = MainEntrySerializer(m_e).data
    m_e['conjugation'] = conjugation
    return HttpResponse(JSONRenderer().render(m_e), content_type="application/json")
def get_csrf_token(request):
    token = django.middleware.csrf.get_token(request)
    return JsonResponse({'token': token})
def login(request):
    try: logout(request)
    except: pass
    if request.method == "POST":
        body = json.loads(request.body.decode('utf-8'))
        username = body.get('username')
        password = body.get('password')
        user = authenticate(request, username=username, password=password)
        authlogin(request, user)
        if user is not None:
            if user.is_active:
                return HttpResponse('yes')
        else:
            return HttpResponse('no')

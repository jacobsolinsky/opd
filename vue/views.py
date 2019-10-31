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


def get_lookup_field(type, scope, field):
    retval = ""
    if type == "ojibwe":
        return "head_lemma"
    if field == "lemma":
        retval = "head_lemma"
    elif field == "stem":
        retval = "stem"
    if scope == "exact":
        return retval
    elif scope == "starts_with":
        return retval + "__istartswith"
    elif scope == "ends_with":
        return retval + "__iendswith"
    elif scope == "contains":
        return retval + "__icontains"

def regular_search(request):
    query = request.GET.get('q')
    type = request.GET.get('type')
    query, type, scope, field = map(request.GET.get, ['q', 'type', 'scope', 'field'])
    entries = None
    if type in ['ojibwe', 'main_entry']:
        lf = get_lookup_field(type, scope, field)
        entries = MainEntry.objects.filter(**{lf:query})
    elif type == "english":
        all = MainEntry.objects.all()
        entries = [a for a in all if
            re.search(rf"\b{re.escape(query)}\b", a.gloss)]
    return HttpResponse(JSONRenderer().render(SearchLinkSerializer(entries, many=True).data), content_type="application/json")


def main_entry(request, entry):
    m_e = MainEntry.objects.get(pk="/main-entry/" + entry)
    conjugation = None
    if m_e.stem and m_e.part_of_speech and \
    m_e.part_of_speech.abbrev in ['vai', 'vti', 'vti2', 'vta', 'vii']:
        conjugation = conj_call(m_e)
    m_e = MainEntrySerializer(m_e).data
    m_e['conjugation'] = conjugation
    return HttpResponse(JSONRenderer().render(m_e), content_type="application/json")
def get_csrf_token(request):
    token = django.middleware.csrf.get_token(request)
    return JsonResponse({'token': token})
def all_parts_of_speech(request):
    return HttpResponse(
    JSONRenderer().render(
    LittlePartOfSpeechSerializer(PartOfSpeech.objects.all(), many=True).data), content_type="application/json")
def login(request):
    try: logout(request)
    except: pass
    if request.method == "PUT":
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
def collection(request, id):
    url = '/collection/' + id
    z = ImageCollection.objects.filter(pk=url).first()
    if z:
        retval = ImageCollectionSerializer(z).data
        retval['type'] = 'image'
        return HttpResponse(JSONRenderer().render(retval), content_type="application/json")
    z = DocumentCollection.objects.filter(pk=url).first()
    if z:
        retval = DocumentCollectionSerializer(z).data
        retval['type'] = 'document'
        return HttpResponse(JSONRenderer().render(retval), content_type="application/json")
    z = VideoCollection.objects.filter(pk=url).first()
    if z:
        retval = VideoCollectionSerializer(z).data
        retval['type'] = 'video'
        return HttpResponse(JSONRenderer().render(retval), content_type="application/json")
def word_part(request, entry):
    url = '/word-part/' + entry
    z = WordPart.objects.get(pk=url)
    retval = WordPartSerializer(z).data
    return HttpResponse(JSONRenderer().render(retval), content_type="application/json")

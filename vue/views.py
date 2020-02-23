from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from conjugator.htmlmaker import conj_call
from conjugator.morphemes import ojibwe_lev, todoublevowel
from django.core import serializers
from dictionary.models import *
from rest_framework.renderers import JSONRenderer
from django.contrib.auth import authenticate, login as authlogin, logout
from django.contrib.auth.decorators import login_required
from dictionary.serializers import *
import django.middleware.csrf
import re
import json
from itertools import chain


def homepage(request):
    return render(request, "dictionary/base-vue.html")


def get_lookup_field(type, scope, field):
    retval = "head_lemma"
    if type == "ojibwe":
        return retval
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
    else:
        return retval


def regular_search(request):
    query = request.GET.get('q')
    type = request.GET.get('type')
    query, type, scope, field, page = map(request.GET.get,
                                    ['q', 'type', 'scope', 'field', 'page'])
    if not page: page = 0
    page = int(page)
    if type in ['ojibwe', 'main_entry']:
        if scope == "inexact":
            all = MainEntry.objects.filter()
            dvquery = todoublevowel(query)
            all = [a for a in all if a.head_lemma]
            entries = [a for a in all
                       if ojibwe_lev(todoublevowel(a.head_lemma),
                                     dvquery) < 10]
        else:
            lf = get_lookup_field(type, scope, field)
            entries = MainEntry.objects.filter(**{lf: query})
        return HttpResponse(
                            JSONRenderer().render(
                                SearchLinkSerializer(entries[page*50:(page+1)*50], many=True).data),
                            content_type="application/json")
    elif type == "english":
        all = Keyword.objects.all()
        entries = set([a for a in all if
                      re.search(rf"\b{re.escape(query)}\b", a.name)])
        return HttpResponse(
                            JSONRenderer().render(
                                KeywordSerializer(entries[page*10:(page+1)*10], many=True).data),
                            content_type="application/json")
    elif type == "collections":
        iall = ImageCollection.objects.all()
        vall = VideoCollection.objects.all()
        dall = DocumentCollection.objects.all()
        all = chain(iall, vall, dall)
        retval = [a for a in all if query in str(a.title) or query in str(a.description)]
        return HttpResponse(
                            JSONRenderer().render(
                                GenericCollectionLinkSerializer(
                                    retval[page*50:(page+1)*50],
                                    many=True).data),
                                content_type="application/json")


def main_entry(request, entry):
    m_e = MainEntry.objects.get(pk="/main-entry/" + entry)
    conjugation = None
    if (m_e.stem and m_e.part_of_speech and
    m_e.part_of_speech.abbrev in ['vai', 'vti', 'vti2', 'vta', 'vii']):
            conjugation = conj_call(m_e)
    m_e = MainEntrySerializer(m_e).data
    m_e['conjugation'] = conjugation
    return HttpResponse(JSONRenderer().render(m_e),
                        content_type="application/json")


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
        if user is not None:
            authlogin(request, user)
            if user.is_active:
                return HttpResponse('{"value":"yes"}',content_type="application/json")
    return HttpResponse('{"value":"no"}', content_type="application/json")


def logout_(request):
    if request.method == "POST":
        logout(request)
        return HttpResponse("yes")
    return HttpResponse("no")


def collection(request, id):
    url = '/collection/' + id
    z = ImageCollection.objects.filter(pk=url).first()
    if z:
        retval = ImageCollectionSerializer(z).data
        return HttpResponse(
            JSONRenderer().render(retval),
            content_type="application/json")
    z = DocumentCollection.objects.filter(pk=url).first()
    if z:
        retval = DocumentCollectionSerializer(z).data
        return HttpResponse(
            JSONRenderer().render(retval),
            content_type="application/json")
    z = VideoCollection.objects.filter(pk=url).first()
    if z:
        retval = VideoCollectionSerializer(z).data
        return HttpResponse(
            JSONRenderer().render(retval),
            content_type="application/json")


def word_part(request, entry):
    url = '/word-part/' + entry
    z = WordPart.objects.get(pk=url)
    retval = WordPartSerializer(z).data
    return HttpResponse(JSONRenderer().render(retval), content_type="application/json")


def am_i_authenticated(request):
    if request.user.is_authenticated:
        return HttpResponse('{"value":"yes"}',content_type="application/json")
    else:
        return HttpResponse('{"value":"no"}',content_type="application/json")


@login_required
def history(request):
    e = ""
    if request.method == "POST":
        try:
            entry = MainEntry.objects.get(e.data['historic'])
            history = entry.historic
            old_head = historic.head
            old_head.url = old_head.old_url
            old_head.save()
            entry.url = entry.old_url
            entry.indexed = True
            entry.save()
            history.historic = entry.url
            history.head = entry
            history.save()

            return HttpResponse("yes")
        except Exception as e: print(e)
    return HttpResponse(repr(e))

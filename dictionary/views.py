from django.shortcuts import render
from .models import MainEntry, Speaker, PartOfSpeech
from django.http import HttpResponse, JsonResponse
from django.template import Context
from conjugator.htmlmaker import conj_call
from conjugator.morphemes import ojibwe_lev, todoublevowel
from django.core import serializers

import re
import json


def homepage(request):
    context = {"main": True}
    return render(request, "dictionary/base.html", context)


def main_entry(resquest, entry):
    m_e = MainEntry.objects.get(pk="/main-entry/" + entry)
    conjugation = conj_call(m_e)
    context = {"entry": m_e, "conjugation": conjugation}
    return render(request, "dictionary/main-entry.html", context=context)


def regular_search(request):
    query = request.GET.get('q')
    type = request.GET.get('type')
    if type == 'ojibwe':
        entries = MainEntry.objects.filter(head_lemma=query)
    else:
        all = MainEntry.objects.all()
        entries = [a for a in all if
                   re.search(rf"\b{re.escape(query)}\b", a.gloss)]
    context = {"entries": entries}
    return render(request, "dictionary/search-result.html", context=context)


def advanced_search_front(request):
    class ANY:
        def __eq__(self, val): return True
    query = request.GET.get('q')
    type = request.GET.get('type')
    scope = request.GET.get('scope')

    scope_name = {"starts_width": "start with",
                  "contains": "contains",
                  "ends_with": "ends with",
                  "exact": "exact match"}.get(scope)
    if type == "main_entry":
        part_of_speech = request.GET.get('partofspeech')
        if not part_of_speech:
            part_of_speech = ANY
        all = MainEntry.objects.all()
        all = [a for a in all if a.head_lemma and a.part_of_speech is not None]
        all = [a for a in all if a.part_of_speech.abbrev == part_of_speech]
        if scope == "starts_with":
            entries = [a for a in all if a.head_lemma.startswith(query)]
        elif scope == "inexact":
            dvquery = todoublevowel(query)
            entries = [a for a in all
                       if ojibwe_lev(todoublevowel(a.head_lemma),
                                     dvquery) < 10]
        elif scope == "ends_with":
            entries = [a for a in all if a.head_lemma.endswith(query)]
        elif scope == "contains":
            entries = [a for a in all if query in a.head_lemma]
        elif scope == "exact":
            entries = MainEntry.objects.filter(head_lemma=query)
        context = {"entries": entries,
                   "scope": scope,
                   "type": type}
        return render(request, "dictionary/advanced-search.html",
                      context=context)
    return render(request, "dictionary/advanced-search.html")


def speaker(request, speaker):
    speakerurl = "/speaker/" + speaker
    speaker = Speaker.objects.get(pk=speakerurl)
    context = {"speaker": speaker}
    return render(request, "dictionary/speaker-popup.html", context=context)


def ojibwe_parts_of_speech(request):
    parts_of_speech = PartOfSpeech.objects.all()
    context = {"parts_of_speech": parts_of_speech}
    return render(request, "dictionary/help/ojibwe-parts-of-speech.html",
                  context)


def small_link(request, entry):
    m_e = MainEntry.objects.get(pk="/main-entry/" + entry)
    regions = [{"abbrev": region.abbrev,
                "full": region.full} for region in m_e.region.all()]
    return HttpResponse(json.dumps({
        "url": m_e.url,
        "head_lemma": m_e.head_lemma,
        "part_of_speech": {
            "abbrev": m_e.part_of_speech.abbrev,
            "full": m_e.part_of_speech.full},
        "regions": regions
        }), content_type="application/json")


def seekrit(request):
    if request.user.is_authenticated:
        return HttpResponse('The seekrit is yours to behold')
    else: return HttpResponse('This seekrit is not meant for thine eyes')

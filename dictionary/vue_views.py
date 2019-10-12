import json
from django.http import HttpResponse
from dictionary.models import MainEntry
from rest_framework.renderers import JSONRenderer
from .serializers import *
import re
def search(request):
  query = request.GET.get('q')
  type = request.GET.get('type')
  if type == 'ojibwe':
      entries = MainEntry.objects.filter(head_lemma=query)
  else:
      all = MainEntry.objects.all()
      entries = [a for a in all if
                 re.search(rf"\b{re.escape(query)}\b", a.gloss)]
  return HttpResponse(JSONRenderer().render(SearchLinkSerializer(entries, many=True).data), content_type="application/json")

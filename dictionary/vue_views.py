import json
from django.http import HttpResponse
from dictionary.models import MainEntry
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
  return HttpResponse(json.dumps([
  small_link_json(entry) for entry in entries
  ]), content_type="application/json")
def small_link_json(m_e):

     return {"url": m_e.url,
          "head_lemma": m_e.head_lemma,
          "regions": [{"abbrev": r.abbrev,
                    "full": r.full} for r in m_e.region.all() if r is not None]
         }

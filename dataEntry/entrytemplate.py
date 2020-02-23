#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 16:44:09 2019

@author: jacobsolinsky
"""
import os
import json
from functools import partial, lru_cache
from fuzzywuzzy import fuzz 


os.chdir("/Users/jacobsolinsky/programming/ojibwe")

class h:
    @staticmethod
    def htmlfunc(tag, contents, **kwargs):
        return f"<{tag} {' '.join([key + '=' + value for key, value in kwargs.items()])}>{contents}</{tag}>"
    def __getattr__(self, attr):
        print(attr)
        return partial(object.__getattribute__(self, "htmlfunc"), attr)
h = h()
with open("all_entries.json") as f:
    ed = json.load(f)
with open("all_word_part_entries.json") as f:
    wp = json.load(f)
with open("parts_of_speech.json") as f:
    ps = json.load(f)

def index_related_words(entries):
    related_words_dict = {}
    for entry in entries:
        related_words = entry['related_words']
        if related_words is not None:
            if related_words['title'] not in related_words_dict:
                related_words_dict[related_words['title']] = \
                RelatedWords(related_words['title'], related_words['words'])
    return related_words_dict

class WordFamily:
    def __init__(self, head, members):
        self.head = head
        self.members = members

def head_in_members(word_family):
        head = word_family['head']
        print(word_family)
        for _, member in word_family['members']:
            if head == member:
                return True
        return False
def index_word_family(entries):
    word_family_dict = {}
    for entry in entries:
        word_family = entry['word_family']
        if word_family is not None:
            if word_family['head'] not in word_family_dict and not \
            head_in_members(word_family):
                word_family_dict[word_family['head']] = \
                WordFamily(word_family['head'], word_family['members'])
    return word_family_dict

def reindex_word_families(entries, word_families):
    for entry in entries:
        eword_family = entry['word_family']
        if eword_family is not None:
            if head_in_members(eword_family):
                for word_family in word_families.values():
                    if word_family.__dict__['members'] == eword_family['members']:
                        eword_family['members'] = word_family.__dict__
class RelatedWords:
    def __init__(self, title, words):
        self.title = title
        self.words = words
class di:
    def __init__(self, dict_):
        self.__dict__.update(dict_)
        
class DictionaryHtml:
    @property
    @lru_cache()
    def entries(self):
        with open("all_entries.json") as f:
            return json.load(f)
    @property
    @lru_cache()
    def word_parts(self):
        with open("all_word_parts.json") as f:
            return json.load(f)
    @property 
    @lru_cache()
    def parts_of_speech(self):
        with open("parts_of_speech.json") as f:
            return json.load(f)
    @property 
    @lru_cache()
    def entry_lemmas(self):
        return [entry['head_lemma'] for entry in self.entries]
            
    def get_by_url(self, url):
        for entry in self.entries:
                if entry['url'] == url:
                    return entry
    def fuzzy_search(self, searchterm):
        return [entry for entry in self.entries if fuzz.ratio(entry['head_lemma'], searchterm) > 80]
        
    def get_by_lemma(self, *lemmas):
        return [entry for entry in self.entries if entry['head_lemma'] in lemmas]

    def get_pos_fullname(self, pos):
        return self.parts_of_speech[pos][1]
        
    def entry_link_html(self, entry_url):
        entry = self.get_by_url(entry_url)
        return f'''<span class="main-entry-title">
          <span class="lemma"><a href="{entry['url']}">{entry['head_lemma']}</a></span>
          <span class="badge badge-oj" data-toggle="tooltip" data-placement="right" title="" data-original-title="{self.get_pos_fullname(entry['part_of_speech'])}">{entry['part_of_speech']}</span>
        </span>'''
    def full_link_html(self, entry_url):
        return self.entry_link_html(entry_url) + self.get_glosses(entry_url)
    def search_link_html(self, entry_url, ):
        def search_word_family(self, entry):
            if entry['word_family'] and entry['url'] not in []:
                retval = []
                for member in entry['word_family']['members']:
                    memberentry = self.get_by_url(member[1])
                    kind = member[0]
                    retval.append(f"""<span class="word-family-child "><span class="main-entry-title">
      {kind}
      <span class="lemma"><a href="{member[1]}">{memberentry['head_lemma']}</a></span>
      <span class="badge badge-oj" data-toggle="tooltip" data-placement="right" title="" data-original-title="transitive animate verb">
        {memberentry['part_of_speech']}
      </span>
      
    </span>{self.get_glosses(member[1])}</span>""")
                retval = ''.join(retval)
                return f"""<div class="item-list">
<div class="indent">{retval}</div>  </div>"""
            else:
                return ''
        def search_paired_with(self, entry):
            if entry['paired_with']:
                return f"""<p class="relations">
      
      <em>Paired with:</em> {self.entry_link_html(entry['paired_with'])}
      
  </p>"""
            else:
                return ''
        entry = self.get_by_url(entry_url)
        main = self.full_link_html(entry_url)
        audio_glyphicon = """<span class="badges"><span class="glyphicon glyphicon-volume-up"></span></span>""" if entry['head_audio'] else ''
        wf_html = search_word_family(self, entry)
        pw_html = search_paired_with(self, entry)
        return '<div class ="main-entry-search">' + main + audio_glyphicon + wf_html + pw_html +'</div>'

    def get_glosses(self, entry_url):
        entry = self.get_by_url(entry_url)
        if entry['gloss'] != ['']:
            return entry['gloss'][0]
        elif entry['gloss_list'] != []:
            lilist = ''.join([f"<li>{glossentry}</li>" for glossentry in entry['gloss_list']])
            return f'<ol class="word-family-glosses">{lilist}</ol>'
    def make_search_page(self, entry_urls):
        searchlist = []
        for entry_url in entry_urls:
            searchlist.append(search_link_html(entry_url))
        return ''.join(searchlist)
        
    
    

    
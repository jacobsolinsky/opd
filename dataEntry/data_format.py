#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 12:42:46 2019

@author: jacobsolinsky
"""
import json
import lxml
from lxml import html
from lxml import etree
from lxml.cssselect import CSSSelector
import requests
with open('/Users/jacobsolinsky/programming/ojibwe/all_entries3.json') as f:
    entries = json.load(f)

'''
entry {
url
head_lemma
foreign_key part of speech -> abbrev
species
notes
foreign_key head_speaker -> href
foreign_key head_audio -> regular
foreign_key head_image -> src
gloss
inv_foreign_key <- inflectional_forms url
inv_foreign_key <- audio_for_basic_forms url
inv_foreign_key <- audio_for_additional_forms url
inv_foreign_key <- example_sentences url
reduplication
inv_foreign_key regions
many paired_with url <-> url
many see_also url <-> url
many redirect url <-> url
}
#%%
'''
def strip_galleries():
    image_collections = []
    video_collections = []
    document_collections = []
    with open("/Users/jacobsolinsky/programming/opd/opd/data/galleries.json") as f:
        gries = json.load(f)
    for gri in gries:
        if gri['type'] == "image":
            if gri not in image_collections: image_collections.append(gri)
        elif gri['type'] == "video":
            if gri not in video_collections: video_collections.append(gri)
        elif gri['type'] == "document":
            if gri not in document_collections: document_collections.append(gri)
    return (image_collections,video_collections,document_collections)
image_collections,video_collections,document_collections = strip_galleries()
def strip_part_of_speech(entries):
    retval = []
    retval2 = []
    for entry in entries:
        if not entry['part_of_speech']: continue
        retval2.append({'url': entry['url'], 'abbrev':entry['part_of_speech']['abbrev']})
        if entry['part_of_speech'] not in retval:
            retval.append(entry['part_of_speech'])
        entry['part_of_speech'] = entry['part_of_speech']['abbrev']
    return retval, retval2
parts_of_speech, entry_part_of_speech = strip_part_of_speech(entries)
        
'''
entry_part_of_speech {
url 
abbrev
}
#%%
part_of_speech {
abbrev
full
}
'''

'''
#%%
entry_speaker {
url
href
}
#%%
speaker{
href
initials
primary_name
full_name
description
}
'''
def strip_head_audio(entries):
    retval = []
    retval2 = []
    for entry in entries:
        if not entry['head_audio']: continue
        retval2.append({'url': entry['url'], 'regular': entry['head_audio']['regular']})
        if entry['head_audio']['regular'] not in retval:
            retval.append(entry['head_audio'])
        entry['head_audio'] = entry['head_audio']['regular']
    return retval, retval2
audios, entry_audio = strip_head_audio(entries)
'''
#%%
entry_audio {
url
regular
}
#%%
audio {
regular 
mobile
}
'''
def strip_head_image(entries):
    retval = []
    retval2 = []
    for entry in entries:
        if not entry['head_image']: continue
        retval2.append({'url': entry['url'], 'src': entry['head_image']['src']})
        if entry ['head_image']  not in retval:
            retval.append(entry['head_image'])
        entry['head_image'] = entry['head_image']['src']
    return retval, retval2
images, entry_image = strip_head_image(entries)
'''
#%%
entry_image {
url
src
}
#%%
image {
src
alt
}
'''
def strip_word_family(entries):
    retval = []
    for entry in entries:
        if not entry['word_family']:
                entry.pop('word_family', None)
                continue
        for member in entry['word_family']['members']:
            a = {'head_url': entry['word_family']['head'],
                               'kind': member[0],
                               'member_url': member[1]}
            if a not in retval:
                retval.append(a)
        entry['word_family'] = entry['word_family']['head']
    return retval
word_families = strip_word_family(entries)
            
'''
#%% 
word_family{
head_url
kind
member_url
}'''
def strip_related_words(entries):
    retval = {}
    for entry in entries:
        if not entry['related_words']: 
            entry.pop('related_words', None)
            continue
        retval[entry['related_words']['title']] = entry['related_words']['words']
        entry['related_words'] = entry['related_words']['title']
    return retval
related_words = strip_related_words(entries)
                
'''
#%%
related_words{
title
member_url
}
'''
def strip_inflectional_forms(entries):
    retval = []
    retval2 = []
    retval3 = []
    inflectional_forms_index = 1
    for entry in entries:
        if not entry['inflectional_forms']: 
            entry.pop('inflectional_forms', None)
            continue
        entry['stem'] = entry['inflectional_forms']['stem']
        for form in entry['inflectional_forms']['forms']:
            retval.append({'url': entry['url'],
                'form': form['form'],
                'inflectional_forms_index': inflectional_forms_index})
            for pos in form['pos_list']:
                if pos not in retval2: retval2.append(pos)
                retval3.append({'inflectional_forms_index': inflectional_forms_index,
                                'abbrev': pos['abbrev']})
            inflectional_forms_index += 1
        entry.pop('inflectional_forms', None)
    return retval, retval2, retval3
inflectional_forms, poss, inflectional_form_pos = strip_inflectional_forms(entries)
'''
#%%
inflectional_forms {
foreign_key url -> entry
form
inflectional_forms_index
inv_foreign_key pos <- inflectional_forms_index
}
#%% 
inflectional_form_pos {
foreign_key inflectional_forms_index -> inflectional_forms
abbrev
}
#%%
pos {
abbrev
full
}
'''
def strip_audio_for_basic_forms(entries, audios, poss):
    retval = []
    retval2 = []
    retval3 = []
    audio_for_basic_forms_index = 1
    for entry in entries:
        if not entry['audio_for_basic_forms']:
            entry.pop('audio_for_basic_forms', None)
            continue
        for audio_form in entry['audio_for_basic_forms']:
            retval.append({'url': entry['url'],
                           'ojibwe': audio_form['ojibwe'],
                           'audio_for_basic_forms_index': audio_for_basic_forms_index
                    })
            for audio_rec in audio_form['audios']:
                retval2.append({'href': audio_rec['speaker'],
                                'audio': audio_rec['audio']['regular'],
                                'audio_for_basic_forms_index': audio_for_basic_forms_index
                        })
                audios.append(audio_rec['audio'])
            for pos in audio_form['pos_list']:
                if pos not in poss: poss.append(pos)
                retval3.append({'audio_for_basic_forms_index': audio_for_basic_forms_index,
                                'abbrev': pos['abbrev']})
            audio_for_basic_forms_index += 1
        entry.pop('audio_for_basic_forms', None)
    return retval, retval2, retval3
audio_for_basic_forms, audio_for_basic_form_audio_rec, audio_for_basic_form_pos = strip_audio_for_basic_forms(entries, audios, poss)
'''
#%%
audio_for_basic_forms {
english
ojibwe
audio_for_basic_forms_index
inv_foreign_key audio_rec <- audio_for_basic_forms_index
}
'''
def strip_additional_audio(entries, audios, poss):
    retval = []
    retval2 = []
    retval3 = []
    additional_audio_index = 1
    for entry in entries:
        if not entry['additional_audio']:
            entry.pop('additional_audio', None)
            continue
        for audio_form in entry['additional_audio']:
            retval.append({'url': entry['url'],
                           'ojibwe': audio_form['ojibwe'],
                           'additional_audio_index': additional_audio_index
                    })
            for audio_rec in audio_form['audios']:
                retval2.append({'href': audio_rec['speaker'],
                                'audio': audio_rec['audio']['regular'],
                                'additional_audio_index': additional_audio_index
                        })
                audios.append(audio_rec['audio'])
            for pos in audio_form['pos_list']:
                if pos not in poss: poss.append(pos)
                retval3.append({'additional_audio_index': additional_audio_index,
                                'abbrev': pos['abbrev']})
            additional_audio_index += 1
        entry.pop('additional_audio', None)
    return retval, retval2, retval3
additional_audio, additional_audio_audio_rec, additional_audio_pos = strip_additional_audio(entries, audios, poss)
'''
#%%
additional_audio {
english
ojibwe
additional_audio_index
inv_foreign_key audio_rec <- additional_audio_index
}
#%% 
audio_rec {
foreign_key audio_for_basic_forms_index -> audio_for_basic_forms
foreign_key additional_audio_index -> additional_audio
foreign_key sentence_example_index -> sentence_example
foreign_key regular -> audio
foreign_key speaker -> href
}
'''
def strip_sentence_examples(entries, audios):
    retval = []
    retval2 = []
    sentence_examples_index = 1
    for entry in entries:
        if not entry['sentence_examples']:
            entry.pop('sentence_examples', None)
            continue
        for audio_form in entry['sentence_examples']:
            retval.append({'url': entry['url'],
                           'english': audio_form['english'],
                           'ojibwe': audio_form['ojibwe'],
                           'sentence_examples_index': sentence_examples_index
                    })
            audio_rec = audio_form
            retval2.append({'href': audio_rec['speaker'],
                                'audio': audio_rec['audio']['regular'] if audio_rec['audio'] else None,
                                'sentence_examples_index': sentence_examples_index
                        })
            audios.append(audio_rec['audio'])
            sentence_examples_index += 1
        entry.pop('sentence_examples', None)
    return retval, retval2
sentence_examples, sentence_example_audio_rec = strip_sentence_examples(entries, audios)
'''
#%%
sentence_example {
foreign_key entry -> url
english
ojibwe
sentence_example_index
inv_foreign_key audio_rec <- sentence_example_index
}
'''
def strip_regions(entries):
    retval = []
    retval2 = []
    for entry in entries:
        if not entry['regions']:
            entry.pop('regions', None)
            continue
        for region in entry['regions']:
            if region not in retval:
                retval.append(region)
            retval2.append({'url': entry['url'], 'abbrev': region['abbrev']})
        entry.pop('regions', None)
    return retval, retval2
regions, entry_region = strip_regions(entries)
'''
entry_regions {
foreign_key entry -> url
foreign_key region -> abbrev
}
'''
def strip_paired_with(entries):
    retval = []
    for entry in entries:
        if not entry['paired_with']:
            entry.pop('paired_with', None)
            continue
        for paired_with in entry['paired_with']:
            a = [entry['url'], paired_with]
            if a not in retval:
                retval.append(a)
        entry.pop('paired_with', None)
    return retval
entry_entry_paired_with = strip_paired_with(entries)

def strip_see_also(entries):
    retval = []
    for entry in entries:
        if not entry['see_also']:
            entry.pop('see_also', None)
            continue
        for see_also in entry['see_also']:
            a = [entry['url'], see_also]
            if a not in retval:
                retval.append(a)
        entry.pop('see_also', None)
    return retval
entry_entry_see_also = strip_see_also(entries)

def strip_redirect(entries):
    retval = []
    for entry in entries:
        if not entry['redirect']:
            entry.pop('redirect', None)
            continue
        for redirect in entry['redirect']:
            a = [entry['url'], redirect]
            if a not in retval:
                retval.append(a)
        entry.pop('redirect', None)
    return retval
entry_entry_redirect = strip_redirect(entries)
            
            
'''
entry_entry_paired_with {
foreign_key entry1 -> url
foreign_key entry2 -> url
}
entry_entry_see_also {
foreign_key entry1 -> url
foreign_key entry2 -> url
}
entry_entry_redirect {
foreign_key entry1 -> url
foreign_key entry2 -> url
}
entry_image_resource {
foreign_key entry -> url
foreign_key image_resource -> leftsrc
}
entry_video_resource {
foreign_key entry -> url
foreign_key video_resource -> leftsrc
}
entry_document_resource {
foreign_key entry -> url
foreign_key document_resource -> leftsrc
}
'''
def strip_image_resources(entries, images):
    retval = []
    for entry in entries:
        if not entry['related_resources']:
            continue
        il = entry['related_resources']['imagelist']
        for ill in il:
            if ill['image'] not in images:
                images.append(ill['image'])
            retval.append({
                    'url': entry['url'],
                    'image': ill['image']['src'],
                    'righthref': ill['righthref'],
                    'righttext': ill['righttext']
                    })
    return retval
image_resources = strip_image_resources(entries, images)
def strip_video_resources(entries, images):
    retval = []
    for entry in entries:
        if not entry['related_resources']:
            continue
        il = entry['related_resources']['videolist']
        for ill in il:
            if ill['image'] not in images:
                images.append(ill['image'])
            retval.append({
                    'url': entry['url'],
                    'image': ill['image']['src'],
                    'righthref': ill['righthref'],
                    'righttext': ill['righttext']
                    })
    return retval
video_resources = strip_video_resources(entries, images)
def strip_document_resources(entries):
    retval = []
    for entry in entries:
        if not entry['related_resources']:
            entry.pop('related_resources')
            continue
        il = entry['related_resources']['documentlist']
        for ill in il:
            retval.append({
                    'url': entry['url'],
                    'righthref': ill['righthref'],
                    'righttext': ill['righttext']
                    })
        entry.pop('related_resources')
    return retval
document_resources = strip_document_resources(entries)
def scrape_speakers(images):
    doc = html.fromstring(requests.get('https://ojibwe.lib.umn.edu/about/voices').text)
    doc = CSSSelector("div.col-md-9.col-sm-9.content")(doc)[0]
    speakers = CSSSelector("div.voice.row.full-row")(doc)
    retval = []
    for speaker in speakers:
        image = CSSSelector("img.voice-image")(speaker)[0]
        imagesrc = image.attrib.get('src')
        imagealt = image.attrib.get('alt')
        image = {'src': imagesrc, 'alt': imagealt}
        if image not in images: images.append(image)
        voice_info_fields = CSSSelector("div.voice-info-field span.voice-field")(speaker)
        ojibwe, english, community, region = [vif.text for vif in voice_info_fields]
        primary = CSSSelector("h2")(speaker)[0].text.strip()
        initials = CSSSelector("h2 div")(speaker)[0].text.strip()
        description = ''.join([etree.tounicode(p, with_tail=False)
        for p in CSSSelector("p")(speaker)])
        url = '/speaker/' + ''.join([
                L if L != " " else "-" for L in primary.lower() 
                ])
        retval.append({"primary_name": primary,
                       "ojibwe_name": ojibwe,
                       "english_name": english,
                       "initials": initials,
                       "image": image,
                       "community": community,
                       "region": region,
                       "description": description,
                       "href": url})
    return retval
speakers = scrape_speakers(images)
    
            
    
'''
image_resource {
leftsrc
foreign_key image -> src
righthref
rightsrc
}
video_resource {
leftsrc
foreign_key video -> src
righthref
rightsrc
}
document_resource {
leftsrc
righthref
rightsrc
}
video {
src
foreign_key image -> src
}
'''
for name in ("entries", "parts_of_speech", "entry_part_of_speech","audios", "entry_audio", "images", "entry_image",
             "word_families", "related_words","inflectional_forms", "poss", "inflectional_form_pos",
             "audio_for_basic_forms", "audio_for_basic_form_audio_rec", "audio_for_basic_form_pos",
             "additional_audio", "additional_audio_audio_rec", "additional_audio_pos",
             "sentence_examples", "sentence_example_audio_rec",
             "regions", "entry_region", "entry_entry_paired_with",
             "entry_entry_see_also", "entry_entry_redirect",
             "image_resources", "video_resources", "document_resources", "speakers",
             "image_collections", "video_collections", "document_collections"):
    with open(f"/Users/jacobsolinsky/programming/opd/opd/database/{name}.json", "w+") as f:
        json.dump(eval(name), f)
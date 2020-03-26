#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 17:19:40 2019

@author: jacobsolinsky
"""
from dictionary.models import MainEntry, PartOfSpeech, Audio, Image, WordFamily, RelatedWord, InflectionalForm, Poss, AudioForBasicForm, AdditionalAudio, SentenceExample, AudioForBasicFormAudioRec, AdditionalAudioAudioRec, SentenceExampleAudioRec, Region, ImageResource, VideoResource, DocumentResource, Speaker, VideoCollection, ImageCollection, DocumentCollection, Video, News, WordFamilyPair, Keyword, KeywordGroup, WordPart
import json
for name in ("entries", "parts_of_speech", "entry_part_of_speech","audios", "entry_audio", "images", "entry_image",
             "word_families", "related_words","inflectional_forms", "poss", "inflectional_form_pos",
             "audio_for_basic_forms", "audio_for_basic_form_audio_rec", "audio_for_basic_form_pos",
             "additional_audio", "additional_audio_audio_rec", "additional_audio_pos",
             "sentence_examples", "sentence_example_audio_rec",
             "regions", "entry_region", "entry_entry_paired_with",
             "entry_entry_see_also", "entry_entry_redirect",
             "image_resources", "video_resources", "document_resources", "speakers",
             "video_collections", "image_collections", "document_collections", "videos", "news", "keywords",
             ):
    with open(f"/home/ec2-user/opd/opd/database/{name}.json") as f:
        exec(f"{name} = json.load(f)")
        thing = eval(name)
        for i in eval(name):
            if i is None:
                thing.remove(i)



for i in parts_of_speech:
    a = PartOfSpeech(abbrev = i["abbrev"],
                     full = i['full'])
    a.save()
#entered to this point

for i in images:
    a = Image(src = i['src'],
              alt = i['alt'])
    a.save()

#entered to this point
for i in videos:
    thumb = Image.objects.get(pk=i['image'])
    a = Video(src = i['src'],
              thumb = thumb)
    a.save()
#entered to this point
for i in audios:
    if i is None: continue
    a = Audio(regular = i['regular'],
              mobile = i['mobile'])
    a.save()
#entered to this point
for i in speakers:
    speakerimage = Image.objects.get(pk=i['image']['src'])
    a = Speaker(
            image=speakerimage,
            href =  i['href'],
            initials =  i["initials"],
            primary_name = i["primary_name"],
            ojibwe_name = i["ojibwe_name"],
            english_name = i["english_name"],
            description = i["description"],
            region = i["region"],
            community = i["community"])
    a.save()
#entered to this point
for i in news:
    a = News(title = i['title'], date = i['date'], html = i['html'])
    a.save()
#entered to this point

#got to this point in amazon
z = 0
for i in entries:
        part_of_speech = PartOfSpeech.objects.filter(pk=i['part_of_speech']).first()
        head_speaker = Speaker.objects.filter(pk=i['head_speaker']).first()
        head_audio = Audio.objects.filter(pk=i['head_audio']).first()
        head_image = Image.objects.filter(pk=i['head_image']).first()
        hs = dictionary.models.HistorySet.objects.create(pk=z)
        hs.save()
        a = MainEntry(url = i['url'],
                      head_lemma = i['head_lemma'],
                      part_of_speech = part_of_speech,
                      head_speaker = head_speaker,
                      head_audio = head_audio,
                      head_image = head_image,
                      history_set = hs,
                      gloss = i['gloss'],
                      notes = i['notes'],
                      reduplication = i['reduplication'],
                      indexed = False,
                      history_set_id=0
                )
        a.save()
        z+= 1
#entered to this point
for e in entry_entry_paired_with:
    a = MainEntry.objects.get(pk=e[0])
    paired_with = MainEntry.objects.get(pk=e[1])
    a.paired_with_inv.add(paired_with)
    a.save()
for e in entry_entry_see_also:
    a = MainEntry.objects.get(pk=e[0])
    see_also = MainEntry.objects.get(pk=e[1])
    a.see_also_inv.add(see_also)
    a.save()
for e in entry_entry_redirect:
    a = MainEntry.objects.get(pk=e[0])
    redirect = MainEntry.objects.get(pk=e[1])
    a.redirect_inv.add(redirect)
    a.save()
#entered to this point

for i in sentence_examples:
    entry = MainEntry.objects.get(pk=i['url'])
    a = SentenceExample(entry = entry,
                        sentence_examples_index = i['sentence_examples_index'],
                        ojibwe = i['ojibwe'],
                        english = i['english'])
    a.save()
#entered to this point
for i in audio_for_basic_forms:
    entry = MainEntry.objects.get(pk=i['url'])
    a = AudioForBasicForm(entry = entry,
                        audio_for_basic_forms_index = i['audio_for_basic_forms_index'],
                        ojibwe = i['ojibwe'])
    a.save()
#entered to this point
for i in additional_audio:
    entry = MainEntry.objects.get(pk=i['url'])
    a = AdditionalAudio(entry = entry,
                        additional_audio_index = i['additional_audio_index'],
                        ojibwe = i['ojibwe'])
    a.save()
#entered to this point
for i in poss:
    a = Poss(abbrev = i['abbrev'],
             full = i['full'])
    a.save()
#entered to this point

for i in sentence_example_audio_rec:
    sentence_example = SentenceExample.objects.filter(pk=i['sentence_examples_index']).first()
    speaker = Speaker.objects.filter(pk=i['href']).first()
    audio = Audio.objects.filter(pk=i['audio']).first()
    a = SentenceExampleAudioRec(sentence_examples_index = sentence_example,
                                speaker = speaker,
                                audio = audio)
    a.save()
#entered to this point

for i in audio_for_basic_form_audio_rec:
    z = Audio(regular = i['audio'])
    audio_for_basic_form = AudioForBasicForm.objects.filter(pk=i['audio_for_basic_forms_index']).first()
    speaker = Speaker.objects.filter(pk=i['href']['href']).first()
    audio = Audio.objects.get(pk=i['audio'])
    a = AudioForBasicFormAudioRec(audio_for_basic_forms_index = audio_for_basic_form,
                                speaker = speaker,
                                audio = audio)
    a.save()
#entered to this point
for i in additional_audio_audio_rec:
    additional_audio = AdditionalAudio.objects.filter(pk=i['additional_audio_index']).first()
    speaker = Speaker.objects.filter(pk=i['href']['href']).first()
    audio = Audio.objects.filter(pk=i['audio']).first()
    a = AdditionalAudioAudioRec(additional_audio_index = additional_audio,
                                speaker = speaker,
                                audio = audio)
    a.save()
#---
for i in audio_for_basic_form_pos:
    audio_for_basic_form = AudioForBasicForm.objects.get(pk = i['audio_for_basic_forms_index'])
    poss = Poss.objects.get(pk=i['abbrev'])
    audio_for_basic_form.poss.add(poss)
    audio_for_basic_form.save()
  #entered to this point
for i in additional_audio_pos:
    additional_audio = AdditionalAudio.objects.get(pk = i['additional_audio_index'])
    poss = Poss.objects.get(pk=i['abbrev'])
    additional_audio.poss.add(poss)
    additional_audio.save()
    #entered to this point
for i in inflectional_forms:
    entry = MainEntry.objects.get(pk=i['url'])
    a = InflectionalForm(url = entry,
                         inflectional_forms_index = i['inflectional_forms_index'],
                         form = i['form'])
    a.save()
    #entered to this point
for i in inflectional_form_pos:
    inflectional_form = InflectionalForm.objects.get(pk=i['inflectional_forms_index'])
    poss = Poss.objects.get(pk=i['abbrev'])
    inflectional_form.poss.add(poss)
    inflectional_form.save()
#entered to this point
for i in image_collections:
    image = Image.objects.filter(pk=i['image']).first()
    a = ImageCollection(url = i['url'],
                        copyright = i['copyright'],
                        title = i['title'],
                        description = i['description'],
                        image = image)
    a.save()
#entered to this point
for i in document_collections:
    a = DocumentCollection(url = i['url'],
                        title = i['title'],
                        description = i['description'],
                        body = i['documentbody'],
                        bibliography = i['bibliography'])
    a.save()
#entered to this point
for i in video_collections:
    try:
        video = Video.objects.get(pk=i['video']['src'])
        print('yes')
    except:
        print(i['video'])
        video = None
    a = VideoCollection(url = i['url'],
                        copyright = i['copyright'],
                        title = i['title'],
                        description = i['description'],
                        video = video)
    a.save()
#entered to this point
for i in image_resources:
    entry = MainEntry.objects.filter(pk=i['url']).first()
    image = Image.objects.filter(pk=i['image']).first()
    righthref = ImageCollection.objects.filter(pk=i['righthref']).first()
    print(righthref)
    a = ImageResource(url = entry,
                         image = image,
                         righthref = righthref,
                         righttext = i['righttext'])
    a.save()
#entered to this point
for i in document_resources:
    entry = MainEntry.objects.filter(pk=i['url']).first()
    righthref = DocumentCollection.objects.get(pk=i['righthref'])
    print(righthref)
    print(righthref is None)
    a = DocumentResource(url = entry,
                      righthref = righthref,
                      righttext = i['righttext'])
    a.save()
#entered to this point
for i in video_resources:
    entry = MainEntry.objects.filter(pk=i['url']).first()
    image = Image.objects.filter(pk=i['image']).first()
    righthref = VideoCollection.objects.filter(pk=i['righthref']).first()
    a = VideoResource(url = entry,
                      image = image,
                      righthref = righthref,
                      righttext = i['righttext'])
    a.save()
#entered to this point

#entered to this point
for i in related_words:
    word = MainEntry.objects.get(pk=i['word'])
    a = RelatedWord(title = i['title'], word = word)
    a.save()
#entered to this point
for i in regions:
    a = Region(abbrev = i['abbrev'],
               full = i['full'],
               description = "")
    a.save()
for i in entry_region:
    r = Region.objects.get(pk=i['abbrev'])
    e = MainEntry.objects.get(pk=i['url'])
    e.region.add(r)
for entry in entries:
    e = MainEntry.objects.get(pk=entry['url'])
    e.stem = entry.get('stem')
    e.save()
with open('/Users/jacobsolinsky/programming/ojibwe/parts_of_speech.json') as f:
    parts_of_speech = json.load(f)
    for i in parts_of_speech:
        a = PartOfSpeech(abbrev=i['abbrev'],
        full=i['label'],
        description = i['description'])
        a.save()


word_family_list = []
for i in word_families:
    if i['head_url'] not in word_family_list: word_family_list.append(i['head_url'])

for i in word_family_list:
    head = MainEntry.objects.get(pk=i)
    a = WordFamily(head=head)
    a.save()
for i in WordFamily.objects.all():
    a = WordFamilyPair(member = i.head, kind = "head")
    a.word_family = i
    a.save()

for i in word_families:
    head_entry = WordFamily.objects.get(pk=i['head_url'])
    word_family = WordFamily.objects.get(pk=head_entry)
    member = MainEntry.objects.get(pk=i['member_url'])
    a = WordFamilyPair(word_family=word_family, member = member, kind = i['kind'])
    a.save()
for i, v in related_words.keys():
    a = RelatedWord(i)
    a.save()
    for word in v:
        e = MainEntry.get(pk=word)
        e.RelatedWord = a
        e.save
for i in entries:
    a = WordFamily.objects.filter(pk=i.get('word_family')).first()
    b = RelatedWord.objects.filter(pk=i.get('related_words')).first()
    c = MainEntry.objects.get(pk=i['url'])
    c.word_family = a
    c.related_words = b
    c.save()
for i in keywords:
    a = Keyword(name = i['title'],
                description = i['description'],
                distinguisher = i['distinguisher'],
                                  pos = i['pos'])
    a.save()
    for j in i['groups']:
        b = KeywordGroup(name = j['title'],
                         keyword = a)
        b.save()
        for k in j['members']:
            e = MainEntry.objects.filter(pk=k).first()
            if e is not None:
                e.keyword_group = b
                e.save()


with open('/Users/jacobsolinsky/programming/opd/opd/database/ojibwe-indexed-urls') as f:
    for url in json.load(f):
        try:
            e = MainEntry.objects.get(pk=url)
            e.indexed = True
            e.save()
        except Exception as e: print(e)
with open('/Users/jacobsolinsky/programming/opd/opd/data/all_word_part_entries.json') as f:
    for i in json.load(f):
        a = WordPart(url = i['url'],
                     title = i['title'],
                     type = i['type'],
                     gloss = i['gloss'],
                     subtypes = i['subtypes'],
                     variants = i['variants'])
        a.save()
        for j in i['words']:
            e = MainEntry.objects.filter(pk=j).first()
            if e is not None: a.words_that_use_this_part.add(e)
        a.save()

rescrape = """/main-entry/ashkibwaa-na
/main-entry/aagwaniitaw-vta
/main-entry/bapasininjii-vta
/main-entry/bimaakwisin-vii
/main-entry/bisoo-pc-interj
/main-entry/gagawaapi-vai
/main-entry/gaachidinamaw-vta
/main-entry/gichiwinan-vti
/main-entry/gidaatabigaadebani-o-vai
/main-entry/ginzhizha-adv-man
/main-entry/giizhapidoon-vti2
/main-entry/giizhapizh-vta
/main-entry/giizhapizhwi-vta
/main-entry/mamadweganaandan-vti
/main-entry/mamibidoon-vti2
/main-entry/mamibizh-vta
/main-entry/mashkawigad-vii
/main-entry/mashkawigizi-vai
/main-entry/mino-bimaadiziwin-ni
/main-entry/miskojaabi-vai
/main-entry/miskokobaa-vii
/main-entry/miskwaasab-n
/main-entry/naanogonendi-vai
/main-entry/naawi-gichigami-adv-loc
/main-entry/nisogonendi-vai
/main-entry/niiyogonendi-vai
/main-entry/niizhogonendi-vai
/main-entry/noosom-vta
/main-entry/okikitaa-vai
/main-entry/zhiishiibidis-ni""".split('\n')

from lxml import etree
from lxml import html
from lxml.cssselect import CSSSelector
import requests
import os
import json
current_directory = "/Users/jacobsolinsky/programming/ojibwe"
os.chdir(current_directory)

build_text_list = etree.XPath("//text()")

#done

def geth(url):
    return html.fromstring(requests.get(url).text)
def index_words(filepath = "words.json"):
    all_urls = []
    sel = CSSSelector("div.main-entry-search"
                   " div.english-search-main-entry"
                   " span.main-entry-title"
                   " span.lemma a")
    for i in range(1, 755):
        print(i)
        entry_list = requests.get(f"https://ojibwe.lib.umn.edu/advanced_search?field=lemma&page={i}&q=&scope=starts_with&submit=Search&type=main_entry")
        entry_list_tree = html.fromstring(entry_list.text)
        all_word_links = sel(entry_list_tree)
        for link in all_word_links:
            all_urls.append(link.attrib.get('href'))
    with open(filepath, "w+") as f:
        json.dump(all_urls, f)

#done
def index_word_parts(filepath = "wordparts.json"):
    all_urls = []
    sel = CSSSelector("div.container-fluid"
                       " div.row.content-container"
                       " div.col-md-9.col-sm-9.content"
                       " div.search-results"
                       " div.word-part-search-result"
                       " a")
    for i in range(1, 80):
        print(i)
        entry_list = requests.get(f"https://ojibwe.lib.umn.edu/advanced_search?field=form&page={i}&q=&scope=starts_with&submit=Search&type=word_part")
        entry_list_tree = html.fromstring(entry_list.text)
        all_word_links = sel(entry_list_tree)
        for link in all_word_links:
            all_urls.append(link.attrib.get('href'))
    with open(filepath, "w+") as f:
        json.dump(all_urls, f)

#verified
def get_head_lemma(doc):
    try: return CSSSelector("h3 span.lemma")(doc)[0].text 
    except IndexError: pass

#verified
def get_part_of_speech(doc):
    try:
        pos_ = CSSSelector("h3 span.badge.badge-oj")(doc)[0]
        return PartOfSpeech(pos_.text, pos_.attrib.get('title'))
    except IndexError : pass
class PartOfSpeech:
    def __init__(self, abbrev, full):
        self.abbrev = abbrev
        self.full = full


def get_species(doc):
    try: return etree.tounicode(doc.xpath("./div[@class='stylized-text'][not(preceding-sibling::strong[1][text()='Note:'])]")[0],
                          with_tail = False)
    except IndexError: pass

def get_notes(doc):
    try: return etree.tounicode(doc.xpath("./div[@class='stylized-text'][preceding-sibling::strong[1][text()='Note:']]")[0],
                          with_tail = False)
    except IndexError: pass


class Species:
    def __init__(self, string, type):
        self.string = string
        self.type = type

#verified
def get_head_speaker(doc):
    try: return CSSSelector("h3 a.speaker-initials")(doc)[0].attrib.get('href')
    except IndexError: pass

#verified
def get_head_audio(doc):
    try:
        audio_form = CSSSelector(("h3"
                               " span.badge.badge-oj.badge-audio-player"
                               " div.audio-player"))(doc)[0]
        regular_audio = audio_form.attrib.get('data-file')
        mobile_audio = audio_form.attrib.get('data-mobile-file')
        return Audio(regular_audio, mobile_audio)
    except IndexError: pass

#verified
def get_head_image(doc):
    try:
        image = CSSSelector((" div.pull-right.index-photo img"))(doc)[0]
        return Image(image.attrib.get('src'), image.attrib.get('alt'))
    except IndexError: pass
class Image:
    def __init__(self, src, alt):
        self.src = src
        self.alt = alt

#verified
def get_word_family(sidebar):
    try:
        word_family = CSSSelector("div.word-family")(sidebar)[0]
        head = CSSSelector("span.word-family-child"
                           " span.main-entry-title"
                           " span.lemma a")(word_family)[0].attrib.get('href')
        link_s = CSSSelector("div.indent"
                             " span.word-family-child"
                             " span.main-entry-title"
                             " span.lemma a")(word_family)
        kind_s = CSSSelector("div.indent"
                             " span.word-family-child"
                             " span.main-entry-title")(word_family)
        memberlist = []
        for kind, link in zip(kind_s, link_s):
            kind = kind.text.strip()
            link = link.attrib.get('href')
            memberlist.append((kind, link))
        return WordFamily(head, memberlist)
    except IndexError: pass
class WordFamily:
    def __init__(self, head, members):
        self.head = head
        self.members = members

#verified
def get_related_words(sidebar):
    try:
        link_s = CSSSelector(" span.main-entry-title"
                             " span.lemma a")(sidebar)
        family_title = CSSSelector("div.container-fluid"
                                   " div.row.content-container"
                                   " div.col-md-3.col-sm-3.sidebar"
                                   " div.stylized-text")(sidebar)[0].text
        family_members_list = []
        for link in link_s:
            family_members_list.append(link.attrib.get('href'))
        return RelatedWords(family_title, family_members_list)
    except IndexError: pass
class RelatedWords:
    def __init__(self, title, words):
        self.title = title
        self.words = words

def get_gloss(doc):
    try:
        glosses_1 = ''.join([etree.tounicode(p, with_tail=False) for p in
                CSSSelector("p.glosses")(doc)])
    except IndexError: glosses_1 = ""
    try:
        glosses_2 = etree.tounicode(CSSSelector("ol.word-family-glosses")(doc)[0],
                                    with_tail = False)
    except IndexError: glosses_2 = ""
    return glosses_1 + glosses_2


def get_inflectional_forms(doc):
    try:
        inflectional_forms = CSSSelector("p.inflectional-forms")(doc)[0]
        stem = CSSSelector("i")(inflectional_forms)[0].tail[1:-1]
        pos_s = CSSSelector("em")(inflectional_forms)
        form_s = CSSSelector("strong")(inflectional_forms)
        form_list = []
        for pos, form in zip(pos_s, form_s):
            form = form.text
            pos_list = []
            for part_of_speech in pos:
                full = part_of_speech.attrib.get('title')
                abbrev = part_of_speech.text
                pos_list.append(WordAttribute(full, abbrev))
            form_list.append(Form(form, pos_list))
        return InflectionalForms(form_list, stem)
    except: pass
class Form:
    def __init__(self, form, pos_list):
        self.form = form
        self.pos_list = pos_list
#verified
class InflectionalForms:
    def __init__(self, forms, stem):
        self.forms = forms
        self.stem = stem

#verified
def get_audio_for_basic_forms(doc):
    audio_forms = CSSSelector(("div#audioBasicForms"
                               " div.panel-body"
                               " table"
                               " tr"))(doc)
    return get_audio_forms(audio_forms)
#verified
def get_additional_audio(doc):
    audio_forms = CSSSelector("div#adtlAudio"
                             " div.panel-body"
                             " table"
                             " tr")(doc)
    return get_audio_forms(audio_forms)
#verified
def get_audio_forms(audio_forms):
    audio_form_list = []
    for audio_form in audio_forms:
        ojibwe = CSSSelector("td:first-child strong")(audio_form)[0].text
        parts_of_speech = CSSSelector("td:nth-child(2) em span")(audio_form)
        pos_list = []
        for part_of_speech in parts_of_speech:
            abbrev = part_of_speech.text
            full = part_of_speech.attrib.get('title')
            pos_list.append(WordAttribute(full, abbrev))
        speakers = CSSSelector("td.text-right a")(audio_form)
        audios = CSSSelector("td.text-right span div.audio-player")(audio_form)
        retaudiorec = []
        for speaker, audio in zip(speakers, audios):
            speakerhref = speaker.attrib.get('href')
            speakerinitials = speaker.text.strip()
            regular_audio = audio.attrib.get('data-file')
            mobile_audio = audio.attrib.get('data-mobile-file')
            retspeaker = Speaker(speakerhref, speakerinitials)
            retaudio = Audio(regular_audio, mobile_audio)
            retaudiorec.append(AudioRec(retspeaker, retaudio))
        audio_form_list.append(AudioForm(ojibwe, pos_list, retaudiorec))
    return audio_form_list
class WordAttribute:
    def __init__(self, full, abbrev):
        self.full = full
        self.abbrev = abbrev
class Speaker:
    def __init__(self, href, initials, name = None):
        self.href = href
        self.initials = initials
        self.name = name
class AudioForm:
    def __init__(self, ojibwe, pos_list, audios):
        self.ojibwe = ojibwe
        self.pos_list = pos_list
        self.audios = audios
class AudioRec:
    def __init__(self, speaker, audio):
        self.speaker = speaker
        self.audio = audio

#verified
def get_sentence_examples(doc):
    sentencerows = CSSSelector("div#sentenceExamples"
                               " div.panel-body"
                               " table"
                               " tr")(doc)
    sentences = []
    for sentencerow in sentencerows:
        try:
            ojibwe = CSSSelector("td:first-child strong div")(sentencerow)[0].text
        except IndexError: ojibwe=None
        try:
            english = CSSSelector("td:first-child small em div")(sentencerow)[0].text
        except IndexError: english = None
        try:
            speaker = CSSSelector("td.text-right a")(sentencerow)[0].attrib.get('href')
        except IndexError: speaker = None
        try:
            regular_audio = CSSSelector("td.text-right span div.audio-player")(sentencerow)[0].attrib.get('data-file')
            mobile_audio = CSSSelector("td.text-right span div.audio-player")(sentencerow)[0].attrib.get('data-mobile-file')
            audio = Audio(regular_audio, mobile_audio)
        except IndexError: audio = None
        sentences.append(SentenceExample(ojibwe, english, speaker, audio))
    return sentences

class Audio:
    def __init__(self, regular, mobile):
        self.regular = regular
        self.mobile = mobile

class SentenceExample:
    def __init__(self, ojibwe, english, speaker, audio):
        self.ojibwe = ojibwe
        self.english = english
        self.speaker = speaker
        self.audio = audio

def get_word_parts(doc):
    try: return etree.tounicode(CSSSelector("div#wordParts div.panel-body")(doc)[0], with_tail = False)
    except: pass


def get_reduplication(doc):
    try: return CSSSelector("div#reduplicatedForms div.panel-body strong")(doc)[0].text
    except IndexError: pass

#verified
def get_related_resources(doc):
    resources = CSSSelector("div#relatedResources"
                            " div.panel-body"
                            " ul.media-list.collection"
                            " li.media")(doc)
    
    if resources:
        retval = RelatedResources()
        for resource in resources:
            retval.add(resource)
        return retval
     
class RelatedResources:
    def __init__(self):
        self.imagelist = []
        self.videolist = []
        self.documentlist = []
    def add(self, resource):
        lefthref = CSSSelector("div.media-left a")(resource)[0].attrib.get('href')
        try:
            righta = CSSSelector("div.media-body h4.media-heading a")(resource)[0]
            righthref = righta.attrib.get('href')
            righttext = righta.text
        except IndexError:
            righta = None
            righthref = None
            righttext = None
        image_or_video_check_selector = CSSSelector(("div.media-left"
                                      " a img")) 
        if image_or_video_check_selector(resource):
            iv = image_or_video_check_selector(resource)[0]
            try:
                leftsrc = iv.attrib.get('src')
            except IndexError:
                leftsrc = None
            try:
                leftalt = iv.attrib.get('alt')
            except IndexError:
                leftalt = None
            retval = {'lefthref': lefthref, 'image': Image(leftsrc, leftalt), 'righthref': righthref, "righttext":righttext }
            if lefthref and lefthref[-6:] == "-video":
                self.videolist.append(retval)
            else:
                self.imagelist.append(retval)
            return 
        document_check_selector = CSSSelector(("div.media-left"
                                               " a"
                                               " span.glyphicon.glyphicon-duplicate.document-icon"))
        if document_check_selector(resource):
            retval = {'lefthref': lefthref,  'righthref': righthref, "righttext":righttext }
            self.documentlist.append(retval)

#verified
def get_regions(doc):
    regions = CSSSelector(" span.badge.badge-oj")(doc)
    retval = []
    for region in regions:
        abbrev = region.text
        full = region.attrib.get('title')
        retval.append(Region(abbrev, full))
    return retval

class Region:
    def __init__(self, abbrev, full):
        self.abbrev = abbrev
        self.full = full

def get_paired_with(doc):
    return doc.xpath('//span[preceding-sibling::em[1]/text()="Paired with:"]/span/a/@href')

def get_see_also(doc):
    return doc.xpath('//span[preceding-sibling::em[1]/text()="See also:"]/span/a/@href')

def get_redirect(doc):
    return doc.xpath('//span[preceding-sibling::text()="\n  ► "]/span/a/@href')
#verified
def get_word_part_title(doc):
    selector = CSSSelector((("div.container-fluid"
                             " div.row.content-container"
                             " div.col-md-9.col-sm-9.content"
                             " h1.page-title")))
    return selector(doc)[0].text.strip()

#verified
def get_word_part_type(doc):
    selector = CSSSelector((("div.container-fluid"
                             " div.row.content-container"
                             " div.col-md-9.col-sm-9.content"
                             " h1.page-title"
                             " span.badge.badge-oj")))
    return selector(doc)[0].text.strip()


def get_word_part_gloss(doc):
    selector = CSSSelector((("div.container-fluid"
                             " div.row.content-container"
                             " div.col-md-9.col-sm-9.content"
                             " dl dd:first-of-type")))
    dd = selector(doc)[0]
    return dd.text_content().strip()


#verified
def get_word_part_subtypes(doc):
    selector = CSSSelector((("div.container-fluid"
                             " div.row.content-container"
                             " div.col-md-9.col-sm-9.content"
                             " dl dt, dd")))
    dt_dd_s = selector(doc)
    for dt, dd in zip(dt_dd_s[:-1], dt_dd_s[1:]):
        if dt.tag == "dt" and dt.text == "Subtypes:":
            return dd.text_content().strip()
        

#verified       
def get_word_part_variants(doc):
    selector = CSSSelector((("div.container-fluid"
                             " div.row.content-container"
                             " div.col-md-9.col-sm-9.content"
                             " dl dt, dd")))
    dt_dd_s = selector(doc)
    for dt, dd in zip(dt_dd_s[:-1], dt_dd_s[1:]):
        if dt.tag == "dt" and dt.text == "Variants:":
            return dd.text_content().strip()

def get_word_part_words(doc):
    selector = CSSSelector(("div#mainEntries div.panel-body table tr td span.main-entry-title span.lemma a"))
    linklist = selector(doc)
    return [link.attrib.get('href') for link in linklist]

     
def scrape_entry(page):
    doc = CSSSelector("div.container-fluid"
                                       " div.row.content-container"
                                       " div.col-md-9.col-sm-9.content")(page)[0]
    sidebar = CSSSelector("div.container-fluid"
                                 " div.row.content-container"
                                 " div.col-md-3.col-sm-3.sidebar")(page)[0]
    retdict = {}
    for funcname in ("head_lemma", "part_of_speech", "notes", "species",
                     "head_speaker", "head_audio", "head_image",
                     "gloss",
                     "inflectional_forms", "audio_for_basic_forms", "additional_audio",
                     "sentence_examples", "word_parts",
                     "reduplication", "related_resources", "regions", "paired_with", "see_also", "redirect"):
        retdict[funcname] = eval("get_" + funcname)(doc)
    for funcname in ("word_family", "related_words"):
        retdict[funcname] = eval("get_" + funcname)(sidebar)
    return retdict

def scrape_word_part_entry(doc):
    retdict = {}
    for funcname in ("title", "type", "gloss", "subtypes", "variants", "words"):
        try:
            retdict[funcname] = eval("get_word_part_" + funcname)(doc)
        except:
            retdict[funcname] = None
    return retdict

def scrape_word_part_entries(urlsourcepath):
    with open(urlsourcepath, "r") as f:
        urls = json.load(f)
    with open("all_word_part_entries.json", "w+") as f:
        for url in urls:
            print(url)
            doc = html.fromstring(requests.get("https://ojibwe.lib.umn.edu" + url).text)
            parse = scrape_word_part_entry(doc)
            def make_jsonable(x):
                if type(x) == bytes:
                    return x.decode('utf8')
                else:
                    return x.__dict__
            json.dump(parse, f, default = make_jsonable)
            f.write(",")
            
def scrape_entries(urlsourcepath):
    with open(urlsourcepath, "r") as f:
        urls = json.load(f)
    with open("all_entries3.json", "w+") as f:
        for url in urls:
            print(url)
            doc = html.fromstring(requests.get("https://ojibwe.lib.umn.edu" + url).text)
            parse = scrape_entry(doc)
            def make_jsonable(x):
                if type(x) == bytes:
                    return x.decode('utf8')
                else:
                    return x.__dict__
            json.dump(parse, f, default = make_jsonable)
            f.write(",")
def make_jsonable(x):
                if type(x) == bytes:
                    return x.decode('utf8')
                else:
                    return x.__dict__    
def scrape_images(iset):
    for url in iset:
        print(url)
        img = requests.get('https://ojibwe.lib.umn.edu' + url).text
        path = "/Users/jacobsolinsky/programming/opd/opd/static" + os.path.dirname(url)
        if not os.path.exists(path):
            os.makedirs(path)
        impath = "/Users/jacobsolinsky/programming/opd/opd/static" + url
        with open(impath, "w+") as f:
            f.write(img)
def scrape_gallery(doc):
    doc2 = doc
    doc = CSSSelector("div.container-fluid div.row.content-container div.col-md-9.col-sm-9.content")(doc)[0]
    title = CSSSelector("h1.page-title")(doc)[0].text
    try:
        copyright = CSSSelector("div.container-fluid div.row.content-container div.col-md-9.col-sm-9.content>div.stylized-text")(doc2)[0].text
    except:
        copyright = None
    if CSSSelector("dl dd div")(doc):
        description = CSSSelector("dl dd div")(doc)[0].text
        if CSSSelector("div.video-player img")(doc):
            image = Image(CSSSelector("div.video-player img")(doc)[0].attrib.get('src'), CSSSelector("div.video-player img")(doc)[0].attrib.get('alt'))
            videosrc = CSSSelector("div.video-player")(doc)[0].attrib.get('data-file')
            video = Video(videosrc, image)
            return VideoGallery( title, copyright, description, video)
        elif CSSSelector("img")(doc):
            src = CSSSelector("img")(doc)[0].attrib.get('src')
            alt = CSSSelector("img")(doc)[0].attrib.get('alt')
            image = Image(src, alt)
            return ImageGallery( title, copyright, description, image)
        else:
            return EmptyGallery( title, copyright, description)
    if CSSSelector("blockquote")(doc):
        description = copyright
        documentbody = CSSSelector("blockquote div.stylized-text")(doc)[0].text
        try:
            bibliography = CSSSelector("blockquote div.bibliography div")(doc)[0].text
        except IndexError:
            bibliography = None
        return DocumentGallery( title, description, documentbody, bibliography)
    elif CSSSelector("img")(doc):
        description = None
        src = CSSSelector("img")(doc)[0].attrib.get('src')
        alt = CSSSelector("img")(doc)[0].attrib.get('alt')
        image = Image(src, alt)
        return ImageGallery( title, copyright, description, image)
class Video:
    def __init__(self, src, image):
        self.src = src
        self.image = image
        
class ImageGallery:
    def __init__(self, title, copyright, description, image):
        self.type = 'image'
        self.title = title
        self.copyright = copyright
        self.description = description
        self.image = image
class VideoGallery:
    def __init__(self, title, copyright, description, video):
        self.type = 'video'
        self.title = title
        self.copyright = copyright
        self.description = description
        self.video = video
class DocumentGallery:
    def __init__(self, title, description, documentbody, bibliography):
        self.type = 'document'
        self.title = title
        self.description = description
        self.documentbody = documentbody
        self.bibliography = bibliography
        
class EmptyGallery:
    def __init__(self, title, copyright, description):
        self.type = 'video'
        self.title = title
        self.copyright = copyright
        self.description = description
        self.video = None
        
def scrape_galleries(urls):
    with open("/Users/jacobsolinsky/programming/opd/opd/data/galleries.json", "w+") as f:
        f.write('[')
        for url in urls:
            print(url)
            doc = html.fromstring(requests.get("https://ojibwe.lib.umn.edu" + url).text)
            gallery = scrape_gallery(doc)
            gallery.url = url
            json.dump(gallery, f, default = make_jsonable)
            f.write(',')
    with open("/Users/jacobsolinsky/programming/opd/opd/data/galleries.json", "r") as f:     
        filestr = f.read()
        filestr = filestr[:-1]
        filestr = filestr + ']'
    with open("/Users/jacobsolinsky/programming/opd/opd/data/galleries.json", "w") as f:
        f.write(filestr)
def scrape_news(doc):
    doc = CSSSelector("div.container-fluid div.row.content-container div.col-md-9.col-sm-9.content")(doc)[0]
    retval = []
    for entry in CSSSelector("h3")(doc):
        title = CSSSelector("strong")(entry)[0].text
        date = entry.xpath('text()')
        paragraphs = ''.join([etree.tounicode(p).decode('utf-8') for p in entry.xpath(f'//p[preceding-sibling::h3[1]/strong[text()="{title}"]]')])
        retval.append({"title":title, "date":date, "html":paragraphs})
    with open("/Users/jacobsolinsky/programming/opd/opd/data/news.json", "w+") as f:
        json.dump(retval, f)

def parse_multi_json(filestring):
    level = 0
    init = 0
    retval = []
    for i, c in enumerate(filestring):
        if c == "{":
            level += 1
        if c == "}":
            level -= 1
            if level == 0:
                if len(retval) == 18965:
                    level += 1
                    continue
                retval.append(json.loads(filestring[init:i +1]))
                init = i + 1
    return retval

static_urls = ["https://ojibwe.lib.umn.edu/about-ojibwe-language",
               "https://ojibwe.lib.umn.edu/understanding-word-stems-word-parts-and-word-families",
               "https://ojibwe.lib.umn.edu/understanding-audio-and-example-sentences",
               "https://ojibwe.lib.umn.edu/news/dictionary",
               "https://ojibwe.lib.umn.edu/news/ojibwe-language"]
index_urls = [ "https://ojibwe.lib.umn.edu/help/ojibwe-parts-of-speech",
               "https://ojibwe.lib.umn.edu/help/regions",
               "https://ojibwe.lib.umn.edu/help/paradigm-classes"]

#gurl = set()
#doc = geth('https://ojibwe.lib.umn.edu/category/galleries/wintertravel')
#docurl = CSSSelector("dd a")(doc)
#for docur in docurl:
#    gurl.add(docur.attrib.get(.get(['href'])
#for m in me:
 #   if m['related_resources'] is not None:
  #      r = m['related_resources']
   #     il =r['imagelist']
    #    vl = r['videolist']
     #   dl = r['documentlist']
     #   for ill in il:
      #      gurl.append(ill['righthref'])
       # for vll in vl:
        #    gurl.append(vll['righthref'])
        #for dll in dl:
         #   gurl.append(dll['righthref'])
#word_attrib.get(.get(ute_list = []
#word_attrib.get(.get(ute_link_list = []
#inflectional_forms_list = []
#forms_list = []

#ifi = 1
#fi = 1
#for t in thing:
#    if t['inflectional_forms'] is not None:
#        tif = t['inflectional_forms']
#
#        ifd = {"index":ifi}
#        if tif['forms'] is not None:
#            for form in tif['forms']:
#                forms_list.append({"index": fi, "inflectional_forms": ifi, "form": form["form"]})
#                for pos in form['pos_list']:
#                    word_attrib.get(.get(ute_link_list.append({"form_index": fi, "word_attrib.get(ute":pos['abbrev']})
#                    if {"full": pos['full'], "abbrev": pos['abbrev']} not in word_attrib.get(ute_list:
#                        word_attrib.get(ute_list.append({"full": pos['full'], "abbrev": pos['abbrev']})
#                fi += 1
#        tif = {"index": ifi, "stem": tif['stem']}
#        inflectional_forms_list.append(tif)
#        t['inflectional_forms'] = tif
#        ifi += 1
#bai = 1
#aai = 1
#esi = 1
#aui = 1
#basic_audio_list = []
#additional_audio_list = []
#sentence_example_list = []
#audio_list = []
#audio_rec_list = []
#word_attrib.get(ute_basic_link_list = []
#word_attrib.get(ute_additional_link_list = []
#for t in thing:
    #if t['audio_for_basic_forms'] is not None:
        #tiff = t['audio_for_basic_forms']
        #for tif in tiff:
            #basic_audio_list.append({"entry": t['url'], "index": bai, "ojibwe": tif['ojibwe']})
            #for pos in tif['pos_list']:
                #word_attrib.get(ute_basic_link_list.append({"baindex": bai,'pos':pos['abbrev']})
            #tifaus = tif["audios"]
            #for audio in tifaus:
                #audio_rec_list.append({"audio_index": bai, "speaker": audio['speaker']['href'],
#                        "audio": aui})
                #aridu = audio['audio']
                #audio_list.append({'index': aui, 'regular':aridu['regular'], 'mobile':aridu['mobile']})
                #aui +=1
            #bai += 1
    #t['audio_for_basic_forms'] = None
    #if t['additional_audio'] is not None:
        #tiff = t['additional_audio']
        #for tif in tiff:
            #additional_audio_list.append({"entry": t['url'], "index": aai, "ojibwe": tif['ojibwe']})
            #for pos in tif['pos_list']:
                #word_attrib.get(ute_additional_link_list.append({"aaindex": aai,'pos':pos['abbrev']})
            #tifaus = tif["audios"]
            #for audio in tifaus:
                #audio_rec_list.append({ "audio_form_index": aai, "speaker": audio['speaker']['href'],
#                        "audio_index": aui})
                #aridu = audio['audio']
                #audio_list.append({'index': aui, 'regular':aridu['regular'], 'mobile':aridu['mobile']})
                #aui +=1
            #aai += 1
    #t['additional_audio'] = None
    #if t['sentence_examples'] is not None:
        #tiff = t['sentence_examples']
        #for tif in tiff:
            #sentence_example_list.append({"entry": t['url'], "index": esi, "ojibwe": tif['ojibwe'], 'english':tif['english']})
            #tifregular = tif['audio']["regular"]
            #tifmobile = tif['audio']['mobile']
            #tifspeaker = tif['speaker']
            #audio_list.append({"index": aui, "regular": tifregular, "mobile":tifmobile})
            #audio_rec_list.append({"audio_form_index":esi, "audio_index": aui, "speaker": tifspeaker})
            #aui +=1
            #esi +=1
    #t['sentence_examples'] = None
    #if t['head_audio'] is not None:
        #audio_rec_list.append({"audio_form_index":t['url'], "audio_index": aui, "speaker": t['head_speaker']})
        #audio_list.append({"index": aui, "regular": t['head_audio']['regular'], "mobile":t['head_audio']['mobile']})
    #t['head_audio'] = None
        

#word_part_link_list = []
#for wpt in wpthing:
#    print(wpt['url'])
#    for word in wpt['words']:
#        word_part_link_list.append({'word': word, 'word_part':wpt['url']})
#for t in thing:
#    print(t['url'])
#    for word_part in t['word_parts']:
#        if {'word': t['url'], 'word_part':word_part} not in word_part_link_list:
#            word_part_link_list.append({'word': t['url'], 'word_part':word_part})
#resources_link_list = []
#for t in thing:
#    if t['related_resources'] is not None:
#        tif = t['related_resources']
#        for i in tif['imagelist']:
#            resources_link_list.append({'entry': t['url'], 'resource': i['righthref']})
#        for i in tif['documentlist']:
#            resources_link_list.append({'entry': t['url'], 'resource': i['righthref']})
#        for i in tif['videolist']:
#            resources_link_list.append({'entry': t['url'], 'resource': i['righthref']})

            


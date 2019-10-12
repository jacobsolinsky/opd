from django.contrib import admin
from .models import MainEntry, PartOfSpeech, Audio, Image, WordFamily, RelatedWord,\
InflectionalForm, Poss, AudioForBasicForm, AdditionalAudio, SentenceExample, AudioForBasicFormAudioRec,\
AdditionalAudioAudioRec, SentenceExampleAudioRec, Region, ImageResource, VideoResource,\
DocumentResource, Speaker, VideoCollection, ImageCollection, DocumentCollection, Video

for modell in (MainEntry, PartOfSpeech, Audio, Image, WordFamily, RelatedWord,
InflectionalForm, Poss, AudioForBasicForm, AdditionalAudio, SentenceExample, AudioForBasicFormAudioRec,
AdditionalAudioAudioRec, SentenceExampleAudioRec, Region, ImageResource, VideoResource,
DocumentResource, Speaker, VideoCollection, ImageCollection, DocumentCollection, Video) :
    admin.site.register(modell)

# Register your models here.

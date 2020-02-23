from rest_framework import serializers
from .models import *
import re
from django.http import HttpResponse
import time
import datetime


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ("historic_entry", "creation_datetime")


class HistorySetSerializer(serializers.ModelSerializer):
    history_set = HistorySerializer(many=True, read_only=True)
    class Meta:
        model = HistorySet
        fields = ("history_set", "id")


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ("src", "alt")


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ("src", "thumb")


class PartOfSpeechSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartOfSpeech
        fields = ("abbrev", "full", "description", "section_url")


class LittlePartOfSpeechSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartOfSpeech
        fields = ("abbrev", "full")


class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaker
        fields = ("image", "href", "initials", "primary_name",
                  "ojibwe_name", "english_name", "community", "region",
                  "description")
        depth = 1


class LittleSpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaker
        fields = ("href", "initials", "primary_name",
                  "ojibwe_name", "english_name")


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ("title", "date", "html")


class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = ("regular", "mobile")


class PossSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poss
        fields = ("abbrev", "full")


class SentenceExampleAudioRecSerializer(serializers.ModelSerializer):
    speaker = LittleSpeakerSerializer(required=False)

    class Meta:
        model = SentenceExampleAudioRec
        fields = ("speaker", "audio")
        depth = 1


class AudioForBasicFormAudioRecSerializer(serializers.ModelSerializer):
    speaker = LittleSpeakerSerializer(required=False)

    class Meta:
        model = AudioForBasicFormAudioRec
        fields = ("speaker", "audio")
        depth = 1


class AdditionalAudioAudioRecSerializer(serializers.ModelSerializer):
    speaker = LittleSpeakerSerializer(required=False)

    class Meta:
        model = AdditionalAudioAudioRec
        fields = ("speaker", "audio")
        depth = 1


class AudioForBasicFormSerializer(serializers.ModelSerializer):
    audio_rec = AudioForBasicFormAudioRecSerializer(many=True)

    class Meta:
        model = AudioForBasicForm
        fields = ("ojibwe", "poss", "audio_rec")
        depth = 1


class AdditionalAudioSerializer(serializers.ModelSerializer):
    audio_rec = AdditionalAudioAudioRecSerializer(many=True)

    class Meta:
        model = AdditionalAudio
        fields = ("ojibwe", "poss", "audio_rec")
        depth = 1


class SentenceExampleSerializer(serializers.ModelSerializer):
    audio_rec = SentenceExampleAudioRecSerializer(many=True)

    class Meta:
        model = SentenceExample
        fields = ("ojibwe", "english", "audio_rec")


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ("abbrev", "full", "description")


class InflectionalFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = InflectionalForm
        fields = ("form", "poss")
        depth = 1


class ImageCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageCollection
        fields = ("url", "copyright", "title", "description", "image")
        depth = 1


class DocumentCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentCollection
        fields = ("url", "copyright", "title", "description", "body",
                  "bibliography")


class VideoCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoCollection
        fields = ("url", "copyright", "title", "description", "video")
        depth = 1


class GenericCollectionLinkSerializer(serializers.Serializer):
    thumb_image = ImageSerializer(required=False)
    url = serializers.CharField(max_length=200)
    title = serializers.CharField(max_length=200)
    type = serializers.CharField(max_length=20)


class ImageResourceSerializer(serializers.ModelSerializer):
    righthref = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = ImageResource
        fields = ("image", "righthref", "righttext")
        depth = 1


class DocumentResourceSerializer(serializers.ModelSerializer):
    righthref = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = DocumentResource
        fields = ("righthref", "righttext")


class VideoResourceSerializer(serializers.ModelSerializer):
    righthref = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = VideoResource
        fields = ("image", "righthref", "righttext")
        depth = 1


class TinyLinkSerializer(serializers.ModelSerializer):
    part_of_speech = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = MainEntry
        fields = ('url', 'head_lemma', 'part_of_speech')


class SmallLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainEntry
        fields = ('url', 'head_lemma', 'part_of_speech', 'region')
        depth = 1


class MediumLinkSerializer(serializers.ModelSerializer):
    imageresource_set = serializers.PrimaryKeyRelatedField(many=True,
                                                           read_only=True)
    documentresource_set = serializers.PrimaryKeyRelatedField(many=True,
                                                              read_only=True)
    videoresource_set = serializers.PrimaryKeyRelatedField(many=True,
                                                           read_only=True)

    class Meta:
        model = MainEntry
        fields = ('url', 'head_lemma', 'part_of_speech', 'gloss',
                  'head_audio', 'head_image',
                  'region', 'imageresource_set', 'videoresource_set',
                  'documentresource_set')
        depth = 1


class WordFamilyPairSerializer(serializers.ModelSerializer):
    member = MediumLinkSerializer()

    class Meta:
        model = WordFamilyPair
        fields = ("kind", "member")
        depth = 1


class WordFamilySerializer(serializers.ModelSerializer):
    head = MediumLinkSerializer()
    members = WordFamilyPairSerializer(many=True)

    class Meta:
        model = WordFamily
        fields = ("head", "members")
        depth = 1


class RelatedWordSerializer(serializers.ModelSerializer):
    mainentry_set = MediumLinkSerializer(many=True)

    class Meta:
        model = RelatedWord
        fields = ("title", "mainentry_set")


class SearchLinkSerializer(serializers.ModelSerializer):
    paired_with_inv = SmallLinkSerializer(many=True)
    see_also_inv = SmallLinkSerializer(many=True)
    redirect_inv = SmallLinkSerializer(many=True)
    imageresource_set = serializers.PrimaryKeyRelatedField(many=True,
                                                           read_only=True)
    documentresource_set = serializers.PrimaryKeyRelatedField(many=True,
                                                              read_only=True)
    videoresource_set = serializers.PrimaryKeyRelatedField(many=True,
                                                           read_only=True)

    class Meta:
        model = MainEntry
        fields = ('url', 'head_lemma', 'part_of_speech', 'gloss',
                  'head_audio', 'head_image', 'word_family',
                  'paired_with_inv', 'see_also_inv', 'redirect_inv',
                  'region', 'imageresource_set', 'videoresource_set',
                  'documentresource_set')
        depth = 1


MainEntryNestedModels = (
    AudioForBasicForm, AdditionalAudio, SentenceExample, InflectionalForm,
    ImageResource, VideoResource, DocumentResource
)
class MainEntrySerializer(serializers.ModelSerializer):
    head_speaker = LittleSpeakerSerializer(required=False)
    history_set = HistorySetSerializer(required=False)
    part_of_speech = LittlePartOfSpeechSerializer(required=False)
    paired_with_inv = SmallLinkSerializer(many=True)
    redirect_inv = SmallLinkSerializer(many=True)
    word_family = WordFamilySerializer(required=False)
    related_words = RelatedWordSerializer(required=False)
    region = RegionSerializer(many=True)
    basic_audio = AudioForBasicFormSerializer(many=True)
    additional_audio = AdditionalAudioSerializer(many=True)
    sentence_examples = SentenceExampleSerializer(many=True)
    inflectionalform_set = InflectionalFormSerializer(many=True)
    imageresource_set = ImageResourceSerializer(many=True)
    videoresource_set = VideoResourceSerializer(many=True)
    documentresource_set = DocumentResourceSerializer(many=True)

    class Meta:
        model = MainEntry
        fields = ('url', 'old_url', 'head_lemma', 'part_of_speech', 'history_set',
                  'notes', 'gloss',
                  'head_speaker', 'head_audio', 'head_image',
                  'paired_with_inv', 'redirect_inv',
                  'word_family', 'related_words', 'word_parts',
                  'reduplication', 'region', 'stem', 'basic_audio',
                  'additional_audio', 'sentence_examples',
                  'inflectionalform_set', 'imageresource_set',
                  'videoresource_set', 'documentresource_set')
        depth = 1

    def validate(self, data): return data

    @staticmethod
    def main_entry_url_synthesize(dict_):
        head_lemma = dict_['head_lemma']
        part_of_speech = dict_['part_of_speech']['abbrev']

        retval = head_lemma + "-" + part_of_speech
        retval = re.sub(r"[ +']", "-", retval)
        retval = re.sub(r"[-]{2,}", "-", retval)
        return retval

    def create(self, validated_data):
        replace_url = validated_data.pop('url')
        old = MainEntry.objets.get(pk=replace_url)
        old.url = old.old_url
        old.save()
        new_url = main_entry_url_synthesize(validated_data)
        new_old_url = new_url + str(int(time.time()))
        new = MainEntry(url=new_url, old_url=new_old_url, history_set=old.history_set)
        new.save()
        h = History(new.history_set, new.old_url, datetime.now())
        h.save()
        if new_url != old.url:
            wf = old.members().all()
            for w in old.members().all():
                w.member_id = new_url
                w.save()
            r = old.related_words
            if r:
                r.mainentry_set.remove(old)
                r.mainentry_set.add(new)
                r.save()
            #finally
            old.url = old.old_url
            old.save()



class WordPartSerializer(serializers.ModelSerializer):
    words_that_use_this_part = MediumLinkSerializer(many=True)
    history_set = HistorySetSerializer(required=False)

    class Meta:
        model = WordPart
        fields = ('url', 'old_url', 'history_set' 'title', 'type', 'gloss', 'subtypes',
                  'words_that_use_this_part')


class KeywordGroupSerializer(serializers.ModelSerializer):
    mainentry_set = MediumLinkSerializer(many=True)
    keyword = None

    class Meta:
        model = KeywordGroup
        fields = ("name", "mainentry_set")


class KeywordSerializer(serializers.ModelSerializer):
    keywordgroup_set = KeywordGroupSerializer(many=True)

    class Meta:
        model = Keyword
        fields = ("name", "description", "distinguisher", "pos",
                  "keywordgroup_set")
        depth = 1


class Utilities:
    @staticmethod
    def new_audio_for_basic_forms_index(count):
        retval = AudioForBasicForm.objects.all().aggregate(Max('audio_for_basic_forms_index'))['audio_for_basic_forms_index__max']+1
        return list(range(retval, retval+count))

    @staticmethod
    def new_additional_audio_index(count):
        new_additional_audio_id = AdditionalAudio.objects.all().aggregate(Max('additional_audio_index'))['additional_audio_index__max']+1
        return list(range(retval, retval+count))

    @staticmethod
    def new_sentence_examples_index(count):
        new_sentence_example_id = SentenceExample.objects.all().aggregate(Max('sentence_examples_index'))['sentence_examples_index__max']+1
        return list(range(retval, retval+count))

    @staticmethod
    def new_inflectional_forms_index(count):
        retval = InflectionalForm.objects.all().aggregate(Max('inflectional_forms_index'))['inflectional_forms_index__max']+1
        return list(range(retval, retval+count))

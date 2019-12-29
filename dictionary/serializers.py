from rest_framework import serializers
from . import models


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Image
        fields = ("src", "alt")


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Video
        fields = ("src", "thumb")


class PartOfSpeechSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PartOfSpeech
        fields = ("abbrev", "full", "description", "section_url")


class LittlePartOfSpeechSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PartOfSpeech
        fields = ("abbrev", "full")


class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Speaker
        fields = ("image", "href", "initials", "primary_name",
                  "ojibwe_name", "english_name", "community", "region",
                  "description")
        depth = 1


class LittleSpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Speaker
        fields = ("href", "initials", "primary_name",
                  "ojibwe_name", "english_name")


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.News
        fields = ("title", "date", "html")


class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Audio
        fields = ("regular", "mobile")


class PossSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Poss
        fields = ("abbrev", "full")


class SentenceExampleAudioRecSerializer(serializers.ModelSerializer):
    speaker = LittleSpeakerSerializer(required=False)

    class Meta:
        model = models.SentenceExampleAudioRec
        fields = ("speaker", "audio")
        depth = 1


class AudioForBasicFormAudioRecSerializer(serializers.ModelSerializer):
    speaker = LittleSpeakerSerializer(required=False)

    class Meta:
        model = models.AudioForBasicFormAudioRec
        fields = ("speaker", "audio")
        depth = 1


class AdditionalAudioAudioRecSerializer(serializers.ModelSerializer):
    speaker = LittleSpeakerSerializer(required=False)

    class Meta:
        model = models.AdditionalAudioAudioRec
        fields = ("speaker", "audio")
        depth = 1


class AudioForBasicFormSerializer(serializers.ModelSerializer):
    audio_rec = AudioForBasicFormAudioRecSerializer(many=True)

    class Meta:
        model = models.AudioForBasicForm
        fields = ("ojibwe", "poss", "audio_rec")
        depth = 1


class AdditionalAudioSerializer(serializers.ModelSerializer):
    audio_rec = AdditionalAudioAudioRecSerializer(many=True)

    class Meta:
        model = models.AdditionalAudio
        fields = ("ojibwe", "poss", "audio_rec")
        depth = 1


class SentenceExampleSerializer(serializers.ModelSerializer):
    audio_rec = SentenceExampleAudioRecSerializer(many=True)

    class Meta:
        model = models.SentenceExample
        fields = ("ojibwe", "english", "audio_rec")


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Region
        fields = ("abbrev", "full", "description")


class InflectionalFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InflectionalForm
        fields = ("form", "poss")
        depth = 1


class ImageCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ImageCollection
        fields = ("url", "copyright", "title", "description", "image")
        depth = 1


class DocumentCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DocumentCollection
        fields = ("url", "copyright", "title", "description", "body",
                  "bibliography")


class VideoCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VideoCollection
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
        model = models.ImageResource
        fields = ("image", "righthref", "righttext")
        depth = 1


class DocumentResourceSerializer(serializers.ModelSerializer):
    righthref = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = models.DocumentResource
        fields = ("righthref", "righttext")


class VideoResourceSerializer(serializers.ModelSerializer):
    righthref = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = models.VideoResource
        fields = ("image", "righthref", "righttext")
        depth = 1


class TinyLinkSerializer(serializers.ModelSerializer):
    part_of_speech = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = models.MainEntry
        fields = ('url', 'head_lemma', 'part_of_speech')


class SmallLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MainEntry
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
        model = models.MainEntry
        fields = ('url', 'head_lemma', 'part_of_speech', 'gloss',
                  'head_audio', 'head_image',
                  'region', 'imageresource_set', 'videoresource_set',
                  'documentresource_set')
        depth = 1


class WordFamilyPairSerializer(serializers.ModelSerializer):
    member = MediumLinkSerializer()

    class Meta:
        model = models.WordFamilyPair
        fields = ("kind", "member")
        depth = 1


class WordFamilySerializer(serializers.ModelSerializer):
    head = MediumLinkSerializer()
    members = WordFamilyPairSerializer(many=True)

    class Meta:
        model = models.WordFamily
        fields = ("head", "members")
        depth = 1


class RelatedWordSerializer(serializers.ModelSerializer):
    mainentry_set = MediumLinkSerializer(many=True)

    class Meta:
        model = models.RelatedWord
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
        model = models.MainEntry
        fields = ('url', 'head_lemma', 'part_of_speech', 'gloss',
                  'head_audio', 'head_image', 'word_family',
                  'paired_with_inv', 'see_also_inv', 'redirect_inv',
                  'region', 'imageresource_set', 'videoresource_set',
                  'documentresource_set')
        depth = 1


class MainEntrySerializer(serializers.ModelSerializer):
    head_speaker = LittleSpeakerSerializer(required=False)
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
        model = models.MainEntry
        fields = ('url', 'head_lemma', 'part_of_speech', 'notes', 'gloss',
                  'head_speaker', 'head_audio', 'head_image',
                  'paired_with_inv', 'redirect_inv',
                  'word_family', 'related_words', 'word_parts',
                  'reduplication', 'region', 'stem', 'basic_audio',
                  'additional_audio', 'sentence_examples',
                  'inflectionalform_set', 'imageresource_set',
                  'videoresource_set', 'documentresource_set')
        depth = 1


class WordPartSerializer(serializers.ModelSerializer):
    words_that_use_this_part = MediumLinkSerializer(many=True)

    class Meta:
        model = models.WordPart
        fields = ('url', 'title', 'type', 'gloss', 'subtypes',
                  'words_that_use_this_part')


class KeywordGroupSerializer(serializers.ModelSerializer):
    mainentry_set = MediumLinkSerializer(many=True)
    keyword = None

    class Meta:
        model = models.KeywordGroup
        fields = ("name", "mainentry_set")


class KeywordSerializer(serializers.ModelSerializer):
    keywordgroup_set = KeywordGroupSerializer(many=True)

    class Meta:
        model = models.Keyword
        fields = ("name", "description", "distinguisher", "pos",
                  "keywordgroup_set")
        depth = 1

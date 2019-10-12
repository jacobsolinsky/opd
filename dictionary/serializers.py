from rest_framework import serializers



class ImageSerializer(serializers.Serializer):
    src = serializers.CharField(max_length=200)
    alt = serializers.CharField(max_length=200,  required = False)


class VideoSerializer(serializers.Serializer):
    src = serializers.CharField( max_length=200)
    thumb = ImageSerializer( required = False)


class PartOfSpeechSerializer(serializers.Serializer):
    abbrev = serializers.CharField(max_length = 30)
    full = serializers.CharField(max_length=200)
    description = serializers.CharField()
    section_url = serializers.CharField(max_length=200)


class SpeakerSerializer(serializers.Serializer):
    image = ImageSerializer()
    href = serializers.CharField(max_length=200)
    initials = serializers.CharField(max_length = 30)
    primary_name = serializers.CharField(max_length=200)
    ojibwe_name = serializers.CharField(max_length=200)
    english_name = serializers.CharField(max_length=200)
    community = serializers.CharField(max_length=200)
    region = serializers.CharField(max_length=200)
    description = serializers.CharField()


class NewsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    date = serializers.CharField(max_length=200)
    html = serializers.CharField()


class AudioSerializer(serializers.Serializer):
    regular = serializers.CharField(max_length=200)
    mobile = serializers.CharField(max_length=200)


class PossSerializer(serializers.Serializer):
    abbrev = serializers.CharField(max_length = 30)
    full = serializers.CharField(max_length=200, default = "")


class SentenceExampleAudioRecSerializer(serializers.Serializer):
    speaker = SpeakerSerializer(required = False)
    audio = AudioSerializer(required = False)


class AudioForBasicFormAudioRecSerializer(serializers.Serializer):
    speaker = SpeakerSerializer(required = False)
    audio = AudioSerializer(required = False)


class AdditionalAudioAudioRecSerializer(serializers.Serializer):
    speaker = SpeakerSerializer(required = False)
    audio = AudioSerializer(required = False)


class AudioForBasicFormSerializer(serializers.Serializer):
    ojibwe = serializers.CharField(max_length=200)
    poss = PossSerializer(many=True)
    audio_rec = AudioForBasicFormAudioRecSerializer(required=False)


class AdditionalAudioSerializer(serializers.Serializer):
    ojibwe = serializers.CharField(max_length=200)
    poss = PossSerializer(many=True)
    audio_rec = AdditionalAudioAudioRecSerializer(required=False)


class SentenceExampleSerializer(serializers.Serializer):
    ojibwe = serializers.CharField()
    english = serializers.CharField()
    audio_rec = SentenceExampleAudioRecSerializer(required=False)


class RegionSerializer(serializers.Serializer):
    abbrev = serializers.CharField(max_length = 30)
    full = serializers.CharField(max_length=200, default = "")
    description = serializers.CharField(default = "")


class InflectionalFormSerializer(serializers.Serializer):
    form = serializers.CharField(max_length=200)
    poss = PossSerializer(many = True)



class ImageCollectionSerializer(serializers.Serializer):
    url = serializers.CharField(max_length=200)
    copyright = serializers.CharField(max_length=200)
    title = serializers.CharField(max_length=200)
    description = serializers.CharField()
    image = ImageSerializer(required = False)


class DocumentCollectionSerializer(serializers.Serializer):
    url = serializers.CharField(max_length=200)
    copyright = serializers.CharField(max_length=200)
    title = serializers.CharField(max_length=200)
    description = serializers.CharField()
    body = serializers.CharField()
    bibliography = serializers.CharField()



class VideoCollectionSerializer(serializers.Serializer):
    url = serializers.CharField(max_length=200)
    copyright = serializers.CharField(max_length=200)
    title = serializers.CharField(max_length=200)
    description = serializers.CharField()
    video = VideoSerializer()


class ImageResourceSerializer(serializers.Serializer):
    image = ImageSerializer()
    righthref = serializers.PrimaryKeyRelatedField(read_only=True)
    righttext = serializers.CharField(max_length = 200)


class DocumentResourceSerializer(serializers.Serializer):
    righthref = serializers.PrimaryKeyRelatedField(read_only=True)
    righttext = serializers.CharField(max_length = 200)


class VideoResourceSerializer(serializers.Serializer):
    image = ImageSerializer()
    righthref = serializers.PrimaryKeyRelatedField(read_only=True)
    righttext = serializers.CharField(max_length = 200)


class SmallLinkSerializer(serializers.Serializer):
    url = serializers.CharField(max_length=200)
    head_lemma = serializers.CharField(max_length=200)
    part_of_speech = PartOfSpeechSerializer(required = False)
    region = RegionSerializer(many = True)


class MediumLinkSerializer(serializers.Serializer):
    url = serializers.CharField(max_length=200)
    head_lemma = serializers.CharField(max_length=200)
    part_of_speech = PartOfSpeechSerializer(required = False)
    species = serializers.CharField()
    gloss = serializers.CharField()
    head_audio = serializers.PrimaryKeyRelatedField(read_only=True)
    head_image = serializers.PrimaryKeyRelatedField(read_only=True)
    region = RegionSerializer(many = True)
    imageresource_set = serializers.PrimaryKeyRelatedField(read_only=True, many = True)
    videoresource_set = serializers.PrimaryKeyRelatedField(read_only=True, many = True)
    documentresource_set = serializers.PrimaryKeyRelatedField(read_only=True, many = True)


class MemberSerializer(serializers.Serializer):
    kind = serializers.CharField(max_length = 200)
    member = MediumLinkSerializer()


class WordFamilySerializer(serializers.Serializer):
    members = MemberSerializer(many=True)


class WordFamilyPairSerializer(serializers.Serializer):
    word_family = WordFamilySerializer()


class RelatedWordSerializer(serializers.Serializer):
    title = serializers.CharField(max_length = 200)
    word = MediumLinkSerializer()

class SearchLinkSerializer(serializers.Serializer):
    url = serializers.CharField(max_length=200)
    head_lemma = serializers.CharField(max_length=200)
    part_of_speech = PartOfSpeechSerializer(required = False)
    species = serializers.CharField()
    gloss = serializers.CharField()
    head_audio = serializers.PrimaryKeyRelatedField(read_only=True)
    head_image = serializers.PrimaryKeyRelatedField(read_only=True)
    paired_with_inv = SmallLinkSerializer(many = True)
    see_also_inv = SmallLinkSerializer(many = True)
    redirect_inv = SmallLinkSerializer(many = True)
    region = RegionSerializer(many = True)
    imageresource_set = serializers.PrimaryKeyRelatedField(read_only=True, many = True)
    videoresource_set = serializers.PrimaryKeyRelatedField(read_only=True, many = True)
    documentresource_set = serializers.PrimaryKeyRelatedField(read_only=True, many = True)


class MainEntrySerializer(serializers.Serializer):
    url = serializers.CharField(max_length=200)
    head_lemma = serializers.CharField(max_length=200)
    part_of_speech = PartOfSpeechSerializer(required = False)
    notes = serializers.CharField()
    species = serializers.CharField()
    gloss = serializers.CharField()
    head_speaker = SpeakerSerializer(required = False)
    head_audio = AudioSerializer(required = False)
    head_image = ImageSerializer(required = False)
    paired_with_inv = SmallLinkSerializer(many = True)
    see_also_inv = SmallLinkSerializer(many = True)
    redirect_inv = SmallLinkSerializer(many = True)
    members = WordFamilyPairSerializer(many = True)
    relatedword_set = RelatedWordSerializer(many = True)
    word_parts = serializers.CharField()
    reduplication = serializers.CharField(max_length=200)
    region = RegionSerializer(many = True)
    stem = serializers.CharField(max_length=200)
    basic_audio = AudioForBasicFormSerializer(many = True)
    additional_audio = AdditionalAudioSerializer(many = True)
    inflectionalform_set = InflectionalFormSerializer(many=True)
    imageresource_set = ImageResourceSerializer(many=True)
    videoresource_set = VideoResourceSerializer(many=True)
    documentresource_set = DocumentResourceSerializer(many=True)

#class WordPartSerializer(serializers.Serializer):
    #url = serializers.CharField(max_length=200)
    #title = serializers.CharField(max_length=200)
    #type = serializers.CharField(max_length=200, default="")
    #gloss = serializers.CharField(default = "")
    #subtypes = serializers.CharField(max_length=200, default="")
    #words_that_use_this_part = MainEntrySerializer(many = True)

from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.



class Video(models.Model):
    src = models.CharField(primary_key = True, max_length=200)
    thumb = models.ForeignKey("dictionary.Image", on_delete = models.PROTECT)
    def __str__(self):
        return self.src

class Image(models.Model):
    src = models.CharField(primary_key = True, max_length=200)
    alt = models.CharField(max_length=200, default="", null=True)
    def __str__(self):
        return self.src


class PartOfSpeech(models.Model):
    abbrev = models.CharField(primary_key = True, max_length = 30,  verbose_name = "Abbreviation")
    full = models.CharField(max_length=200, verbose_name = "Full Name")
    description = models.TextField(default = "")
    section_url = models.CharField(max_length=200, verbose_name = "Full Name", default="", blank=True, null=True)
    def __str__(self):
        return self.abbrev


class Speaker(models.Model):
    image = models.ForeignKey("dictionary.Image", on_delete=models.PROTECT)
    href = models.CharField(primary_key = True, max_length=200)
    initials = models.CharField(max_length = 30)
    primary_name = models.CharField(max_length=200, verbose_name = "Primary Name")
    ojibwe_name = models.CharField(max_length=200, default = "", verbose_name = "Ojibwe Name")
    english_name = models.CharField(max_length=200, default = "", verbose_name = "English Name")
    community = models.CharField(max_length=200, default = "", verbose_name = "Community")
    region = models.CharField(max_length=200, default = "", verbose_name = "Region")
    description = RichTextField(default = "")
    def __str__(self):
        return self.primary_name

class News(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Title")
    date = models.CharField(max_length=200, verbose_name = "Date")
    html = RichTextField(default = "", verbose_name = "Content")
    def __str__(self):
        return self.title

class Audio(models.Model):
    regular = models.CharField(primary_key=True, max_length=200, verbose_name = "Regular File")
    mobile = models.CharField(max_length=200, verbose_name = "Mobile File", default = "")
    def __str__(self):
        return self.mobile

class AudioForBasicForm(models.Model):
    audio_for_basic_forms_index = models.IntegerField(primary_key = True)
    entry = models.ForeignKey("dictionary.MainEntry", related_name = "basic_audio", on_delete = models.PROTECT, null = True, blank = True)
    ojibwe = models.CharField(max_length=200, null = True, blank = True)
    poss = models.ManyToManyField("dictionary.Poss",  blank = True)
    def __str__(self):
        return self.ojibwe

class AdditionalAudio(models.Model):
    additional_audio_index = models.IntegerField(primary_key = True)
    entry = models.ForeignKey("dictionary.MainEntry", related_name = "additional_audio", on_delete = models.PROTECT, null = True, blank = True)
    ojibwe = models.CharField(max_length=200, null = True, blank = True)
    poss = models.ManyToManyField("dictionary.Poss",  blank = True)
    def __str__(self):
        return self.ojibwe
class SentenceExample(models.Model):
    sentence_examples_index = models.IntegerField(primary_key = True)
    entry = models.ForeignKey("dictionary.MainEntry", related_name = "sentence_examples", on_delete = models.PROTECT)
    ojibwe = models.TextField(default = "", null = True, blank = True)
    english = models.TextField(default = "", null = True, blank = True)
    def __str__(self):
        return self.ojibwe

class SentenceExampleAudioRec(models.Model):
    sentence_examples_index = models.ForeignKey("dictionary.SentenceExample", related_name="audio_rec", on_delete=models.PROTECT)
    speaker = models.ForeignKey("dictionary.Speaker", on_delete = models.PROTECT, default = "", null = True, blank = True)
    audio = models.ForeignKey("dictionary.Audio", on_delete = models.PROTECT, default="", null = True, blank = True)
    def __str__(self):
        return str(self.speaker) + ", " + str(self.audio)
    class Meta:
        verbose_name = "Sentence Example Audio and Speaker"

class AudioForBasicFormAudioRec(models.Model):
    audio_for_basic_forms_index = models.ForeignKey("dictionary.AudioForBasicForm", related_name="audio_rec", on_delete=models.PROTECT)
    speaker = models.ForeignKey("dictionary.Speaker", on_delete = models.PROTECT, default = "", null = True, blank = True)
    audio = models.ForeignKey("dictionary.Audio", on_delete = models.PROTECT, default="", null = True, blank = True)
    def __str__(self):
        return str(self.speaker) + ", " + str(self.audio)
    class Meta:
        verbose_name = "Basic Form Audio and Speaker"

class AdditionalAudioAudioRec(models.Model):
    additional_audio_index = models.ForeignKey("dictionary.AdditionalAudio", related_name="audio_rec", on_delete=models.PROTECT)
    speaker = models.ForeignKey("dictionary.Speaker", on_delete = models.PROTECT, default = "", null = True, blank = True)
    audio = models.ForeignKey("dictionary.Audio", on_delete = models.PROTECT, default="", null = True, blank = True)
    def __str__(self):
        return str(self.speaker) + ", " + str(self.audio)
    class Meta:
        verbose_name = "Additional Form Audio and Speaker"

class Region(models.Model):
    abbrev = models.CharField(max_length = 30, primary_key = True)
    full = models.CharField(max_length=200, default = "")
    description = models.TextField(default = "")
    def __str__(self):
        return f"{self.abbrev}: {self.full}"

class Poss(models.Model):
    abbrev = models.CharField(max_length = 30, primary_key = True)
    full = models.CharField(max_length=200, default = "")
    class Meta:
        verbose_name = "Inflectional Attributes"
    def __str__(self):
        return f"{self.abbrev}: {self.full}"


class InflectionalForm(models.Model):
    url = models.ForeignKey("dictionary.MainEntry",  on_delete=models.PROTECT)
    inflectional_forms_index = models.IntegerField(primary_key = True)
    form = models.CharField(max_length=200, null = True, blank = True)
    poss = models.ManyToManyField("dictionary.Poss",  blank = True)
    def __str__(self):
        return self.form + ''.join(pos.abbrev for pos in self.poss_set.all())


class ImageCollection(models.Model):
    url = models.CharField(primary_key = True, max_length=200)
    copyright = models.CharField(max_length=200, null = True, blank = True)
    title = models.CharField(max_length=200, null = True, blank = True)
    description = RichTextField( null = True, blank = True)
    image = models.ForeignKey("dictionary.Image", related_name="mainimage", on_delete=models.PROTECT, null = True, blank = True)
    def __str__(self):
        return self.title

class DocumentCollection(models.Model):
    url = models.CharField(primary_key = True, max_length=200)
    copyright = models.CharField(max_length=200, verbose_name = "Copyright", null = True, blank = True)
    title = models.CharField(max_length=200, verbose_name = "Title", null = True, blank = True)
    description = RichTextField(default = "", verbose_name = "Description", null = True, blank = True)
    body = models.TextField(default = "", verbose_name = "Document Body", null = True, blank = True)
    bibliography = models.TextField(default = "", verbose_name = "Bibliography", null = True, blank = True)
    def __str__(self):
        return self.title


class VideoCollection(models.Model):
    url = models.CharField(primary_key = True, max_length=200)
    copyright = models.CharField(max_length=200, verbose_name = "Copyright", null = True, blank = True)
    title = models.CharField(max_length=200, verbose_name = "Title", null = True, blank = True)
    description = RichTextField( verbose_name = "Description", null = True, blank = True)
    video = models.ForeignKey("dictionary.Video", on_delete=models.PROTECT, verbose_name = "Video", null = True, blank = True)
    def __str__(self):
        return self.title

class ImageResource(models.Model):
    url = models.ForeignKey("dictionary.MainEntry", on_delete = models.PROTECT, null = True, blank = True)
    image = models.ForeignKey("dictionary.Image", on_delete = models.PROTECT, null = True, blank = True)
    righthref = models.ForeignKey("dictionary.ImageCollection", on_delete = models.PROTECT, null = True, blank = True)
    righttext = models.CharField(max_length = 200, default = "", null = True, blank = True)
    def __str__(self):
        return self.righthref

class DocumentResource(models.Model):
    url = models.ForeignKey("dictionary.MainEntry", on_delete = models.PROTECT, null = True, blank = True)
    righthref = models.ForeignKey("dictionary.DocumentCollection", on_delete = models.PROTECT, null = True, blank = True)
    righttext = models.CharField(max_length = 200, default = "", null = True, blank = True)
    def __str__(self):
        return self.righthref

class VideoResource(models.Model):
    url = models.ForeignKey("dictionary.MainEntry", on_delete = models.PROTECT, null = True, blank = True)
    image = models.ForeignKey("dictionary.Image", on_delete = models.PROTECT, null = True, blank = True)
    righthref = models.ForeignKey("dictionary.VideoCollection", on_delete = models.PROTECT, null = True, blank = True)
    righttext = models.CharField(max_length = 200, default = "", null = True, blank = True)
    def __str__(self):
        return self.righthref

class WordFamily(models.Model):
    head = models.ForeignKey("dictionary.MainEntry", primary_key=True, related_name = "head_inv",  on_delete=models.PROTECT)
    def __str__(self):
        return self.head.head_lemma

class WordFamilyPair(models.Model):
    word_family = models.ForeignKey("dictionary.WordFamily", on_delete=models.PROTECT, related_name = "members" )
    kind = models.CharField(max_length = 200, default = "")
    member = models.ForeignKey("dictionary.MainEntry", related_name = "members",  on_delete=models.PROTECT)
    def __str__(self):
        return f"{self.kind}: {self.member.head_lemma}"

class RelatedWord(models.Model):
    title = models.CharField(max_length = 200, primary_key = True)
    word = models.ForeignKey("dictionary.MainEntry",  on_delete=models.PROTECT)
    def __str__(self):
        return self.title

class MainEntry(models.Model):
    url = models.CharField(primary_key = True, max_length=200)
    head_lemma = models.CharField(max_length=200, verbose_name = "Lemma", null = True, blank = True)
    part_of_speech = models.ForeignKey("dictionary.PartOfSpeech", on_delete=models.PROTECT, verbose_name = "Part Of Speech", null = True, blank = True)
    notes = RichTextField(default = "", null = True, blank = True)
    species = RichTextField(default = "", null = True, blank = True)
    gloss = RichTextField(default = "", null = True, blank = True)
    head_speaker = models.ForeignKey("dictionary.Speaker", default="", on_delete=models.PROTECT, verbose_name = "Main Speaker", null = True, blank = True)
    head_audio = models.ForeignKey("dictionary.Audio", default="", on_delete=models.PROTECT, verbose_name = "Main Audio", null = True, blank = True)
    head_image = models.ForeignKey("dictionary.Image", default="", on_delete=models.PROTECT, verbose_name = "Main Image", null = True, blank = True)
    paired_with = models.ManyToManyField("dictionary.MainEntry", related_name = "paired_with_inv",  default = "", verbose_name = "Paired With",  blank = True)
    see_also = models.ManyToManyField("dictionary.MainEntry", related_name = "see_also_inv", default = "",  verbose_name = "See Also",  blank = True)
    redirect = models.ManyToManyField("dictionary.MainEntry", related_name = "redirect_inv", default = "",  verbose_name = "Redirect to", blank = True)
    word_parts = RichTextField(default = "", null = True, blank = True)
    reduplication = models.CharField(max_length=200, default = "", null = True, blank = True)
    region = models.ManyToManyField("dictionary.Region",  blank=True)
    stem = models.CharField(max_length=200, default = "", null = True, blank = True)
    def __str__(self):
        return self.head_lemma + " (" + self.part_of_speech.abbrev + ")"
    class Meta:
        verbose_name = "Main Entry"

class WordPart(models.Model):
    url = models.CharField(primary_key = True,max_length=200)
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=200, default="")
    gloss = models.TextField(default = "")
    subtypes = models.CharField(max_length=200, default="")
    words_that_use_this_part = models.ManyToManyField("dictionary.MainEntry", blank = True, null = True)
    def __str__(self):
        return self.title + " (" + + self.type.text + ")"
    class Meta:
        verbose_name = "Word Part Entry"

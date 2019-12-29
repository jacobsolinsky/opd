from dictionary.serializers import *
from dictionary.models import *

from rest_framework.viewsets import ModelViewSet


from rest_framework.routers import SimpleRouter

class VideoViewSet(ModelViewSet):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()


class RelatedWordViewSet(ModelViewSet):
    serializer_class = RelatedWordSerializer
    queryset = RelatedWord.objects.all()

class TinyLinkViewSet(ModelViewSet):
    queryset = MainEntry.objects.all()
    serializer_class = TinyLinkSerializer


class SpeakerViewSet(ModelViewSet):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer


class ImageResourceViewSet(ModelViewSet):
    queryset = ImageResource.objects.all()
    serializer_class = ImageResourceSerializer


class VideoResourceViewSet(ModelViewSet):
    queryset = VideoResource.objects.all()
    serializer_class = VideoResourceSerializer


class DocumentResourceViewSet(ModelViewSet):
    queryset = DocumentResource.objects.all()
    serializer_class = DocumentResourceSerializer

class LittlePartOfSpeechViewSet(ModelViewSet):
    queryset = PartOfSpeech.objects.all()
    serializer_class = LittlePartOfSpeechSerializer

class PossViewSet(ModelViewSet):
    queryset = Poss.objects.all()
    serializer_class = PossSerializer

router = SimpleRouter()
router.register("videos", VideoViewSet)
router.register("relatedwords", RelatedWordViewSet)
router.register("tinylinks", TinyLinkViewSet)
router.register("speakers", SpeakerViewSet)
router.register("imageresources", ImageResourceViewSet)
router.register("videoresources", VideoResourceViewSet)
router.register("documentresources", DocumentResourceViewSet)
router.register("littlepartsofspeech", LittlePartOfSpeechViewSet)
router.register("poss", PossViewSet)

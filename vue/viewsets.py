from dictionary.serializers import *
from dictionary.models import *

from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, \
GenericViewSet, mixins
from rest_framework import permissions
from rest_framework.routers import SimpleRouter
from django.http import HttpResponse



class VideoViewSet(ModelViewSet):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()


class RelatedWordViewSet(ModelViewSet):
    serializer_class = RelatedWordSerializer
    queryset = RelatedWord.objects.all()

class TinyLinkViewSet(ReadOnlyModelViewSet):
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


class LittlePartOfSpeechViewSet(ReadOnlyModelViewSet):
    queryset = PartOfSpeech.objects.all()
    serializer_class = LittlePartOfSpeechSerializer


class PossViewSet(ModelViewSet):
    queryset = Poss.objects.all()
    serializer_class = PossSerializer


class MainEntryViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = MainEntry.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = MainEntrySerializer

    def create(self, request):
        MainEntrySerializer().create(request.data)
        return HttpResponse('created')



class OptionalSlashRouter(SimpleRouter):
    def __init__(self):
        self.trailing_slash = '/?'
        super(SimpleRouter, self).__init__()




router = OptionalSlashRouter()
router.register("videos", VideoViewSet)
router.register("relatedwords", RelatedWordViewSet)
router.register("tinylinks", TinyLinkViewSet)
router.register("speakers", SpeakerViewSet)
router.register("imageresources", ImageResourceViewSet)
router.register("videoresources", VideoResourceViewSet)
router.register("documentresources", DocumentResourceViewSet)
router.register("littlepartsofspeech", LittlePartOfSpeechViewSet)
router.register("poss", PossViewSet)
router.register("main-entry", MainEntryViewSet)

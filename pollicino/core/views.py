from rest_framework import parsers, renderers
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ClientTokenSerializer
from .models import ClientToken

class ObtainClientAuth(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = ClientTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        client_secret = serializer.data['client_secret']
        token, created = ClientToken.objects.get_or_create(client_secret=client_secret)
        return Response({'token': token.key})


obtain_client_auth = ObtainClientAuth.as_view()

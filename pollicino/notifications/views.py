from rest_framework import parsers, renderers
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import HTTP_HEADER_ENCODING, exceptions
from core.utils import decode_jwt
from core.models import App
from .models import Installation
from .serializers import SimpleInstallationSerializer

def get_client_header(request):
    """
    Return request's 'ClientAuthorization:' header, as a bytestring.
    Hide some test client ickyness where the header can be unicode.
    """
    auth = request.META.get('HTTP_AUTHORIZATION', b'')
    if isinstance(auth, type('')):
        # Work around django test client oddness
        auth = auth.encode(HTTP_HEADER_ENCODING)
    return auth



class ClientAPIView(APIView):

    def initial(self, request, *args, **kwargs):
        header = get_client_header(request).split()
        if header and header[0].lower() == 'token':
            try:
                payload = decode_jwt(header[1])
                if payload.get("app_id"):
                    app = App.objects.get(pk=payload["app_id"])
                    request.app = app
            except Exception, e:
                #todo : check exception ... 
                pass
        
        return super(ClientAPIView, self).initial(request, *args, **kwargs)



class RegisterDeviceView(ClientAPIView):
    throttle_classes = ()
    #todo: require request.app
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    
    def post(self, request, *args, **kwargs):
        serializer = SimpleInstallationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        app = request.app
        installation, created = Installation.objects.get_or_create(
            app=app, device_token=serializer.data["device_token"],
            platform=serializer.data["platform"])
        
        installation.app_version = serializer.data["app_version"]
        installation.save()

        return Response({ 'hey': installation.pk })


register_device_view = RegisterDeviceView.as_view()

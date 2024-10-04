from djoser.views import TokenCreateView
from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework.response import Response
from playground.main import CustomTokenCreateSerializer


# Create your views here.
class CustomTokenCreateView(TokenCreateView):
    serializer_class = CustomTokenCreateSerializer

    # @extend_schema(
    #     responses={
    #         200: OpenApiResponse(
    #             description="Custom Token Response",
    #             examples={
    #                 'application/json': {
    #                     'refresh': 'refresh-token-example',
    #                     'access': 'access-token-example',
    #                     'user': {
    #                         'id': 1,
    #                         'username': 'uznext',
    #                         'email': 'uznext17@gmail.com',
    #                     },
    #                     'remember_me': False
    #                 }
    #             }
    #         )
    #     }
    # )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)

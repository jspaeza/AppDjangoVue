from .models import Film
from rest_framework import viewsets
from .serializers import FilmSerializer
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class FilmView(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    parser_class = [FileUploadParser]
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

    def post(self, request, *args, **kwargs):
        film_serializer = FilmSerializer(data=request.data)
        if film_serializer.is_valid():
            film_serializer.save()
            return Response(film_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(film_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
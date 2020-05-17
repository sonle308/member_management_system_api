from django.http.multipartparser import MultiPartParser
from apps.position.serializers import PositionSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.settings import api_settings
from rest_framework_csv import renderers as r
from apps.position.models import Position


class PositionList(APIView):
    renderer_classes = (r.CSVRenderer,) + tuple(api_settings.DEFAULT_RENDERER_CLASSES)

    @classmethod
    def get_extra_actions(cls):
        return []

    def get(self, request, format=None):
        positions = Position.objects.all()
        serializer = PositionSerializer(positions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PositionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_renderer_context(self):
        context = super().get_renderer_context()
        context['header'] = (
            self.request.GET['fields'].split(',')
            if 'fields' in self.request.GET else None)
        return context


class PositionDetail(APIView):
    def get_object(self, pk):
        try:
            return Position.objects.get(pk=pk)
        except Position.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        position = self.get_object(pk)
        serializer = PositionSerializer(position)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        position = self.get_object(pk)
        serializer = PositionSerializer(position, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        position = self.get_object(pk)
        position.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FormParser(object):
    pass


class ImportCsv(APIView):
    serializer_class = PositionSerializer
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        try:
            serializer = PositionSerializer(data=request.data)
            print(serializer.initial_data)

            if serializer.is_valid():
                print(serializer.data)
                return Response("Done")
            else:
                print(serializer.errors)
                return Response("Not Done")

        except Exception as e:
            return Response(str(e))

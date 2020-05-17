from django.http.multipartparser import MultiPartParser
from apps.team.serializers import TeamSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.settings import api_settings
from rest_framework_csv import renderers as r
from apps.team.models import Team


class TeamList(APIView):
    renderer_classes = (r.CSVRenderer,) + tuple(api_settings.DEFAULT_RENDERER_CLASSES)

    @classmethod
    def get_extra_actions(cls):
        return []

    def get(self, request, format=None):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TeamSerializer(data=request.data)
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


class TeamDetail(APIView):
    def get_object(self, pk):
        try:
            return Team.objects.get(pk=pk)
        except Team.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        skill = self.get_object(pk)
        serializer = TeamSerializer(skill)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        skill = self.get_object(pk)
        serializer = TeamSerializer(skill, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        skill = self.get_object(pk)
        skill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FormParser(object):
    pass


class ImportCsv(APIView):
    serializer_class = TeamSerializer
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        try:
            serializer = TeamSerializer(data=request.data)
            print(serializer.initial_data)

            if serializer.is_valid():
                print(serializer.data)
                return Response("Done")
            else:
                print(serializer.errors)
                return Response("Not Done")

        except Exception as e:
            return Response(str(e))

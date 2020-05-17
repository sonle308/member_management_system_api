from rest_framework import serializers
from rest_framework import routers, serializers, viewsets, permissions
from apps.team.models import Team


# # Serializers define the API representation.
class TeamSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Team
        fields = ['name', 'abbreviation', 'description', 'leader_id']
        name = serializers.CharField(max_length=120)
        abbreviation = serializers.CharField(max_length=120)
        description = serializers.CharField()
        leader_id = serializers.IntegerField(default=0)

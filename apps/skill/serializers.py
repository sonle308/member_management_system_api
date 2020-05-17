from rest_framework import serializers
from rest_framework import routers, serializers, viewsets, permissions
from apps.skill.models import Skill


# # Serializers define the API representation.
class SkillSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Skill
        fields = ['name', 'level', 'used_year_number']
        name = serializers.CharField(max_length=120)
        level = serializers.CharField(max_length=120)
        used_year_number = serializers.IntegerField(default=0)

from rest_framework import serializers
from .models import *


class RegionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Region


class ArchiveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Archive


class DossierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dossier


class ScribeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Scribe


class PeriodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Period


class TextTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TextType

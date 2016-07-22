from rest_framework import serializers
from vocabularies.serializers import *
from places.serializers import *
from .models import *


class SignSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sign


class TabletSerializer(serializers.HyperlinkedModelSerializer):
    archive = ArchiveSerializer()
    place = PlaceSerializer()
    scribe = ScribeSerializer()
    period = PeriodSerializer()
    text_type = TextTypeSerializer()

    class Meta:
        model = Tablet


class TabletImageSerializer(serializers.HyperlinkedModelSerializer):
    tablet = TabletSerializer()

    class Meta:
        model = TabletImage


class GlyphSerializer(serializers.HyperlinkedModelSerializer):
    tablet = TabletSerializer()

    class Meta:
        model = Glyph

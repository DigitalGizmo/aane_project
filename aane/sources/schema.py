# from statistics import mode
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
# from pops.models import Visit

from .models import PrimarySource, Volume, SourceEntry

class PrimarySourceNode(DjangoObjectType):
  class Meta:
    model = PrimarySource
    filter_fields = ['id', 'title']
    interfaces = (relay.Node, )

class VolumeNode(DjangoObjectType):
  class Meta:
    model = Volume
    filter_fields = ['primary_source_id', 'title']
    interfaces = (relay.Node, )

class SourceEntryNode(DjangoObjectType):
  class Meta:
    model = SourceEntry
    filter_fields = ['volume_id', 'entry_text_html']
    interfaces = (relay.Node, )

class Query(ObjectType):
  # panel = relay.Node.Field(PanelNode)
  all_volumes = DjangoFilterConnectionField(VolumeNode)
  # all_articles = DjangoFilterConnectionField(ArticleNode)
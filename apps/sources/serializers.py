from rest_framework import serializers
from .models import SourceEntry

class SourceEntrySerializer(serializers.HyperlinkedModelSerializer):
    # relateds = RelatedSerializer(many=True, read_only=True)
    
    # bio = FieldQuillSerializer()
    # more_text = FieldQuillSerializer()
    class Meta:
        model = SourceEntry
        fields = [
            'id',
            'entry_text_html',
            'low_year',
            'low_month'          
        ]
        lookup_field = 'id'


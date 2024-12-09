from rest_framework import serializers
from .models import AAPerson


# class RelatedSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Related
#         fields = ['title', 'content_type', 'slug', 'link']
#         # person = serializers.ReadOnlyField(source='person.slug')

class FieldQuillSerializer(serializers.Field):
    def to_representation(self, value):
        # Assuming `value` is an instance of your FieldQuill class
        return {
            # 'json_string': value.json_string,
            # 'delta': value.delta,
            # 'plain': value.plain,
            'html': value.html,
        }
    
    def to_internal_value(self, data):
        pass

class AAPersonSerializer(serializers.HyperlinkedModelSerializer):
    # relateds = RelatedSerializer(many=True, read_only=True)
    
    bio = FieldQuillSerializer()
    # more_text = FieldQuillSerializer()
    class Meta:
        model = AAPerson
        fields = [
            'id',
            'name',
            'bio'          
        ]
        lookup_field = 'name'
from drf_writable_nested import WritableNestedModelSerializer
from rest_flex_fields.serializers import FlexFieldsSerializerMixin
from rest_framework import serializers

from . import utils

BASE_FIELDS = (
    'modified_by',
    'modified',
    'created_by'
)


class CWNModelSerializer(FlexFieldsSerializerMixin, WritableNestedModelSerializer):

    def create(self, validated_data):
        request = self.context.get('request', None)

        if request:
            validated_data['created_by'] = request.user.username
        else:
            validated_data['created_by'] = 'Auto'

        return super().create(validated_data)

    def update(self, instance, validated_data):

        request = self.context.get('request', None)

        if request:
            validated_data['modified_by'] = request.user.username
        else:
            validated_data['modified_by'] = 'Auto'

        return super().update(instance, validated_data)


class ChoicesField(serializers.Field):
    def __init__(self, choices, **kwargs):
        self.choices = choices
        self.to_value = utils.get_choice_name_value_dictionary(choices)
        self.to_repr = utils.reverse_of_simple_dictionary(self.to_value)
        super().__init__(**kwargs)

    def to_representation(self, value):
        return self.to_repr[value]

    def to_internal_value(self, data):
        if data in self.to_value.keys():
            return self.to_value[data]

        raise serializers.ValidationError(
            f"Acceptable values are {list(self.to_value.keys())}.")

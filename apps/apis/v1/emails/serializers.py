from apps.utils.serializers import BaseSerializer, BASE_FIELDS

from apps.emails import models as email_models


class EmailSerializer(BaseSerializer):

    class Meta:
        model = email_models.Email
        exclude = BASE_FIELDS

    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.send_email()
        return instance

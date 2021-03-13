from django.db import IntegrityError
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from ..models import Organization, Link, FAQ, NotificationSubscription, Alias


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['id', 'name', 'github_name', 'github_id', 'location', 'image_url', 'links', 'parent_organization', 'cti_contributor']
        depth = 1


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['id', 'link_type', 'url', 'organization', ]
        depth = 1


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer', 'view_count', ]
        depth = 1


class AliasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alias
        fields = ['id', 'tag', 'alias', ]
        depth = 1

class NotificationSubscriptionSerializer(serializers.Serializer):
    email_address = serializers.EmailField()
    notification_type = serializers.CharField()
    created_date = serializers.DateTimeField(read_only=True)
    ip_address = serializers.IPAddressField(read_only=True)

    def create(self, validated_data):
        try:
            return NotificationSubscription.objects.create(**validated_data)
        except IntegrityError:
            raise ValidationError(detail=f"We already have a subscription for {validated_data['email_address']}")

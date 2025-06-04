from django.utils import timezone
from rest_framework import serializers
from .models import Server, Promotion

class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = ['id', 'type', 'expires_at', 'paid']

class ServerSerializer(serializers.ModelSerializer):
    promotions = PromotionSerializer(many=True, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')
    color = serializers.SerializerMethodField()
    badges = serializers.SerializerMethodField()

    class Meta:
        model = Server
        fields = ['id', 'name', 'ip', 'owner', 'promotions', 'color', 'badges']

    def get_color(self, obj):
        active = obj.promotions.filter(expires_at__gt=timezone.now(), paid=True)
        if active.filter(type='highlight').exists():
            return 'yellow'
        if active.filter(type='featured').exists():
            return 'green'
        return 'default'

    def get_badges(self, obj):
        return list(obj.promotions.filter(expires_at__gt=timezone.now(), paid=True).values_list('type', flat=True))
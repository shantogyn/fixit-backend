from rest_framework import serializers
from .models import Service

class ServiceSerializer(serializers.ModelSerializer):
    service_image = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = "__all__"

    def get_service_image(self, obj):
        request = self.context.get("request")
        if obj.service_image:
            if request:
                return request.build_absolute_uri(obj.service_image.url)
            return obj.service_image.url
        return None

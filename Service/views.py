from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Service

class ServiceView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        services = Service.objects.all()

        data = [
            {
                "id": s.id,
                "provider_id": str(s.provider_id),
                "category_id": str(s.category_id),
                "title": str(s.title),
                "price": str(s.price),
                "description": str(s.description),
                "status": s.status,
                "location": s.location,
                "service_image": request.build_absolute_uri(s.service_image.url) if s.service_image else None
            }
            for s in services
        ]

        return Response(data)
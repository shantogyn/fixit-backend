from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Service
from .serializers import ServiceSerializer

class ServiceView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True, context={"request": request})
        return Response(serializer.data)

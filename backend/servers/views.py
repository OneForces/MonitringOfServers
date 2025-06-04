from django.utils import timezone
from rest_framework import generics, permissions
from .models import Server, Promotion
from .serializers import ServerSerializer, PromotionSerializer

class ServerListCreateView(generics.ListCreateAPIView):
    serializer_class = ServerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Server.objects.all()
        if self.request.query_params.get('my'):
            queryset = queryset.filter(owner=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PromotionPurchaseView(generics.CreateAPIView):
    serializer_class = PromotionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(paid=True, expires_at=timezone.now() + timezone.timedelta(days=7))

class ServerDetailView(generics.RetrieveAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    permission_classes = [permissions.IsAuthenticated]
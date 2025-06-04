from django.urls import path
from .views import ServerListCreateView, PromotionPurchaseView, ServerDetailView

urlpatterns = [
    path('servers/', ServerListCreateView.as_view(), name='server-list-create'),
    path('servers/<int:pk>/', ServerDetailView.as_view(), name='server-detail'),
    path('servers/<int:pk>/promote/', PromotionPurchaseView.as_view(), name='promotion-purchase'),
]
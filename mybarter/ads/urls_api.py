from rest_framework.routers import DefaultRouter
from .views_api import AdViewSet, ExchangeProposalViewSet

router = DefaultRouter()
router.register(r'ads', AdViewSet, basename='ad')
router.register(r'exchange-proposals', ExchangeProposalViewSet)

urlpatterns = router.urls

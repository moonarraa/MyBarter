from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from ads.views_api import AdViewSet, ExchangeProposalViewSet

router = DefaultRouter()
router.register(r'ads', AdViewSet, basename='ad')
router.register(r'exchange-proposals', ExchangeProposalViewSet, basename='exchangeproposal')

schema_view = get_schema_view(
    openapi.Info(
        title="MyBarter API",
        default_version='version1',
        description="Документация MyBarter API",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("admin/", admin.site.urls),

    # drf-api urls
    path('api/', include(router.urls)),

    # swagger, redoc urls
    path('api/swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

from . import views
from django.urls import path,include
from rest_framework import routers
from apis.views import PriceViewSet

app_name="test"

router = routers.DefaultRouter()

# Prefix : products / Viewset : PriceViewSet
router.register('products',PriceViewSet)


urlpatterns=[
    path('api/',include(router.urls)),
    path('',views.IndexView.as_view(),name='index_page')
]
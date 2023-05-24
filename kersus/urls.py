from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework import routers
from kersus_app.views import CategoryView, ParticipantView

router = routers.DefaultRouter()

router.register(r'category', CategoryView)
router.register(r'participant', ParticipantView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', TemplateView.as_view(template_name='index.html')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

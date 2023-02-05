from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from todo.views import ProductViewSet,EmailView

from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register('products', ProductViewSet)


urlpatterns = [
    path('', include(router.urls)),
    #path('test/', send_email, name ='test'),
    path('test/', EmailView.as_view()),
    path('admin/', admin.site.urls)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
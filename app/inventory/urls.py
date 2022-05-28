from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include # new
from django.views.generic.base import TemplateView # new
urlpatterns = [
    # path("", image_upload, name="upload"),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),  # new
    path("", TemplateView.as_view(template_name='home.html'), name='home'), # new
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

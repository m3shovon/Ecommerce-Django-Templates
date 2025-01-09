from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns # static
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("django-check-seo/", include("django_check_seo.urls")),
    # for SEO:
    # http://127.0.0.1:8000/django-check-seo/?page=/
    path('', include('App_Shop.urls')),
    path('account/', include('App_Login.urls')),
    path('order/', include('App_Order.urls')),
    path('payment/', include('App_Payment.urls')),
    # path('userlog/', include('App_UserLog.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
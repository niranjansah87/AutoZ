"""AutoZ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from Admin.views import order_list,msg_delete,admin_msg,car_list,order_created,loginrequired

urlpatterns = [
    path('admin/', admin.site.urls),
path("",include('RMSapp.urls')),
    path("car/",include('Admin.urls')),
    path('listOrder/', order_list, name = "order_list"),
    path('message/', admin_msg, name='message'),
    path('accounts/login/?next=/car/',loginrequired),
    # path('accounts/',include('allauth.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),  # <-- here
    # path('login/defender/',include('defender.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


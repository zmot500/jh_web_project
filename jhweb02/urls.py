"""jhweb02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url,include
from patient import views
#from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r"^$", views.home),
    url(r"^insert_patient$", views.insert_patient),
    url(r"^detail_patient$", views.detail_patient),
    url(r"^insert_check$", views.insert_check),
    url(r"^detail_check$", views.detail_check),
    url(r"^update_check$", views.update_check),
    url(r"^delete_check$", views.delete_check),
]

#if settings.DEBUG:
#    import debug_toolbar
#    urlpatterns += [
#        url(r'^__debug__/', include(debug_toolbar.urls)),
#        ]

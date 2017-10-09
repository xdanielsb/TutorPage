"""CleverPage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls import patterns


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'mypage.views.home', name='home'), #home
    url(r'^dashboard/', 'mypage.views.dashboard', name='dashboard'), #dashboard
    url(r'^dynamicProgramming/', 'mypage.views.dynamicProgramming', name='dynamicProgramming'), #dynamic Programming
    url(r'^boltzman/', 'mypage.views.boltzman', name='boltzman'), #boltzman
]

#Help me to see the static files
urlpatterns += patterns ('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)



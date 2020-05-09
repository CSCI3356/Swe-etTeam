"""loginPage_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
#from django.urls import include
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('createPeerAssessment/', TemplateView.as_view(template_name="createPeerAssessment.html"), name='createPeerAssessment'),
    url('instructorResults/', TemplateView.as_view(template_name="instructorResults.html"), name='instructorResults'),
    url('takePeerAssessment/', TemplateView.as_view(template_name="takePeerAssessment.html"), name='takePeerAssessment'),
    url('studentResults/', TemplateView.as_view(template_name="studentResults.html"), name='studentResults'),
    url('accounts/', include('accounts.urls')),
    url('accounts/', include('django.contrib.auth.urls')), # new
    url('', TemplateView.as_view(template_name='home.html'), name='home')

]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


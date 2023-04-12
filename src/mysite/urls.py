"""mysite URL Configuration

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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from personal.views import(
	home_screen_view,
    index_view,
    blogpost_view,
    userprofile_view,
    doctor_index_view,
    doctor_blogpost_view,
    doc_profile_view,
    covid_view,
    product_view,
       
)
from account.views import(
    registration_view,
    logout_view,
    login_view,
    doc_login_view,
    doc_reg_view,

)
urlpatterns = [
    path('',home_screen_view, name="home"),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', 'blog')),
    path('blogpost/',blogpost_view, name="blogpost"),
    path('doctor_blogpost/',doctor_blogpost_view, name="doctor_blogpost"),
    path('index/',index_view, name="index"),
    path('logout/',logout_view, name="logout"),
    path('login/',login_view, name="login"),
    path('doctor_login/',doc_login_view, name="doctor_login"),
    path('doctor_index/',doctor_index_view, name="doctor_index"),
    path('register/',registration_view, name="register"),
    path('doctor_register/',doc_reg_view, name="doctorregister"),
    path('userprofile/',userprofile_view, name="userprofile"),
    path('doctor_profile/',doc_profile_view, name="doctorprofile"),
    path('covidlist/',covid_view, name="covidlist"),
    path('product/',product_view, name="product"),
    path('', include('store.urls', 'store'))

   
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
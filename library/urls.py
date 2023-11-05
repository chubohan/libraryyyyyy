"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from mysite import views 
from mysite.views import search_books
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage,name='homepage'), #連到view的homepage
    path('post/<slug:slug>/',views.showpost,name="showpost"),
    path('function1/<slug:slug>/', views.function1, name='function1'),
    path('function2/<slug:slug>/', views.function2, name='function2'),
    path('function/<slug:slug>/', views.function, name='function'),
    path('search_books/',views.search_books, name='search_books')
]

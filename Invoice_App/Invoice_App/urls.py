"""Invoice_App URL Configuration

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
''' path('',login_user,name="login"),
    path('welcome/',welcome,name="welcome"),
    path('signup/', views.signup),
    path('logout/',logout_user,name="logout"),
'''

from django.contrib import admin
from django.urls import path,include
from Invoice_App import views
from Invoice_App.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.mainpage,name='mainpage'),
    path('welcome/', views.welcome,name='welcome'),
    path('login/', views.login_user,name='login'),
    path('signup/', views.signup,name='signup'),
    path('logout/', views.logout,name='logout'),
    path('inventory/', views.inventory,name='inventory'),
    path('orderhistory/', views.orderhistory,name='orderhistory'),
    path('billing/', views.billing,name='billing'),
    path('delete/<int:id>/', views.delete, name='deletedata'),
    path('update/<int:id>/', views.update, name='updatedata'),
    path('pdf/', views.gen_pdf,name ='pdf'),
    path('view/<int:id>/', views.view, name='view'),

]


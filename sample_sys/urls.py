"""sample_sys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from app import views
from app.view import sample_type
from app.view import cancer_type
from app.view import surgery_method
from app.view import medication
from app.view import dashboard
from app.view import box_position


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),

    # login, logout
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    path('Dashboard/', dashboard.Dashboard, name='Dashboard'),

    path('SampleTypeList/', sample_type.SampleTypeList.as_view(), name='SampleTypeList'),
    path('sample_type_create/', sample_type.create, name='sample_type_create'),
    path('sample_type_update/', sample_type.update, name='sample_type_update'),
    path('sample_type_delete/', sample_type.delete, name='sample_type_delete'),

    path('CancerTypeList/', cancer_type.CancerTypeList.as_view(), name='CancerTypeList'),
    path('cancer_type_create/', cancer_type.create, name='cancer_type_create'),
    path('cancer_type_update/', cancer_type.update, name='cancer_type_update'),
    path('cancer_type_delete/', cancer_type.delete, name='cancer_type_delete'),

    path('SurgeryMethodList/', surgery_method.SurgeryMethodList.as_view(), name='SurgeryMethodList'),
    path('surgery_method_create/', surgery_method.create, name='surgery_method_create'),
    path('surgery_method_update/', surgery_method.update, name='surgery_method_update'),
    path('surgery_method_delete/', surgery_method.delete, name='surgery_method_delete'),

    path('MedicationList/', medication.MedicationList.as_view(), name='MedicationList'),
    path('medication_create/', medication.create, name='medication_create'),
    path('medication_update/', medication.update, name='medication_update'),
    path('medication_delete/', medication.delete, name='medication_delete'),

    path('BoxPositionList/', box_position.BoxPositionList.as_view(), name='BoxPositionList'),
    path('box_position_create/', box_position.create, name='box_position_create'),
    path('box_position_update/', box_position.update, name='box_position_update'),
    # path('box_position_delete/', box_position.delete, name='box_position_delete'),
]

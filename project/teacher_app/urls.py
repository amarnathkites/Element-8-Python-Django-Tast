
from django.urls import path,include
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index,name='index'),
    path('admin_login_action',views.admin_login_action,name='admin_login_action'),
    path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),
    path('admin_add_teacher',views.admin_add_teacher,name='admin_add_teacher'),
    path('admin_upload_teachers_details_action',views.admin_upload_teachers_details_action,name='admin_upload_teachers_details_action'),
    path('admin_view_teacher',views.admin_view_teacher,name='admin_view_teacher'),
    path('view_teacher_more_details',views.view_teacher_more_details,name='view_teacher_more_details'),
    path('search_result',views.search_result,name='search_result'),
    path('logout',auth_views.LogoutView.as_view(),name="logout"),
    path('login_page',views.login_page,name='login_page'),

    

]

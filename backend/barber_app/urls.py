from django.urls import re_path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    re_path(r'^$', views.api_root, name='api-root'),
    re_path(r'^auth/register/?$', csrf_exempt(views.RegisterView.as_view()), name='register'),
    re_path(r'^auth/login/?$', csrf_exempt(views.LoginView.as_view()), name='login'),
    re_path(r'^auth/logout/?$', csrf_exempt(views.LogoutView.as_view()), name='logout'),
    re_path(r'^appointments/?$', views.AppointmentList.as_view(), name='appointment-list'),
    re_path(r'^appointments/(?P<pk>\d+)/?$', views.AppointmentDetail.as_view(), name='appointment-detail'),
    re_path(r'^appointments/my/?$', views.MyAppointments.as_view(), name='my-appointments'),
]

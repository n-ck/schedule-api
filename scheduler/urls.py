from django.conf.urls import url
# from .views import AppointmentsList, AppointmentsDetail
from . import views


urlpatterns = [
    url(r'^schedule/get/(?P<pk>.+)$', views.ScheduleView.as_view({'get': 'retrieve'})),
    url(r'^schedule/create/$', views.ScheduleView.as_view({'post': 'create'})),
    url(r'^schedule/delete/(?P<pk>.+)$', views.ScheduleView.as_view({'delete': 'destroy'})),

    url(r'^appointment/get/(?P<pk>.+)$', views.AppointmentView.as_view({'get': 'retrieve'})),
    url(r'^appointment/create/$', views.AppointmentView.as_view({'post': 'create'})),
    url(r'^appointment/delete/(?P<pk>.+)$', views.AppointmentView.as_view({'delete': 'destroy'})),

]

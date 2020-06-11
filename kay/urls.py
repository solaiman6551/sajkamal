from django.contrib import admin
from django.urls import path, re_path
from meetingApp.views import view_all, show_time_slot, reserve_time_slot


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view_all, name="view_all"),
    re_path(r"""^time/(?P<id>(\d)+)$""", show_time_slot, name="show_time_slot"),
    re_path(r"""^time/reservation/(?P<id>(\d)+)$""", reserve_time_slot, name="reserve_time_slot"),

]

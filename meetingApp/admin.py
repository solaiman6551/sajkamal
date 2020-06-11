from django.contrib import admin
from .models import TimeSlot
from .models import Booking


admin.site.register(TimeSlot)
admin.site.register(Booking)

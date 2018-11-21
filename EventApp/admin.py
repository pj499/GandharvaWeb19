from django.contrib import admin
from .models import EventMaster,EventDepartment,Department,SponsorMaster,Carousel

admin.site.register(EventMaster)
admin.site.register(EventDepartment)
admin.site.register(Department)
admin.site.register(SponsorMaster)
admin.site.register(Carousel)

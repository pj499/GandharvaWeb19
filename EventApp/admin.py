from django.contrib import admin
from .models import EventMaster,EventDepartment,Department,SponsorMaster,Carousel,ContactUs,MyUser


admin.site.register(MyUser)
admin.site.register(EventMaster)
admin.site.register(EventDepartment)
admin.site.register(Department)
admin.site.register(SponsorMaster)
admin.site.register(Carousel)
admin.site.register(ContactUs)
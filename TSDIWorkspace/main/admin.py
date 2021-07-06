from django.contrib import admin
from .models import Testing, Lease, Bill, ServiceRequest, MailAndPackage, Notification

# Register your models here.
admin.site.register(Testing)
admin.site.register(Lease)
admin.site.register(Bill)
admin.site.register(ServiceRequest)
admin.site.register(MailAndPackage)
admin.site.register(Notification)

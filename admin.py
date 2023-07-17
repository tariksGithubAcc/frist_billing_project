from django.contrib import admin
from .models import SMSMessage

admin.site.register(SMSMessage)

admin.site.site_header = 'Admin Dashboard'


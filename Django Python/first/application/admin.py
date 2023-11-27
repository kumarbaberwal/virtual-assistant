from django.contrib import admin

# Register your models here.

from application.models import Contact
admin.site.register(Contact)

from application.models import Audio
admin.site.register(Audio)

from application.models import Additional_information
admin.site.register(Additional_information)
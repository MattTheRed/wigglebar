from django.contrib import admin
from bar.models import Bar


#from register_user.models import BarUser

class BarAdmin(admin.ModelAdmin):
	pass
admin.site.register(Bar, BarAdmin)

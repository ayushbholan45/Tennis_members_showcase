from django.contrib import admin
from .models import Member     # added

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "joined_date", "phone")


admin.site.site_header = "My Tennis Club Admin"  
admin.site.site_title = "Tennis Club Portal" 
admin.site.index_title = "Welcome to the Tennis Club Admin Portal"
admin.site.register(Member, MemberAdmin)         # added


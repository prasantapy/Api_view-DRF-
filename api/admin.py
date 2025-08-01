from django.contrib import admin
from api.models import Job_Profile
# Register your models here.
@admin.register(Job_Profile)
class profileAdmin(admin.ModelAdmin):
    list_display=['id','username','password','gender','skill','Age','Email_id']
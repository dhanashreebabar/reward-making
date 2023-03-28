from django.contrib import admin
from . models import Task,TaskLinks
# Register your models here.
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('user',)


class TaskeAdmin(admin.ModelAdmin):
    list_display = ('user','account_balance', 'created_at','description','status','task_complete')    

class TaskLinksAdmin(admin.ModelAdmin):
    list_display = ('user','youtubelink','task1', 'video','task2','ig','task3','share','task4')    
#admin.site.register(Profile,ProfileAdmin)    
admin.site.register(Task,TaskeAdmin)    
admin.site.register(TaskLinks,TaskLinksAdmin)    
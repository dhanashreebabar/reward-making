from django.db import models
from django.contrib.auth.models import User



class Task(models.Model):
    COMPLETE = 'Complete'
    INCOMPLETE = 'Incomplete'
    STATUS = [
        (COMPLETE,'Complete'),
        (INCOMPLETE,'Incomplete',)

    ]
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    account_balance = models.FloatField(default=100)

    created_at = models.DateTimeField(auto_now_add=True)
    #task =  models.ForeignKey(User,on_delete = models.CASCADE,null=True)
    #task_links =  models.ForeignKey(TaskLinks,on_delete = models.CASCADE,null=True)

    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=200,choices=STATUS,default=INCOMPLETE)
    task_complete =models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.user.username    


class TaskLinks(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE,null=True)
    youtubelink = models.URLField(max_length=2000,default='https://www.youtube.com/')
    task1=models.CharField(max_length=200,help_text='False',null=True)
    video = models.URLField(max_length=2000,default='https://www.youtube.com/')
    task2 =models.CharField(max_length=200,help_text='False',null=True)

    ig = models.URLField(max_length=2000,default='https://www.youtube.com/')
    task3 =models.CharField(max_length=200,help_text='False',null=True)

    share = models.URLField(max_length=2000,default='https://www.youtube.com/')
    task4 =models.CharField(max_length=200,help_text='False',null=True)

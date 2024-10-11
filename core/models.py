from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):

    #one to many relationship
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='tasks')

    #create fields
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_done = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.user) + ' ' + self.title


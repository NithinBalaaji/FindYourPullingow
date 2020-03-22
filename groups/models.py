from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django import template
from django.urls import reverse

register = template.Library()

class Group(models.Model):
    name = models.CharField(max_length=255 ,unique=True)
    description = models.TextField(blank=True, default='')
    members = models.ManyToManyField(User, through = 'GroupMember')

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
         self.slug = slugify(self.name)
         super().save(*args,**kwargs)

    def get_absolute_url(self):
         return reverse('single-group',kwargs={'pk': self.pk})     
   

class GroupMember(models.Model):
    group = models.ForeignKey(Group,related_name='memberships',on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_groups',on_delete=models.CASCADE)

    def __str__(self):
        return self.user

    class Meta:
        unique_together = ('group','user')    

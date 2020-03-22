from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from  django.urls import reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView, 
    RedirectView
)# Create your views here.
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .models import Group, GroupMember
from .forms import GroupCreationForm

class CreateGroup(LoginRequiredMixin,CreateView):
    model = Group
    form_class = GroupCreationForm

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class SingleGroup(DetailView):
    model = Group

class ListGroups(ListView):
    model = Group
    template_name ='groups/group_list.html'
    context_object_name = 'groups'

    def get_query_set(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Group.objects.filter(author=user).order_by('-date_posted')    

class JoinGroup(LoginRequiredMixin,RedirectView):
    
    def get_redirect_url(self,*args,**kwargs):
        return reverse('single-group', kwargs={'pk': self.pk})

    def get(self,request,*args,**kwargs):
        group = get_object_or_404(Group, name=self.kwargs.get('name'))

        try:
            GroupMember.objects.create(user=self.request.user, group=group)

        except IntegrityError:
            messages.warning(self.request,'You are already a member!')
        else:
            messages.success(self.request,'You are now a member of the group!')  

        return super().get(request,*args,**kwargs) 


class LeaveGroup(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self,*args,**kwargs):
        return reverse('single-group')

    def get(self,request,*args, **kwargs):

        try:
            membership = get_object_or_404(GroupMember, user=self.kwargs.get('user'))

        except GroupMember.DoesNotExist:
            messages.warning(self.request, 'Sorry! You are not part of this group')
        else:
            membership.delete()
            messages.success(self.request, 'You have left the group!')

        return super().get(request) 

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Event
from .forms import EventCreationForm



class EventListView(ListView):
    model = Event
    template_name ='events/home.html'
    context_object_name = 'events'
    paginate_by = 2

class UserEventListView(ListView):
    model = Event
    template_name ='events/user_posts.html'
    context_object_name = 'events'
    paginate_by = 2

    def get_query_set(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Event.objects.filter(author=user).order_by('-date_posted')


class EventDetailView(DetailView):
    model = Event

class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventCreationForm
       
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    fields = ['event_name' , 'content', 'date_event', 'time_event']
    

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


    def test_func(self):
        event = self.get_object()
        if self.request.user == event.author:
             return True
        return False
        
class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    success_url = '/'

    def test_func(self):
        event = self.get_object()
        if self.request.user == event.author:
             return True
        return False


def about(request):
    return render(request, 'events/about.html', {'title': 'About'})

    

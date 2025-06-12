from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Bug
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q



class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

class BugListView(LoginRequiredMixin, ListView):
    model = Bug
    template_name = 'bugtracker/bug_list.html'
    context_object_name = 'bugs'
    login_url = '/accounts/login/'   # 👈 Redirects to login if user not logged in


    def get_queryset(self):
        return Bug.objects.filter(
            Q(created_by=self.request.user) | Q(assigned_to=self.request.user)
        ).distinct()

class BugDetailView(LoginRequiredMixin, DetailView):
    model = Bug
    template_name = 'bugtracker/bug_detail.html'

class BugCreateView(LoginRequiredMixin, CreateView):
    model = Bug
    fields = ['title', 'description', 'status', 'assigned_to']
    template_name = 'bugtracker/bug_form.html'
    success_url = reverse_lazy('bugtracker:bug_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class BugUpdateView(LoginRequiredMixin, UpdateView):
    model = Bug
    fields = ['title', 'description', 'status', 'assigned_to']
    template_name = 'bugtracker/bug_form.html'
    success_url = reverse_lazy('bugtracker:bug_list')

class BugDeleteView(LoginRequiredMixin, DeleteView):
    model = Bug
    template_name = 'bugtracker/bug_confirm_delete.html'
    success_url = reverse_lazy('bugtracker:bug_list')


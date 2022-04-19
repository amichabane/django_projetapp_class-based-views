from django.shortcuts import render
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Notes


class NotesList(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = 'notes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = context['notes'].filter(user=self.request.user)
        context['count'] = context['notes'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['notes'] = context['notes'].filter(title__icontains=search_input)

        context['search_input'] = search_input
        return context


class NotesDetail(LoginRequiredMixin, DetailView):
    model = Notes
    context_object_name = 'notes'


class NotesCreate(LoginRequiredMixin, CreateView):
    model = Notes
    fields = ['title', 'desciption', 'tags','complete','category']
    success_url = reverse_lazy('note')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NotesCreate, self).form_valid(form)


class NotesUpdate(LoginRequiredMixin, UpdateView):
    model = Notes
    fields = ['title', 'desciption', 'tags','complete','category']
    success_url = reverse_lazy('note')


class NotesDelete(LoginRequiredMixin, DeleteView):
    model = Notes
    fields = ['title', 'desciption', 'tags','complete','category']
    success_url = reverse_lazy('note')

    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)

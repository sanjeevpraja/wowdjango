from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from .models import *
from .forms import ExerciseForm
from django.core import serializers
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView, View
import json


class ExerciseView(ListView):
    model = Exercise
    context_object_name = 'model'
    template_name = 'exercise.html'
    paginate_by = 5


class ExerciseListView(ListView):
    model = Exercise
    context_object_name = 'model'
    template_name = '_exercise-list.html'


class ExerciseCreateView(CreateView):
    model = Exercise
    form_class = ExerciseForm
    form_prefix = 'create'
    template_name = '_exercise-create.html'

    def get_form_kwargs(self):
        kwargs = super(CreateView, self).get_form_kwargs()
        if self.form_prefix:
            kwargs.update({'prefix': self.form_prefix})
        return kwargs

    def post(self, request, *args, **kwargs):
        form_data = ExerciseForm(self.request.POST, self.request.FILES, prefix="create")
        print(form_data.is_valid())
        if form_data.is_valid():
            # form_data.save()
            instance = form_data.save()
            ser_instance = serializers.serialize('json', [instance, ])
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            return JsonResponse(form_data.errors, status=500)


class ExerciseDeleteView(DeleteView):
    model = Exercise
    context_object_name = 'model'
    template_name = '_exercise-confirm-delete.html'
    success_url = "/exercise"


class ExerciseEditView(UpdateView):
    model = Exercise
    context_object_name = 'model'
    form_class = ExerciseForm
    template_name = '_exercise-edit.html'
    form_prefix = None  # this is passed in url
    success_url = reverse_lazy('exercise:exercise')

    def get_form_kwargs(self):
        kwargs = super(UpdateView, self).get_form_kwargs()
        if self.form_prefix:
            kwargs.update({'prefix': self.form_prefix})
        return kwargs

    # def get_success_url(self):
    #     exercise_id = self.kwargs['pk']
    #     return reverse_lazy('exercise:exercise_edit', kwargs={'pk': exercise_id})

    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Exercise, id=self.kwargs['pk'])
        form_data = ExerciseForm(self.request.POST, self.request.FILES, prefix="edit", instance=obj)
        # update_item = Exercise.objects.filter(id=self.kwargs['pk'])
        if form_data.is_valid():
            instance = form_data.save()
            ser_instance = serializers.serialize('json', [instance, ])
            return JsonResponse({"exercise": ser_instance}, status=200)
        else:
            return JsonResponse(form_data.errors, status=500)


class ExerciseDetailView(DetailView):
    model = Exercise
    context_object_name = 'model'
    template_name = '_exercise-detail.html'


def sorry(request):
    return render(request, 'sorry.html')

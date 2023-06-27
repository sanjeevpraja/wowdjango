from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import *
from .forms import ExerciseForm
from django.core import serializers
from django.http import JsonResponse
from django.views.generic import ListView, CreateView
import json


class ExerciseView(ListView):
    model = Exercise
    context_object_name = 'model'
    template_name = 'exercise.html'


# def exercise(request):
#     model = Exercise.objects.all()
#     if request.user.is_authenticated:
#         form = ExerciseForm(prefix="create")
#         user_group = request.user.groups.all
#     else:
#         form = "no_access"
#         user_group = "none"
#     content = {'form': form, "model": model, "group": user_group}
#     if request.method == 'GET':
#         return render(request, 'exercise.html', content)

class ExerciseListView(ListView):
    model = Exercise
    context_object_name = 'model'
    template_name = '_exercise-list.html'


# def exercise_list(request):
#     model = Exercise.objects.all()
#     if request.user.is_authenticated:
#         form = ExerciseForm()
#         user_group = request.user.groups.all
#     else:
#         form = "no_access"
#         user_group = "none"
#     content = {"model": model}
#     if request.method == 'GET':
#         return render(request, '_exercise-list.html', content)


class ExerciseCreateView(CreateView):
    model = Exercise
    form_class = ExerciseForm
    template_name = '_exercise-create.html'

    def form_valid(self, form):
        instance = form.save()

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


#
# def exercise_create(request):
#     if request.user.is_authenticated:
#         form = ExerciseForm(prefix="create")
#     else:
#         form = "no_access"
#     content = {'form': form}
#     if request.method == 'GET':
#         return render(request, '_exercise-create.html', content)
#     elif request.method == "POST":
#         form_data = ExerciseForm(request.POST, request.FILES, prefix="create")
#         if form_data.is_valid():
#             # form_data.save()
#             instance = form_data.save()
#             ser_instance = serializers.serialize('json', [instance, ])
#             return JsonResponse({"instance": ser_instance}, status=200)
#         else:
#             return JsonResponse(form_data.errors, status=500)


def exercise_delete(request, pk):
    if request.method == "GET":
        exercise_obj = Exercise.objects.get(pk=pk)
        exercise_obj.delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


def exercise_edit(request, pk):
    if request.user.is_authenticated:
        user_group = request.user.groups.all
        if request.method == 'GET':
            exercise_obj = Exercise.objects.get(pk=pk)
            steps = exercise_obj.steps
            print(type(steps))
            form = ExerciseForm(instance=exercise_obj, prefix="edit")
            content = {'form': form, "model": exercise_obj, "group": user_group, "steps": steps}
            return render(request, '_exercise-edit.html', content)
        elif request.method == "POST":
            old_image = Exercise.objects.get(pk=pk)
            form = ExerciseForm(request.POST, files=request.FILES or None, instance=old_image, prefix="edit")
            if form.is_valid():
                form.save()
                instance = form.save()
                ser_instance = serializers.serialize('json', [instance, ])
                return JsonResponse({"instance": ser_instance}, status=200)
            else:
                return JsonResponse(form.errors, status=500)

    else:
        return redirect('exercise:sorry')


def exercise_detail(request, pk):
    if request.user.is_authenticated:
        user_group = request.user.groups.all
        if request.method == 'GET':
            exercise_obj = Exercise.objects.get(pk=pk)
            content = {"model": exercise_obj, "group": user_group}
            return render(request, '_exercise-detail.html', content)
    else:
        return redirect('exercise:sorry')


def sorry(request):
    return render(request, 'sorry.html')

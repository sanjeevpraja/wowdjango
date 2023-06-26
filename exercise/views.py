import os.path

from django.shortcuts import render, get_object_or_404, redirect
from django.utils.dateparse import parse_duration

from .models import *
from .forms import ExerciseForm
from django.core import serializers
from django.http import JsonResponse
import json


# Create your views here.
# def login_success(request):
#     """
#     Redirects users based on whether they are in the admins group
#     """
#     if request.user.groups.filter(name="Trainee").exists():
#         print('sfa')
#         return redirect("exercise")
#     else:
#         return redirect("admin_list")


def exercise(request):
    model = Exercise.objects.all()
    if request.user.is_authenticated:
        form = ExerciseForm(prefix="create")
        user_group = request.user.groups.all
    else:
        form = "no_access"
        user_group = "none"
    content = {'form': form, "model": model, "group": user_group}
    if request.method == 'GET':
        return render(request, 'exercise.html', content)

    # this is not required since exercise_create function is created
    # elif request.method == "POST":
    #     form_data = ExerciseForm(request.POST, request.FILES)
    #     if form_data.is_valid():
    #         form_data.save()
    #         #instance = form_data.save()
    #         # ser_instance = serializers.serialize('json', [instance, ])
    #         # return JsonResponse({"instance": ser_instance}, status=200)
    #         return render(request, 'exercise.html', content)
    #     else:
    #         return JsonResponse(form_data.errors, status=500)


def exercise_create(request):
    if request.user.is_authenticated:
        form = ExerciseForm(prefix="create")
    else:
        form = "no_access"
    content = {'form': form}
    if request.method == 'GET':
        return render(request, '_exercise-create.html', content)
    elif request.method == "POST":
        form_data = ExerciseForm(request.POST, request.FILES, prefix="create")
        if form_data.is_valid():
            #form_data.save()
            instance = form_data.save()
            ser_instance = serializers.serialize('json', [instance, ])
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            return JsonResponse(form_data.errors, status=500)


def exercise_list(request):
    model = Exercise.objects.all()
    if request.user.is_authenticated:
        form = ExerciseForm()
        user_group = request.user.groups.all
    else:
        form = "no_access"
        user_group = "none"
    content = {"model": model}
    if request.method == 'GET':
        return render(request, '_exercise-list.html', content)


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
            # working
            # exercise_obj = Exercise.objects.filter(pk=pk).update(
            #     name=request.POST['name'],
            #     description=request.POST['description'],
            #     duration=parse_duration(request.POST['duration'])
            # )
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


# def exercise_create(request):
#     form = ExerciseForm()
#     if request.method == 'GET':
#         content = {'form': form}
#         return render(request, '_exercise-create.html', content)
#     # elif request.method == 'POST':
#     #     form = ExerciseForm(request.POST, request.FILES)
#     #     if form.is_valid():
#     #         form.save()
#     #         return redirect('exercise')
#     #     else:
#     #         content = {"form": form}
#     #         return render(request, '_exercise-create.html', content)

#     elif request.method == "POST":
#         # get the form data
#         form = ExerciseForm(request.POST, request.FILES)
#         # save the data and after fetch the object in instance
#         if form.is_valid():
#             instance = form.save()
#             # serialize in new friend object in json
#             ser_instance = serializers.serialize('json', [ instance, ])
#             # send to client side.
#             return JsonResponse({"instance": ser_instance}, status=200)
#         else:
#             # some form errors occured.
#             return JsonResponse({"error": form.errors}, status=500)


def sorry(request):
    return render(request, 'sorry.html')

from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Ai1, Ai2
from .serializers import Ai1Serial, Ai2Serial
from .forms import AiForm, AiForms, Ai2Form, AiForms2


class WSLoginView(LoginView):
    template_name = 'login.html'


@login_required
def graph(request):
    return render(request, 'graph.html')


@login_required
def add_ai(request):
    if request.user.pk == 1:
        if request.method == 'POST':
            form = AiForm(request.POST, request.FILES)
            form.save()
            return redirect('graph')
        else:
            context = {'addForm': AiForm(initial={'user': request.user.pk})}
            return render(request, 'add.html', context)
    elif request.user.pk == 2:
        if request.method == 'POST':
            form = Ai2Form(request.POST, request.FILES)
            form.save()
            return redirect('graph')
        else:
            context = {'addForm': Ai2Form(initial={'user': request.user.pk})}
            return render(request, 'add.html', context)


@login_required
def edit_ai(request):
    if request.user.pk == 1:
        if request.method == 'POST':
            form = AiForms(request.POST)
            form.save()
            return redirect('graph')
        else:
            context = {'addForm': AiForms()}
            return render(request, 'edit.html', context)
    elif request.user.pk == 2:
        if request.method == 'POST':
            form = AiForms2(request.POST)
            form.save()
            return redirect('graph')
        else:
            context = {'addForm': AiForms2()}
            return render(request, 'edit.html', context)


@api_view(['GET'])
def api_ai(request):
    if request.user.pk == 1:
        if request.method == 'GET':
            data = Ai1.objects.filter(user=request.user.pk)
            serial = Ai1Serial(data, many=True)
            return Response(serial.data)
    elif request.user.pk == 2:
        if request.method == 'GET':
            data = Ai2.objects.filter(user=request.user.pk)
            serial = Ai2Serial(data, many=True)
            return Response(serial.data)

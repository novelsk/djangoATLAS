from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Ai1, Ai2
from .serializers import Ai1Serial, Ai2Serial


class WSLoginView(LoginView):
    template_name = 'login.html'


@login_required
def graph(request):
    return render(request, 'graph.html')


@api_view(['GET'])
def api_ai(request):
    if request.method == 'GET':
        if request.user.pk == 1:
            data = Ai1.objects.all()
            serial = Ai1Serial(data, many=True)
            return Response(serial.data)
        elif request.user.pk == 2:
            data = Ai2.objects.all()
            serial = Ai2Serial(data, many=True)
            return Response(serial.data)

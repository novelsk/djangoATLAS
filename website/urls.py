from django.urls import path, include
from .views import WSLoginView, graph, api_ai

urlpatterns = [
    path('api/ai/', api_ai),
    path('graph/', graph, name='graph'),
    path('', WSLoginView.as_view(), name='login'),
]

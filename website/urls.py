from django.urls import path
from .views import WSLoginView, graph, api_ai, add_ai, edit_ai

urlpatterns = [
    path('api/', api_ai),
    path('edit/', edit_ai, name='edit'),
    path('add/', add_ai, name='add'),
    path('graph/', graph, name='graph'),
    path('', WSLoginView.as_view(), name='login'),
]

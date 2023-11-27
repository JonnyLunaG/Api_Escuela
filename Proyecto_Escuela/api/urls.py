from django.urls import path
from .views import EscuelaView

urlpatterns = [
    path('escuelas/', EscuelaView.as_view(), name='escuelas_list'),
    path('escuelas/<int:id>', EscuelaView.as_view(), name='escuelas_procesos')  
]
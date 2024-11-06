
from django.urls import path
from . import views


# localhost:8000 / chai/ xyz

urlpatterns = [
    
    path('',views.all_test , name='all_test'),
    #path('xyz/', views.xyz , name = 'all_xyz')
]
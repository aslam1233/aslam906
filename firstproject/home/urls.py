from django.urls import path

from home import views
from home.views import delete

app_name = 'home'

urlpatterns = [
    path('', views.myfun),
    path('2/', views.fun1),
    path('3/', views.fun2),
    path('register/', views.fun3, name='fun3'),
    path('display/', views.display, name='display'),
    path('delete/,<int:id>', views.delete, name='delete'),
    path('insert/', views.insert, name='insert'),
    path('edit/,<int:id>', views.edit, name='edit'),

]

from django.urls import path

from welcome import views
from welcome.views import fun2

app_name = 'welcome'
urlpatterns = [
    path('1/', views.fun),
    path('2/', views.fun1),
    path('3/', views.fun2, name='fun2'),
    path('display/', views.display, name='display'),
    path('delete/,<int:id>', views.delete, name='delete')
]

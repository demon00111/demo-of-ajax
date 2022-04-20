
from . import views
from django.urls import path

urlpatterns = [
    path('',views.home, name='home'),
    path('save/',views.save_data, name='save'),
    path('show/',views.show_data, name='show'),
    path('all/',views.all_data, name='all'),

]

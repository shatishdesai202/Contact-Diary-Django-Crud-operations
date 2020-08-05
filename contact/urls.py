from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('del/<int:id>', views.delete, name="delete"),
    path('upd/<int:id>', views.update, name="update"),
    path('search', views.search, name="search"),
]

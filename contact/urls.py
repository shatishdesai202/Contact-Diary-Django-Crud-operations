from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('del/<int:id>', views.delete, name="delete"),
    path('upd/<int:id>', views.index, name="update"),
    path('search/', views.search, name="search"),
    path('signup/', views.sign_up, name="signup"),
    path('login/', views.login_, name="login"),
    path('logout/', views.log_out, name="logout"),

]

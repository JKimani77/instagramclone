from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from clone import views 

urlpatterns = [
    path('', views.home, name='home'),
    #
    #
    #
    #
    #
    #
    path('logout/', views.logout_view, name='logout'),
]
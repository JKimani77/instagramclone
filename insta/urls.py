from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from insta import views 

urlpatterns = [
    path('', views.index, name='home'),
    path('profile/', views.profile, name='create-profile'),
    path('profile/<slug:username>/', views.updatedprofile, name='dipslay-profile'),
    path('post/image/', views.uploadimage, name = 'uploadimage'),
    path('search/', views.search, name='searchbyusername'),
    path('image/(?P<img_id>\d+)/', views.specific, name='single-image'),
    path('comment/(?P<id>\d+)/', views.comment, name='comment'),
    path('logout/', views.logout_view, name='logout'),
]
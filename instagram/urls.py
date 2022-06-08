from django.urls import path,include
from . import views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('newpost/', views.NewPost, name='newpost'),
    path('<uuid:post_id>', views.PostDetails, name='postdetails'),
    path('<uuid:post_id>/like',views.like,  name='postlike')
    
] 
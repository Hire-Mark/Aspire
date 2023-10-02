from django.urls import path
from .import  views 

x = 0
if x == 1:
    IndexPagePath = path('', views.PostList.as_view(), name='index')
else:
    IndexPagePath = path('',views.index, name='index')           

urlpatterns = [
    path('category/<slug:slug>/<int:pk>',views.PostCategoryList, name='category'),
    #path('about/',views.about, name='about'),
    #path('', views.PostList.as_view(), name='posts'),
    IndexPagePath,
    path('search/', views.search, name = 'search'),
    path('about/', views.about, name='about'),
    path('articles/', views.PostList.as_view(), name='articles'),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    # path('<slug:slug>/<int:pk>', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/<int:pk>', views.postdetail, name='post_detail'),
    
    
]
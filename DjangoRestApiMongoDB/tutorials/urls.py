from django.urls import path, include
from tutorials import views 
 
urlpatterns = [ 
    path('api/tutorials/<int:pk>', views.tutorial_detail),
    path('api/tutorials/', views.tutorial_list),
    path('api/tutorials/published', views.tutorial_list_published),

    # paths for Teacher API

    #path('api/teachers/<int:pk>', views.teacher_detail),
    path('api/teachers', views.teacher_list)
]

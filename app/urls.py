from django.urls import path
from app import views
app_name='movie'

# urlpatterns = [
#     path('', views.index.as_view(), name='index'),
#     path('movie/<int:p>/', views.detail.as_view(), name='detail'),
#     path('delete/<int:p>/', views.delete.as_view(), name='delete'),
#     path('update/<int:p>',views.update,name="update"),

# ]

urlpatterns = [
    path('',views.movieListview.as_view(),name="index"),
    path('movie/<int:pk>/', views.MovieDetailView.as_view(), name='moviedetail'),
    path('movie/<int:pk>/delete/', views.MovieDeleteView.as_view(), name='moviedelete'),

]
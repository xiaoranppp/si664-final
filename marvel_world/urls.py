from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('characters/', views.CharacterListView.as_view(), name='characters'),
    path('chracters/<int:pk>/', views.CharacterDetailView.as_view(), name='character_information'),
    path('comics/', views.ComicListView.as_view(), name='comics'),
    path('comics/<int:pk>/', views.ComicDetailView.as_view(), name='comic_information'),
]
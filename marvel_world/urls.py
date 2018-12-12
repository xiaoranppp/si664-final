from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('characters/', views.CharacterListView.as_view(), name='characters'),
    path('characters/<int:pk>/', views.CharacterDetailView.as_view(), name='character_information'),
    path('comics/', views.ComicListView.as_view(), name='comics'),
    path('comics/<int:pk>/', views.ComicDetailView.as_view(), name='comic_information'),
    path('powers/', views.PowerListView.as_view(), name='super_power'),
    path('powers/<int:pk>/', views.PowerDetailView.as_view(), name='super_power_information'),
    path('character/filter/',views.CharacterFilterView.as_view(),name='character_filter'),
    path('comic/filter/',views.ComicFilterView.as_view(),name='comic_filter'),
    path('characters/new/', views.CharacterCreateView.as_view(), name='character_new'),
    path('characters/<int:pk>/delete/', views.CharacterDeleteView.as_view(), name='character_delete'),
    path('characters/<int:pk>/update/', views.CharacterUpdateView.as_view(), name='character_update'),
    path('powers/new/', views.PowerCreateView.as_view(), name='power_new'),
    path('powers/<int:pk>/delete/', views.PowerDeleteView.as_view(), name='power_delete'),
    path('powers/<int:pk>/update/', views.PowerUpdateView.as_view(), name='power_update'),
    

   # path('logoutpage/', views.LogoutPageView.as_view(), name='logoutpage'),
]
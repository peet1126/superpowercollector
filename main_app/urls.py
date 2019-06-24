from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('powers/', views.powers_index, name='index'),
    path('powers/<int:power_id>/', views.powers_details, name='details'),
    path('powers/<int:power_id>/add_practice/', views.add_practice, name='add_practice'),
    path('powers/<int:power_id>/assoc_suit/<int:suit_id>/', views.assoc_suit, name='assoc_suit'),
    path('powers/<int:power_id>/add_photo/', views.add_photo, name='add_photo'),
    path('powers/create/', views.PowersCreate.as_view(), name='powers_create'),
    path('powers/<int:pk>/update/', views.PowersUpdate.as_view(), name='powers_update'),
    path('powers/<int:pk>/delete/', views.PowersDelete.as_view(), name='powers_delete'),
    path('suits/', views.SuitList.as_view(), name='suits_index'),
    path('suits/<int:pk>/', views.SuitDetail.as_view(), name='suits_details'),
    path('suits/create/', views.SuitCreate.as_view(), name='suits_create'),
    path('suits/<int:pk>/', views.SuitUpdate.as_view(), name='suits_update'),
    path('suits/<int:pk>/', views.SuitDelete.as_view(), name='suits_delete'),
]
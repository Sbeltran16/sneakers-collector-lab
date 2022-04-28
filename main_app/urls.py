from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('about/', views.about, name='about'),
	path('sneakers/', views.sneakers_index, name='index'),
    path('sneakers/<int:sneaker_id>/', views.sneakers_detail, name='detail'),
    path('sneakers/create/', views.SneakerCreate.as_view(), name='sneakers_create'),
    path('sneakers/<int:pk>/update/', views.SneakerUpdate.as_view(), name='sneakers_update'),
    path('sneakers/<int:pk>/delete/', views.SneakerDelete.as_view(), name='sneakers_delete'),
    path('sneakers/<int:sneaker_id>/add_buyer/', views.add_buyer, name='add_buyer'),
    path('sneakers/<int:sneaker_id>/assoc_lace/<int:lace_id>/', views.assoc_lace, name='assoc_lace'),
    path('laces/', views.LaceList.as_view(), name='laces_index'),
    path('laces/<int:pk>/', views.LaceDetail.as_view(), name='laces_detail'),
    path('laces/create/', views.LaceCreate.as_view(), name='laces_create'),
    path('laces/<int:pk>/delete/', views.LaceDelete.as_view(), name='laces_delete'),
]
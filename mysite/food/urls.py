from django.urls import path
from . import views

app_name = 'food'
urlpatterns = [
    # /food/
    path('',views.IndexClassView.as_view(),name='index'),
    # /food/item
    path('item/',views.item,name='item'),
    # /food/1
    path('<int:pk>/', views.FoodDetail.as_view(),name='detail'),
    # add items
    path('add/', views.CreateItem.as_view(), name='create_item'),
    # delete item
    path('delete/<int:id>', views.delete_item, name='delete_item'),
    # edit item
    path('edit/<int:id>/', views.edit_item, name='edit_item'),
]

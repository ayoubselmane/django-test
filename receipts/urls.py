from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('edit/<int:id>', views.edit_receipt, name='edit'),
    path('create_receipt', views.create_receipt, name='edit'),
    path('delete/<int:id>', views.delete_receipt, name='delete'),
    path('details/<int:id>', views.details, name='details'),

]

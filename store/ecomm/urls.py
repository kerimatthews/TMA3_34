from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from ecomm.views import CartListView


urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('ecomm/', views.ecomm, name='ecomm'),
    path('computers/', views.computers, name="computers"),
    path('laptops/', views.laptops, name="laptops"),
    path('desktops/', views.desktops, name="desktops"),
#    path('computer_list/', views.computer_list),
#    path('computers/', views.ComputerListView.as_view(), name="computers"),
#   path('computers/<int:pk>', views.ComputerDetailView.as_view(), name="computer-detail"),
]
urlpatterns += staticfiles_urlpatterns()

# importing views from views..py
#https://www.geeksforgeeks.org/detailview-class-based-views-django/?ref=gcse
from .views import ComputerDetailView
urlpatterns += [
    # <pk> is identification for id field,
   # path('delete/<item_id>', views.delete, name="delete"),
  #  path('details/', views.details, name='details'),
    path('computers/<pk>/', ComputerDetailView.as_view()),
    path('cart/list', CartListView.as_view(), name="cart_list"),
]
from django.urls import path
from .views import Add_Pizza_order, CurrentOrderStatusView

urlpatterns = [
    # Path for placing orders
    path('placeorders/', Add_Pizza_order.as_view(), name='place_order'),
    # Path for tracking orders
    path('trackorders/', CurrentOrderStatusView.as_view(), name='track_order'),
]

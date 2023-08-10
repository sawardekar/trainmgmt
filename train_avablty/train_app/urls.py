from django.urls import path, include
from django.conf.urls import url
from . import views
from . import api
from . import train_api


urlpatterns = [
    path('', views.index, name='index'),
    path('train', api.TrainView.as_view()),
    path('train/(?P<pk>[0-9]+)$', api.TrainView.as_view()),
    path('comp', api.CompartmentView.as_view()),
    path('comp/(?P<pk>[0-9]+)$', api.CompartmentView.as_view()),
    path('seat', api.SeatAvabiltyView.as_view()),
    path('seat/(?P<pk>[0-9]+)$', api.SeatAvabiltyView.as_view()),
    path('check_seat',train_api.check_seat,name="check_seat"),
    path('available_seat',train_api.available_seat,name="available_seat"),
    path('update_seats',train_api.update_seats,name="update_seats"),
    path('book_seats',train_api.book_seats,name="book_seats"),
]
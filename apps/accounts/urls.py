from django.urls import path

from .views import UserView

urlpatterns = [
    path('signup/', UserView.as_view(), name='user-signup'),
    path('signin/', UserView.as_view(), name='user-signin'),
]

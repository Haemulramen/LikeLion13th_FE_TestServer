from django.urls import path
from accounts.views import *

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='signup'),
    # path('login/', ),
    # path('mypage/'),
    # path('refresh/')
]
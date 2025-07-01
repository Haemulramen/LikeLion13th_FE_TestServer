from django.urls import path
from accounts.views import *

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='signup'),
    path('login/', AuthView.as_view(), name='login'),
    path('mypage/', MyPageView.as_view(), name='mypage'),
    # path('refresh/')
]
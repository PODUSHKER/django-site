from django.urls import path
from users.views import *

app_name = 'users'

urlpatterns = [
        path('login/', LoginUserView.as_view(), name='login'),
        path('logout/', logout, name='logout'),
        path('register/', RegisterView.as_view(), name='register'),
        path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
        path('verify_mail/<str:email>/<uuid:code>', verify_email, name='verify_email')
]


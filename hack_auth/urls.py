from django.urls import path
from .views import RegisterView, LoginAPIView
#from .views import VerifyEmailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login')
    #path('email-verify/', VerifyEmailView.as_view(), name='email-verify'),   
]
from django.urls import path
from authentication import views as vd
from authentication.views import Login

urlpatterns = [
    path('login/',Login.as_view(), name="login"),
    path('register/',vd.register, name="register"),
]

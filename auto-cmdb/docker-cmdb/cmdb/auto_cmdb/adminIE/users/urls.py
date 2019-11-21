from django.urls import path, register_converter,re_path,include
from . import views
from django.views.generic import TemplateView




app_name="users"
urlpatterns = [
    path('login/',views.UserLoginView.as_view(),name="login"),
    path('logout/', views.UserLogoutView.as_view(), name="logout"),
    path('regist/',views.UserRegisterView.as_view(),name="regist"),
    path('api-auth/', include('rest_framework.urls')),
]


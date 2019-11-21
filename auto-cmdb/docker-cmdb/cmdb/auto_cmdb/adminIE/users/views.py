from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse, reverse_lazy
from users.users_forms import UserRegisterFormView
from django.views import View
from users.models import UsersProfile
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q


# Create your views here.

class UserLoginView(LoginView):
    # 指定一个用于接收到 GET 请求时，需要返回的模板文件
    template_name = "login.html"


class UserLogoutView(LogoutView):
    # 用户退出登录后，将要跳转的 URL
    next_page = reverse_lazy("users:login")



class UserRegisterView(FormView):
    template_name = "register.html"
    form_class = UserRegisterFormView
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = UsersProfile(**form.cleaned_data)
        user.set_password(form.cleaned_data["password"])
        user.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        # 数据无效返回原来的模板，并且携带原来提交的数据
        return super().form_invalid(form)


User = get_user_model()


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(
                Q(username=username) | Q(email=username) | Q(mobile=username)
            )
            if user.check_password(password):
                return user
        except Exception:
            return None


from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView
from . import views

app_name="octopus"
urlpatterns = [
    path('connection/',views.ConnectionView.as_view(),name="connection"),
    path('async/',views.AsyncDemoView.as_view(),name="asyncDemo"),
    path('get_task/',views.TaskResultView.as_view(),name="getTask" ),
    path('run/',views.RunView.as_view(),name="run"),
    path('get_return/',views.ExecCommandMakeView.as_view(),name="getreturn" ),
    path('task_result/',views.ExecCommandView.as_view(),name="taskResult")
]
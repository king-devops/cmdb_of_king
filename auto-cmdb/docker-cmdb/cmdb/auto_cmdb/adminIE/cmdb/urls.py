from django.urls import path, register_converter,re_path,include
from . import views
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('assets', views.AssetViewSet)
router.register('idc', views.IDCViewSet)
router.register('cabinet', views.CabinetViewSet)
router.register('sysusers', views.SysUsersViewSet)
router.register('server', views.ServerViewSet)
router.register('memory', views.MemoryViewSet)
router.register('disk', views.DiskViewSet)
router.register('treenode', views.TreeNodeViewSet)
router.register('detail/<int:num>', views.AssetDetailViewSet)




app_name="cmdb"
urlpatterns = [
    path('', include(router.urls)),
    path('assets-list/',TemplateView.as_view(template_name='cmdb/asset-list.html'),name='assets'),
    path('idc-list/',TemplateView.as_view(template_name='cmdb/idc.html'),name='idc'),
    path('cabinet-list/',TemplateView.as_view(template_name='cmdb/cabinet.html'),name='cabinet'),
    path('sysusers-list/',TemplateView.as_view(template_name='cmdb/sysusers.html'),name='sysusers'),
    path('server-list/',TemplateView.as_view(template_name='cmdb/server.html'),name='server'),
    path('meminfo-list/',TemplateView.as_view(template_name='cmdb/meminfo.html'),name='meminfo'),
    path('diskinfo-list/',TemplateView.as_view(template_name='cmdb/diskinfo.html'),name='diskinfo'),
    path('tree-node/',TemplateView.as_view(template_name='cmdb/tree-node.html'),name='treenode'),
    path('assets-detail/<int:num>',TemplateView.as_view(template_name='cmdb/detail.html'),name='assets-detail'),
]
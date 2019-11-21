from django.shortcuts import render

from django.views.generic import ListView,DetailView
from .page import StandardResultsSetPagination
from rest_framework import viewsets
from .models import Asset,IDC,Cabinet,Server,Memory,Disk,SysUsers,TreeNode
from .serializers import (AssetSerializer,IDCSerializer,ServerSerializer,
                                    SysUsersSerializer,MemorySerializer,
                                    DiskSerializer,CabinetSerializer,TreeNodeSerializer)
from rest_framework import mixins
# Create your views here.


class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    pagination_class = StandardResultsSetPagination


class IDCViewSet(viewsets.ModelViewSet):
    queryset = IDC.objects.all()
    serializer_class = IDCSerializer
    pagination_class = StandardResultsSetPagination


class CabinetViewSet(viewsets.ModelViewSet):
    queryset = Cabinet.objects.all()
    serializer_class = CabinetSerializer
    pagination_class = StandardResultsSetPagination


class SysUsersViewSet(viewsets.ModelViewSet):
    queryset = SysUsers.objects.all()
    serializer_class = SysUsersSerializer
    pagination_class = StandardResultsSetPagination


class ServerViewSet(viewsets.ModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    pagination_class = StandardResultsSetPagination
 

class MemoryViewSet(viewsets.ModelViewSet):
    queryset = Memory.objects.all()
    serializer_class = MemorySerializer
    pagination_class = StandardResultsSetPagination


class DiskViewSet(viewsets.ModelViewSet):
    queryset = Disk.objects.all()
    serializer_class = DiskSerializer
    pagination_class = StandardResultsSetPagination


class TreeNodeViewSet(viewsets.ModelViewSet):
    queryset = TreeNode.objects.filter(node_upstream=None)
    serializer_class = TreeNodeSerializer

class AssetDetailViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.filter(id=num)
    serializer_class = AssetSerializer
     

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import mixins
# from rest_framework import generics
# from rest_framework import filters
# from rest_framework.pagination import PageNumberPagination
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework import viewsets
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.throttling import UserRateThrottle

# from rest_framework_extensions.cache.mixins import CacheResponseMixin

# from .models import Goods, GoodsCategory, HotSearchWords, Banner
# from .filters import GoodsFilter
# from .serializers import GoodsSerializer, CategorySerializer, HotWordsSerializer, BannerSerializer
# from .serializers import IndexCategorySerializer
# # Create your views here.


# class GoodsPagination(PageNumberPagination):
#     page_size = 12
#     page_size_query_param = 'page_size'
#     page_query_param = "page"
#     max_page_size = 100


# class GoodsListViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
#     """
#     商品列表页, 分页， 搜索， 过滤， 排序
#     """
#     # throttle_classes = (UserRateThrottle, )
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
#     pagination_class = GoodsPagination
#     # authentication_classes = (TokenAuthentication, )
#     filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
#     filter_class = GoodsFilter
#     search_fields = ('name', 'goods_brief', 'goods_desc')
#     ordering_fields = ('sold_num', 'shop_price')

#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.click_num += 1
#         instance.save()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)

# class CategoryViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
#     """
#     list:
#         商品分类列表数据
#     retrieve:
#         获取商品分类详情
#     """
#     queryset = GoodsCategory.objects.filter(category_type=1)
#     serializer_class = CategorySerializer


# class HotSearchsViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
#     """
#     获取热搜词列表
#     """
#     queryset = HotSearchWords.objects.all().order_by("-index")
#     serializer_class = HotWordsSerializer


# class BannerViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
#     """
#     获取轮播图列表
#     """
#     queryset = Banner.objects.all().order_by("index")
#     serializer_class = BannerSerializer


# class IndexCategoryViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
#     """
#     首页商品分类数据
#     """
#     queryset = GoodsCategory.objects.filter(is_tab=True, name__in=["生鲜食品", "酒水饮料"])
#     serializer_class = IndexCategorySerializer
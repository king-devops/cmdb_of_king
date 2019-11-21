from django.shortcuts import render, HttpResponse
from django.views import View
from cmdb.models import Asset
from django.http import JsonResponse
from django.db.models import Count


class assetpie(View):
    def get(self,request):
        li = [
            ['状态', '在线', '上架', '离线','下架'],
            ['服务器', 4,6,2,5],
            ['路由器', 2,10,1,3],
            ['交换机', 3,4,5,1],
            ['容器', 20,50,7,0]
        ]
        # Asset.objects.filter(device_type_id=1).count(device_status_id=2)
        #当传值为字典时，safe为true
        return JsonResponse(li, safe=False)                                      
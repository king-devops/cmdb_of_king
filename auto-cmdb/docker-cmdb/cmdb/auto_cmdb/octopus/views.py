import subprocess,ansible,pexpect


from django.http import JsonResponse,HttpResponse
from django.shortcuts import render
from django.views.generic import View


from cmdb.models import Server,Inventorypool
from .utils.handle_command import HandleCommand




            




class ConnectionView(View):
    def get(self,request):
        conninfo = Server.objects.filter(connection__user__isnull=False)
        return render(request,"octopus/connection.html",{"connection": conninfo})

    def post(self,requset):
        server_id = requset.POST.get("server_id")
        server = Server.objects.filter(id=server_id).first()
        user = server.connection.user
        port = server.connection.port
        pwd = server.connection.password
        ip = server.manager_ip
        #shell
        # status,_ = subprocess.getstatusoutput("sh /root/copyssh.sh {} {} {} {}".format(port,user,ip,pwd))
        # if status == 0 :
        #     server.connection.authed = True
        #     server.connection.save()
        #     return JsonResponse({"status":True})
        # else :
        #     return JsonResponse({"status":False})

        #python
        shell_comm = "ssh-copy-id -p {} {}@{}".format(port,user,ip)
        
        child = pexpect.spawn(shell_comm)

        index = child.expect(["yes/no","password",pexpect.exceptions.EOF, pexpect.TIMEOUT],timeout=10)
        
        
        try:
            print ("开始向%s上传公钥"%(server))
            child.sendline("yes")
            child.expect("password")
            child.sendline(pwd)
           
            print ("已向%s上传公钥"%(server))
            server.connection.authed = True
            server.connection.save()
            return JsonResponse({"status": True})
        except Exception as e:
            print(e)
            return JsonResponse({"status": False}) 


class RunView(View):
      def get(self,request):           
            inventory_info = Inventorypool.objects.all()
            return render(request,"octopus/run.html",{"inventorys": inventory_info})
      def post(self,request):
            command = request.POST.get("command")
            # inventory_info = Inventorypool.objects.all()
            handler = HandleCommand(command)
            ret = handler.exec_command()
            return JsonResponse(
            {
                # "inventorys": inventory_info,
                "result":ret
                })

class ExecCommandView(View):
    def get(self, request):
        inventorys = Inventorypool.objects.all()
        return render(request, "octopus/run.html", {
            "inventorys": inventorys
        })

    def post(self, request):
        inventorys = Inventorypool.objects.all()
        command = request.POST.get('command')
        from .tasks import test_ansible
        task = test_ansible.delay(command)   #传入异步命令
        return JsonResponse({"task_id": task.id})

###demo
class AsyncDemoView(View):
      def get(self,request):
            return render(request,'octopus/async_demo.html')
      def post(self,request):
            num = request.POST.get('num')
            from .tasks import add
            task = add.delay(int(num))
            print("命令到了。。。。")
            return JsonResponse({"task_id":task.id})

from celery.result import AsyncResult
class TaskResultView(View):
    def get(self, request):
        task_id = self.request.GET.get("task_id")
        # print(task_id)
        task_obj = AsyncResult(id=task_id)
        task_json = {
            "id": task_obj.id,
            "status": task_obj.status,
            "success": task_obj.successful(),
            "result": task_obj.result
        }
        return JsonResponse(task_json)

class ExecCommandMakeView(View):
    def get(self, request):
        task_id = self.request.GET.get("task_id")
        task_obj = AsyncResult(id=task_id)
        task_json = {
            "id": task_obj.id,
            "status": task_obj.status,
            "success": task_obj.successful(),
            "result": task_obj.result
        }
        return JsonResponse(task_json)
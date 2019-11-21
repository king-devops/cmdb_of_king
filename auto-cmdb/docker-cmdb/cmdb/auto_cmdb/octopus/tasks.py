# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task

from cmdb.models import Inventorypool
from .utils.handle_command import HandleCommand

@shared_task
def test_ansible(command):
        inventorys = Inventorypool.objects.all()
        handler = HandleCommand(command)
        ret = handler.exec_command()
        print("任务执行中")
        return ret

@shared_task
def add(n):
          import time
          time.sleep(2)
          return n + 10
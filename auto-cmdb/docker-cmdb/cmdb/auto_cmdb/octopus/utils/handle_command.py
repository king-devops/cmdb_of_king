import subprocess
from auto_cmdb.settings import INVENT_PATH as invent_path


class HandleCommand:
    ret_msg = {
        "status": False,
        "msg": '命令格式错误'
    }
    def __init__(self, command):
        self.command = command
        self.invent_path = invent_path
        self.command_tpl = '{} -i {} -{}'

    def checked(self):
        """检查命令格式"""
        ansib, arg = self.command.split('-', 1)
        self.command = self.command_tpl.format(ansib,self.invent_path, arg)
        return self.command

    def exec_command(self):
        comm = self.checked()
        if comm:
            status, r = subprocess.getstatusoutput(comm)
            if status == 0:
                self.ret_msg['status'] = True
            self.ret_msg['msg'] = r
        return self.ret_msg

                  
from django.contrib import admin

from .models import Asset, Server, Memory, Disk,SysUsers,Tag,TreeNode,Connection,Inventorypool,Variable2Server,Variable2Group
class AssetAdmin(admin.ModelAdmin):
      pass
class ServerAdmin(admin.ModelAdmin):
      pass
class MemoryAdmin(admin.ModelAdmin):
      pass

class DiskAdmin(admin.ModelAdmin):
      pass
class SysUsersAdmin(admin.ModelAdmin):
      pass

class TreeNodeAdmin(admin.ModelAdmin):
      pass

class TagAdmin(admin.ModelAdmin):
      pass

class ConnectionAdmin(admin.ModelAdmin):
      pass

class InventorypoolAdmin(admin.ModelAdmin):
      pass

class Variable2GroupAdmin(admin.ModelAdmin):
      pass

class Variable2ServerAdmin(admin.ModelAdmin):
      pass



admin.site.register(Asset,AssetAdmin)
admin.site.register(Server,ServerAdmin)
admin.site.register(Memory,MemoryAdmin)
admin.site.register(Disk,DiskAdmin)
admin.site.register(SysUsers,SysUsersAdmin)
admin.site.register(TreeNode,TreeNodeAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Connection,ConnectionAdmin)
admin.site.register(Inventorypool,InventorypoolAdmin)
admin.site.register(Variable2Group,Variable2GroupAdmin)
admin.site.register(Variable2Server,Variable2ServerAdmin)



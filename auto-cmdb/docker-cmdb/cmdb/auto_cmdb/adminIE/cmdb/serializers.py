from rest_framework import serializers
from .models import Asset,IDC,Cabinet,Server,SysUsers,Disk,Memory,TreeNode


class MemorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Memory
        fields = "__all__"


class DiskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Disk
        fields = "__all__"


class ServerSerializers(serializers.ModelSerializer):
    disk = DiskSerializers(many=True)
    memory = MemorySerializers(many=True)
    class Meta:
        model = Server
        fields = "__all__"
    
    def create(self,validated_data):
        return Disk.objects.create(**validated_data)

    def create(self,validated_data):
        return Memory.objects.create(**validated_data)


class AssetSerializer(serializers.ModelSerializer):
    device_type = serializers.SerializerMethodField()
    device_status = serializers.SerializerMethodField()
    server = ServerSerializers()
    class Meta:
        model = Asset
        fields = "__all__"

    def get_device_type(self,obj):
        return obj.get_device_type_id_display()

    def get_device_status(self,obj):
        return obj.get_device_status_id_display()

    def create(self,validated_data):
        return Server.objects.create(**validated_data)


class IDCSerializer(serializers.ModelSerializer):
    class Meta:
        model = IDC
        fields = "__all__"


class CabinetSerializer(serializers.ModelSerializer):
    idc = IDCSerializer()
    class Meta:
        model = Cabinet
        fields = "__all__"

    def create(self, validated_data):    
            return Cabinet.objects.create(**validated_data)

    

class SysUsersSerializer(serializers.ModelSerializer):
    user_type_id = serializers.SerializerMethodField()
    class Meta:
        model = SysUsers
        fields = "__all__"
    
    def get_user_type_id(self,obj):
        return obj.get_user_type_display()


class ServerSerializer(serializers.ModelSerializer):
    asset = AssetSerializer()
    # sysusers = SysUsersSerializer()
    class Meta:
        model = Server
        fields = "__all__"

    def create(self,validated_data):
        return Server.objects.create(**validated_data)




class MemorySerializer(serializers.ModelSerializer):
    server = ServerSerializer()
    class Meta:
        model = Memory
        fields = "__all__"

    def create(self,validated_data):
        return Server.objects.create(**validated_data)


class DiskSerializer(serializers.ModelSerializer):
    server = ServerSerializer()
    class Meta:
        model = Disk
        fields = "__all__"

    def create(self,validated_data):
        return Server.objects.create(**validated_data)


class SubsubTreeNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreeNode
        fields = "__all__"


class SubTreeNodeSerializer(serializers.ModelSerializer):
    sub_node = SubsubTreeNodeSerializer(many=True)
    class Meta:
        model = TreeNode
        fields = "__all__"


class TreeNodeSerializer(serializers.ModelSerializer):
    sub_node = SubTreeNodeSerializer(many=True)
    class Meta:
        model = TreeNode
        fields = "__all__"



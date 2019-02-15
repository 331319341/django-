from rest_framework import serializers
from APP01 import models
# class 出版社序列化(serializers.Serializer):
#     id= serializers.IntegerField(read_only=True)
#     名称=serializers.CharField(max_length=32)
#     地址=serializers.CharField(max_length=32)
#
#     def create(self, validated_data):
#         return  models.出版社.objects.create(**validated_data)
#     def update(self, instance, validated_data):
#         instance.名称=validated_data("名称",instance)
#         instance.地址=validated_data("地址",instance)
#         instance.save()
#         return instance

# from APP01 import models
# from APP01 import models ,序列化
# p1=models.出版社.objects.first()
# s =序列化.出版社序列化(p1)
# s.data
# p2={'名称': '22', '地址': '222'}
# s = 序列化.出版社序列化(data=p2)
# s.is_valid()
# s.validated_data
# s.save()

class 出版社序列化(serializers.ModelSerializer):
    class Meta:
        model=models.出版社
        fields = ('id', '名称', '地址')

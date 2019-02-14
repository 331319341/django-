from django.shortcuts import render

from APP01 import  models
from django.http import HttpResponse
def 出版社列表(requset):
    结果=models.出版社.objects.all()
    # 方法1
    # data=[]
    # for i in 结果:
    #     p_tpm={
    #          "名称":i.名称,
    #          "地址": i.地址 }
    #     data.append(p_tpm)

    #方法2
    # data=[]
    # from django.forms.models import model_to_dict
    # for i in 结果:
    #     data.append(model_to_dict(i))

    # 方法3
    from django.core import serializers
    data=serializers.serialize("json",结果)

    import json
    return HttpResponse(json.dumps(data),content_type='application/json')

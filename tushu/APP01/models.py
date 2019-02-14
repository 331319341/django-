from django.db import models

class 出版社(models.Model):
    名称=models.CharField(max_length=32,verbose_name="名称",unique=True)
    地址=models.CharField(max_length=32,verbose_name="地址")
    def __str__(self):
        return self.名称
    class Meta:
        verbose_name="出版社"
        verbose_name_plural=verbose_name


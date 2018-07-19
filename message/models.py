# _*_ coding:utf-8 _*_

from django.db import models

# Create your models here.


#透過models 直接生成資料表  設定null = true   blank = true 這兩個設定為true 代表字段可以為空   default 默認直 如果沒給name付值的話 會自己給她一個值
#不給主ＫＥＹ的話 會自動產生一個id當key
#改動 輸入makemigrations message  驗證是否有錯誤 如果沒有 migrate message 就會生成資料表or更新

class UserMessage(models.Model):

    object_id = models.CharField(max_length=50,default="",primary_key=True , verbose_name=u"主鍵ma")
    name = models.CharField(max_length=20, null=True,blank= True , default= "",verbose_name=u"用戶名") #char 類型 （指定最大長度,）
    email = models.EmailField(verbose_name=u"信箱")
    address = models.CharField(max_length=100,verbose_name=u"地址")
    message = models.CharField(max_length=500 , verbose_name=u"留言訊息")


    class Meta:
        verbose_name = u"用戶留言訊息"
        verbose_name_plural= verbose_name #指定訊息 如果沒有指定 後面會加上S  "用戶留言訊息S"
        # db_table = "user_message" #設定表明  如果需要自己設定名稱的話 生成前先輸入
        # ordering ="-object_id" #代表 orbey 排序 設定就直接會排序
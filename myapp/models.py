from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=256)
    user_id = models.IntegerField(default=0)
     #adminで表示されるテーブルの表記
    def __str__(self):
        return 'ID: ' + str(self.id) + ', 名前: ' + self.user_name

#Testモデル
class Test(models.Model):
    test_name = models.CharField(max_length=256)
    tesetr_id = models.IntegerField(default=0)
    def __str__(self):
        return 'ID: ' + str(self.id) + ', 名前: ' + self.test_name
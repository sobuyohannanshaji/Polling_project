from django.db import models


class Register(models.Model):
    name=models.CharField(max_length=100,default=True)
    phone=models.CharField(max_length=100,default=True)
    email=models.CharField(max_length=100,default=True)
    username = models.CharField(max_length=100,default=True)
    password = models.CharField(max_length=100,default=True)

    def __str__(self):
        return self.name

class Questions(models.Model):
    question=models.CharField(max_length=1000,default=True)
    name = models.ForeignKey(Register,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.question

class Vote(models.Model):
    op1 = models.CharField(max_length=1000)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, null=True,related_name='choices')
    like = models.IntegerField(default=0)

    def __str__(self):
        return self.op1

# class Like(models.Model):
#
#     op1=models.ForeignKey(Vote,on_delete=models.CASCADE,null=True)
#     question = models.ForeignKey(Questions, on_delete=models.CASCADE, null=True)
#
#     def __str__(self):
#         return self.like
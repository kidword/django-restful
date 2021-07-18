# -*- coding=utf-8 -*-
from django.db import models


class BookInfo(models.Model):
    btitle = models.CharField(max_length=20, verbose_name='名称')
    bpub_date = models.DateField(verbose_name='发布日期', null=True)
    bread = models.IntegerField(default=0, verbose_name='阅读量')
    bcomment = models.IntegerField(default=0, verbose_name='评论量')
    image = models.ImageField(upload_to='booktest', verbose_name='图片', null=True)

    def __str__(self):
        return self.btitle


class HeroInfo(models.Model):
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    hname = models.CharField(max_length=20, verbose_name="名称")
    hgender = models.IntegerField(choices=GENDER_CHOICES, verbose_name='性别', default=0)
    hcomment = models.CharField(max_length=200, blank=True, verbose_name="描述信息")
    hbook = models.ForeignKey(BookInfo, max_length=200, blank=True, on_delete=models.CASCADE)


class UserGroup(models.Model):
    user_type = models.CharField(max_length=32, verbose_name="用户类型")


class UserInfo(models.Model):
    user_type_choise = (
        (1, '普通用户'),
        (2, 'VIP'),
        (3, 'SVIP')
    )

    user_type = models.IntegerField(choices=user_type_choise)
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=64)
    group = models.ForeignKey('UserGroup', on_delete=models.CASCADE)
    roles = models.ManyToManyField('Role')


class UserToken(models.Model):
    user = models.OneToOneField(to="UserInfo", on_delete=models.CASCADE)
    token = models.CharField(max_length=64)


class Role(models.Model):
    title = models.CharField(max_length=32)

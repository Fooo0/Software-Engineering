# -*- coding: utf-8 -*-
from django.db import models

class Book(models.Model):
    ISBN = models.AutoField(primary_key=True)
    AuthorID = models.IntegerField(verbose_name = '作者ID')
    Title = models.CharField(max_length = 50, verbose_name = '书名')
    Publisher = models.CharField(max_length = 50, verbose_name = '出版商')
    PublishDate = models.DateField(blank = True, null = True, verbose_name = '出版日期')
    Price = models.FloatField(verbose_name = '价格')
    
    def __unicode__(self):
        return self.Title
        
class Author(models.Model):
    AuthorID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length = 50, verbose_name = '姓名')
    Age = models.IntegerField(blank = True, null = True, verbose_name = '年龄')
    Country = models.CharField(max_length = 50, verbose_name = '国别')
    
    def __unicode__(self):
        return self.Name
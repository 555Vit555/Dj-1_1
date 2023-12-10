# coding=utf-8

from django.db import models


class Book(models.Model):
    name = models.CharField(u'Название', max_length=64)
    author = models.CharField(u'Автор', max_length=64)
    pub_date = models.DateField(u'Дата публикации')

    def __str__(self):
        return self.name + " " + self.author

# class Phone(models.Model):
#     #id = models.CharField(u'id', max_length=64)
#     name = models.CharField(u'name', max_length=64)
#     price = models.CharField(u'price', max_length=64)
#     image = models.CharField(u'image', max_length=64)
#     release_date = models.CharField(u'release_date', max_length=64)
#     lte_exists = models.CharField(u'lte_exists', max_length=64)
#     slug = models.CharField(u'slug', max_length=64)


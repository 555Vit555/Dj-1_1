from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название раздела')

    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    tags = models.ManyToManyField(Tag, related_name='articles', through='Scope')




    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title
class Scope(models.Model):
    is_main = models.BooleanField(verbose_name='Основной')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='scopes')

    class Meta:
        ordering = ['-is_main', 'tag']
    def __str__(self):
        return 'Тэг'

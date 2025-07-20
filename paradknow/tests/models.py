from django.db import models
from ckeditor.fields import RichTextField

class Topic(models.Model):
    name = models.CharField(max_length=512, verbose_name="Название темы")

    def __str__(self):
        return self.name

class Question(models.Model):
    title = models.CharField(max_length=2000, verbose_name="Заголовок вопроса")
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='questions')
    answer = RichTextField(verbose_name="Ответ", blank=True, null=True)

    def __str__(self):
        return self.title
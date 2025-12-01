from django.db import models
class Bb(models.Model):
   title = models.CharField(max_length=50, verbose_name='Товар')
   content = models.TextField(verbose_name='Описание')
   rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')
   price = models.FloatField(verbose_name='Цена')
   published = models.DateTimeField(auto_now_add=True, db_index=True,
                                    verbose_name='Опубликовано')
   class Meta:
    verbose_name_plural = 'Объявления' 
    ordering = ['-published'] 

class Rubric(models.Model):
  def __str__(self):
    return self.name
  name = models.CharField(max_length=20, db_index=True,
                          verbose_name='Название')
  class Meta:
    verbose_name_plural = 'Рубрики'
    verbose_name = 'Рубрика'
    ordering = ['name'] 

from django.forms import ModelForm 
from .models import Bb
class BbForm(ModelForm):
  class Meta:
    model = Bb
    fields = ('title', 'content', 'price', 'rubric')
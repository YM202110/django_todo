from django.db import models

# Create your models here.

class TodoCategory(models.Model):
    name = models.CharField(
        '業務種別',
        max_length=255,
        blank=True,
        null=True,
        unique=True)

    def __str__(self):
        return self.name


class TodoStatus(models.Model):
    name = models.CharField(
        '処理状況',
        max_length=255,
        blank=True,
        null=True,
        unique=True)

    def __str__(self):
        return self.name

class Todo(models.Model):
    title = models.CharField(
        "タスク名", 
        max_length=30, 
        help_text='【社名】を記載してください')

    description = models.TextField(
        "詳細",
        blank=True,
        help_text='作成物の対象期間や属性などの詳細を記入してください')

    deadline = models.DateField(
        "締切")
    
    category = models.ForeignKey(
        TodoCategory,
        on_delete=models.CASCADE,
        verbose_name="業務種別")
    
    status = models.ForeignKey(
        TodoStatus,
        on_delete=models.CASCADE,
        verbose_name="処理状況")
    
    created_at = models.DateTimeField(
        verbose_name="登録日時", 
        auto_now_add=True)

    updated_at = models.DateTimeField(
        verbose_name="更新日時",
        auto_now=True
    )
    

    def __str__(self):
        return self.title
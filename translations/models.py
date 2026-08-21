from django.db import models


class Language(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'languages'
        ordering = ['name']

class Translation(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='translations')
    key = models.CharField(max_length=255)
    value = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'translations'
        constraints = [models.UniqueConstraint(fields=['language', 'key'], name='unique_language_translation_key')]
        ordering = ['key']
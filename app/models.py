from django.db import models


class TODO(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "ToDo"
        verbose_name_plural = "ToDos"

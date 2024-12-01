from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=100)  # Название фильма
    description = models.TextField()          # Описание фильма
    review = models.TextField()               # Отзыв о фильме

    def __str__(self):
        return self.title

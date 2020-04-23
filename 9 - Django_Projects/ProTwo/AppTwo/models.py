from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

        class Meta:
            verbose_name = 'Site Account'
            verbose_name_plural = 'Site Accounts'

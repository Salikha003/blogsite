from django.db import models


class PortfolioPage(models.Model):
    name = models.CharField(max_length=50, verbose_name='Portfolio nomi')
    about = models.TextField(verbose_name='Portfolio haqida')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'PortfolioPage'
        managed = True
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolio'


class PortfolioManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='active')

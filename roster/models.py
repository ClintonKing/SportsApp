from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(unique=True, max_length=25)
    school = models.CharField(unique=True, max_length=50, default='')
    players = models.ManyToManyField('Player', blank=True)


    class Meta(object):
        verbose_name_plural = "Teams"
        ordering = ('name',)

    def __unicode__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(unique=True, max_length=50)
    number = models.IntegerField(unique=False, max_length=2)
    hand = models.CharField(unique=False, max_length=4)
    position = models.CharField(unique=False, max_length=20, default='')
    height = models.CharField(unique=False, max_length=5)
    year = models.CharField(unique=False, max_length=10)
    hometown= models.CharField(unique=False, max_length=50)
    #photo = models.CharField(unique=True, max_length=200, default='', null=True)

    class Meta(object):
        verbose_name_plural = "Players"
        ordering = ('number',)

    def __unicode__(self):
        return self.name

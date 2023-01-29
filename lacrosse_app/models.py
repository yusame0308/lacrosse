from django.db import models
from django.core import validators


class Player(models.Model):
    name = models.CharField(max_length=32)
    grade = models.IntegerField()
    
    def __str__(self):
        return self.name


class Injury(models.Model):
    player = models.ForeignKey(Player, related_name='injuries', on_delete=models.CASCADE)
    body = models.CharField(max_length=32)
    date = models.TextField()
    # date = models.DateField()
    status = models.CharField(max_length=128)
    
    
class Stick(models.Model):
    depth_choices = (
        (0, 'アウト'),
        (1, 'ぴったり'),
    )
    string_choices = ((0, 'アウト'),)
    end_choices = ((0, 'アウト'),)
    ball_choices = (
        (0, '落ちない'),
        (1, '落ちづらい'),
    )
    player = models.ForeignKey(Player, related_name='sticks', on_delete=models.CASCADE)
    depth = models.IntegerField(null=True, choices=depth_choices)
    string = models.IntegerField(null=True, choices=string_choices)
    end = models.IntegerField(null=True, choices=end_choices)
    ball = models.IntegerField(null=True, choices=ball_choices)
    length = models.FloatField(null=True, validators=[validators.MinValueValidator(1), validators.MaxValueValidator(9)])
    narrow = models.FloatField(null=True, validators=[validators.MinValueValidator(0.5), validators.MaxValueValidator(9)])
    height = models.FloatField(null=True, validators=[validators.MinValueValidator(0.5), validators.MaxValueValidator(9)])
    
    
class Shot(models.Model):
    player = models.ForeignKey(Player, related_name='shots', on_delete=models.CASCADE)
    date = models.TextField()
    # date = models.DateField()
    score = models.IntegerField(default=0)
    gb = models.IntegerField(default=0)
    bd = models.IntegerField(default=0)
    pc = models.IntegerField(default=0)
    shot_all = models.IntegerField(default=0)
    shot_goal = models.IntegerField(default=0)
    shot_in = models.IntegerField(default=0)


class Post(models.Model):
    title = models.CharField('title', max_length=50)
    image = models.ImageField(upload_to='images')
    content = models.TextField('content')
    date = models.TextField('date')
    # date = models.DateTimeField('date')

    def __str__(self):
        return self.title
    

class Menu(models.Model):
    title = models.CharField('title', max_length=50)
    image = models.ImageField(upload_to='images')
    content = models.TextField('content')
    date = models.TextField('date')

    def __str__(self):
        return self.title
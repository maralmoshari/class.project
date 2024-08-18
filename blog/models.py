from django.db import models
from django.shortcuts import reverse
# Create your models here.


class Post(models.Model) :
    STATUS_CHOISES = (
        ('pub' , 'published') ,
        ('drf', 'Draft'),
    )
    title = models.CharField(max_length=50)
    discription = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOISES , max_length=3)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post_detail' , args=[self.id])

import os
import random
from django.db import models

# Create your models here.

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name , ext = os.path.splitext(base_name)
    return name , ext
def upload_path(instance , filename):
    new_filename = random.randint(1,2000)
    name , ext = get_filename_ext(filename)
    final_name = '{new_filename}{ext}'.format(new_filename=new_filename, ext = ext)
    return "newsApp/{new_filename}/{final_name}".format(new_filename = new_filename,  final_name =final_name)

class BlogModel(models.Model):
    
    title = models.CharField(max_length = 250)
    descirption = models.TextField()
    subdescription = models.TextField(max_length = 400, null = True)
    image = models.ImageField(upload_to=upload_path, null = True , blank = True)
    def __str__(self):
        return self.title
    def __unicode__(self):

        return  self.title

    
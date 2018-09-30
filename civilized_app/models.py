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
    return "civilized_app/{new_filename}/{final_name}".format(new_filename = new_filename,  final_name =final_name)


class FileUploadModel(models.Model):
    
    name = models.CharField(max_length = 100, blank=False, null=False)
    file_name = models.FileField(upload_to = upload_path, null = False , blank = False)



    def __str__(self):
        return self.name
    def __unicode__(self):

        return  self.name

class JobsProvied(models.Model):
    
    jobTitle = models.CharField(max_length=100, blank=True, null=True) 
    job_file_name = models.FileField(upload_to = upload_path, null = True , blank = True) 

    def __str__(self):
        return self.jobTitle
    def __unicode__(self):

        return  self.jobTitle

from django.db import models

# Create your models here.
class Banner(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='BannerImage')
    http_link = models.URLField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Banner'

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)
    main_category = models.ForeignKey('self', on_delete=models.CASCADE,  blank= True, null= True)
    def __str__(self):
        return self.name

    

class Content(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='international image')
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.title
    


    


    
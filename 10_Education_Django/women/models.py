from django.db import models
from django.urls import reverse

# Create your models here.
class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок') # 'vervose_name' is alternative name for admin panel
    # For "slug" of url
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.title
    
    # Thanks to this we can 'view on site' from admin panel
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug}) # pk is internal attribute of Model. It's 'primary key'
    
    # Special class for admin panel
    class Meta:
        verbose_name = 'Famous Women' # Add to end of name symbol 's'
        verbose_name_plural = 'Famous women' # So as not be symbol 's'
        ordering = ['-time_create', 'title'] # Sorting (and in the admin panel and on the site)


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Category')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk}) # pk is internal attribute of Model. It's 'primary key'
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id']

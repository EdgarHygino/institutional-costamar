from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Album(models.Model):
    '''Um album é um pacote de imagens, ele tem um titúlo e é um slug para sua
    identificacao'''
    class Meta:
        ordering = ('title',)

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    summary = RichTextField()
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='gallery/original',
    )

    def __str__(self):
        return self.title



# class Image(models.Model):
#     '''Cada intancia dessa classe contem uma imagem da galeria, com seu respectivo
#     thumbnail e imagem em tamanho real, podendo incluir varia imagens.'''

#     class Meta:
#         ordering = ('album', 'title',)

#     album = models.ForeignKey('Album')
#     title = models.CharField(max_length=100,)
#     description = models.TextField(blank=True)
#     original = models.ImageField(
#         null=True,
#         blank=True,
#         upload_to='gallery/original',
#     )
#     thumbnail = models.ImageField(
#         null=True,
#         blank=True,
#         upload_to='gallery/thumbnail',
#     )
#     publication = models.DateTimeField(default=datetime.now, blank=True)

#     def __unicode__(self):
#         return self.title

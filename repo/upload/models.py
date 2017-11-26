from django.db import models
from django.core.urlresolvers import reverse

class Files(models.Model):
    file_uploaded = models.FileField()

    def get_absolute_url(self):
        return reverse('upload:upload_csv')
from django.db import models

class ParameterGlobal(models.Model):
    nama_parameter = models.CharField(max_length=100)
    nilai_parameter = models.CharField(max_length=100)

    class Meta:
        ordering = ('nama_parameter',)

    def __str__(self):
        return self.nama_parameter

from django.db import models

class Report(models.Model):
    PILIH_APP = [
        ('marketing','marketing'),('training','training'),
        ('ekonomi','ekonomi'),('personalia','personalia'),
        ('global','global'),
    ]

    nama_laporan = models.CharField(max_length=50)
    script = models.CharField(max_length=50,blank=True,null=True,unique=True)
    app = models.CharField(max_length=20,choices=PILIH_APP)
    is_enable = models.BooleanField(default=True)

    class Meta:
        ordering = ('app','nama_laporan',)

    def __str__(self):
        return self.nama_laporan

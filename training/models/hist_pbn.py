from django.db import models
from training.models import Peserta, Materi
from enterprise.models import Trainer

class Histpbn(models.Model):
    peserta = models.ForeignKey(Peserta, on_delete=models.CASCADE)
    materi = models.ForeignKey(Materi, on_delete=models.CASCADE)
    tgl_training = models.DateField(blank=True,null=True)
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL,null=True)
    keterangan = models.TextField(max_length=500,blank=True,null=True)

    class Meta:
        ordering = ('-tgl_training','peserta','materi',)
        unique_together = ('peserta','materi','tgl_training','keterangan','trainer')

    def __str__(self):
        return self.peserta

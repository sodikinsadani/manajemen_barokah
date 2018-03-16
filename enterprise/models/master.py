from django.db import models

class Trainer(models.Model):
    nama_trainer = models.CharField(max_length=50)

    class Meta:
        ordering = ('nama_trainer',)

    def __str__(self):
        return self.nama_trainer

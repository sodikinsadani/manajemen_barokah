from django.db import models

class Kue(models.Model):
    PILIH_JENIS = [
        ('1','pastry'),('2','mini regular'),('3','regular'),
        ('4','kombinasi regular'),('5','medium'),('6','premium'),
        ('7','kombinasi spesial'),('8','exclusive'),
    ]

    nama_kue = models.CharField(max_length=100)
    harga = models.IntegerField()
    jenis_kue = models.CharField(max_length=2,choices=PILIH_JENIS)
    target = models.IntegerField()
    stok = models.IntegerField()
    terjual = models.IntegerField()
    sisa = models.IntegerField()
    keterangan = models.TextField(max_length=500,blank=True,null=True)

    class Meta:
        ordering = ('jenis_kue','nama_kue',)

    def __str__(self):
        return self.nama_kue

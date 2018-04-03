from django.db import models
from personalia.models import Member

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

    def save(self, *args, **kwargs):
        self.sisa = self.target - self.terjual

        super(Kue, self).save(*args, **kwargs)

    class Meta:
        ordering = ('jenis_kue','nama_kue',)

    def __str__(self):
        return self.nama_kue

class Penjualan(models.Model):
    PILIH_JENIS_TRANSAKSI = [
        ('1','jual'),('2','cancel'),#('3','ambil'),
        #('4','reture'),
    ]

    nama_konsumen = models.CharField(max_length=100)
    kue = models.ForeignKey(
        Kue,
        on_delete=models.SET_NULL,
        null=True
    )
    sales = models.ForeignKey(
        Member,
        on_delete=models.SET_NULL,
        null=True
    )
    jumlah = models.IntegerField()
    jenis_transaksi = models.CharField(max_length=2,choices=PILIH_JENIS_TRANSAKSI)
    #is_terkirim = models.BooleanField(default=False)
    #tgl_kirim = models.DateField(blank=True,null=True)
    tgl_penjualan = models.DateField(blank=True,null=True)
    keterangan = models.TextField(max_length=500,blank=True,null=True)

    class Meta:
        ordering = ('sales__individu__nama','nama_konsumen','kue__nama_kue',)

    def __str__(self):
        return self.nama_konsumen

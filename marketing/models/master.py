from django.db import models
from personalia.models import Individu, Member

class Sales(models.Model):
    PILIH_STASUS = [
        ('1','pemula'),('2','anggaran')
    ]

    sales_id = models.OneToOneField(
        Member,
        on_delete=models.CASCADE,
        primary_key=True
    )
    status = models.CharField(max_length=1,
        choices=PILIH_STASUS)
    target = models.IntegerField(blank=True,null=True)

    class Meta:
        ordering = ('status','sales_id__individu__nama',)

    def __str__(self): # __unicode__ on Python 2
        return '{}'.format(self.sales_id.individu.nama)

class Konsumen(models.Model):
    PILIH_STASUS = [
        ('1','pendekatan'),('2','pendataan'),('3','pengkondisian'),
        ('4','pengisian'),('5','pengajakan'),
    ]
    PILIH_SA = [
        ('ak','AK'),('pa','PA'),('bk1','BK_1'),('bk2','BK_2'),('bk3','BK_3')
    ]
    PILIH_SEG = [
        ('m','Mahasiswa'),('p','Pelajar'),('u','Umum')
    ]

    individu = models.OneToOneField(
        Individu,
        on_delete=models.CASCADE,
        primary_key=True
    )
    status = models.CharField(max_length=1,
        choices=PILIH_STASUS)
    tgl_finish = models.DateField(blank=True,null=True)
    status_aktif = models.CharField(max_length=5,choices=PILIH_SA,blank=True,null=True)
    segmentasi = models.CharField(max_length=1,choices=PILIH_SEG,blank=True,null=True)
    sales = models.ForeignKey(Sales, on_delete=models.SET_NULL,null=True)
    warga_media = models.BooleanField(default=False)
    keterangan = models.TextField(max_length=500,blank=True,null=True)

    class Meta:
        ordering = ('status_aktif','status','individu__nama')

    def __str__(self): # __unicode__ on Python 2
        return '{}'.format(self.individu.nama)

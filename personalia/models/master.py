from django.db import models
from django.utils import timezone

class Individu(models.Model):
    PILIH_JK = [
        ('L','Laki-laki'),('P','Perempuan'),
    ]

    PILIH_LULUSAN = [
        ('1','SD'),('2','SMP'),('3','SMA'),('4','D3'),('5','S1'),('6','S2'),('7','S3'),
    ]

    nama = models.CharField('nama lengkap',max_length=50)
    tmpt_lahir = models.CharField(max_length=50,blank=True,null=True)
    tgl_lahir = models.DateField(blank=True,null=True)
    jk = models.CharField(max_length=1,choices=PILIH_JK)
    alamat = models.TextField(max_length=200,blank=True,null=True)
    alamat_desa = models.CharField(max_length=50,blank=True,null=True)
    alamat_kec = models.CharField(max_length=50,blank=True,null=True)
    alamat_kabkot = models.CharField(max_length=50,blank=True,null=True)
    alamat_prov = models.CharField(max_length=50,blank=True,null=True)
    lulusan = models.CharField(max_length=3,choices=PILIH_LULUSAN,blank=True,null=True)
    hp = models.CharField(max_length=15,blank=True,null=True)

    class Meta:
        ordering = ('jk','nama',)
        unique_together = ('nama','jk','alamat_kec','alamat_kabkot','alamat_prov')

    def __str__(self):
        return self.nama

class Pangkal(models.Model):
    PILIH_RT = [
        ('ahm','ahmad'),('ksm','kusmawan'),('mgd','migud'),
        ('sdk','sodikin'),('sdr','sodirun'),
    ]

    id_pk = models.CharField(max_length=5,primary_key=True,)
    nama = models.CharField(max_length=50)
    rt = models.CharField(max_length=5,choices=PILIH_RT)

    class Meta:
        ordering = ('rt','id_pk',)

    def __str__(self):
        return self.nama

class Member(models.Model):
    PILIH_JEN = [
        ('0','WB'),('1','Pra A1'),('2','A1.1'),('3','A1.2'),('4','A1.3'),('5','A2')
    ]
    #('0','WB'),('1','Pra A1'),('2','A1'),('3','A2')

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
    jenjang = models.CharField(max_length=1,
        choices=PILIH_JEN)
    tgl_daftar = models.DateField(blank=True,null=True)
    status_aktif = models.CharField(max_length=5,choices=PILIH_SA,blank=True,null=True)
    segmentasi = models.CharField(max_length=1,choices=PILIH_SEG,blank=True,null=True)
    pangkal = models.ForeignKey(Pangkal, on_delete=models.SET_NULL,null=True)
    warga_media = models.BooleanField(default=False)
    keterangan = models.TextField(max_length=500,blank=True,null=True)
    tgl_input = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('status_aktif','jenjang',)

    def __str__(self): # __unicode__ on Python 2
        return '{}'.format(self.individu)

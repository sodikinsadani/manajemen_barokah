from django.db import models
from personalia.models import Member

'''class Simpanan(models.Model):
    member = models.OneToOneField(
        Member,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    jumlah = models.IntegerField()
    tgl_setor = models.DateField(blank=True,null=True)

    class Meta:
        ordering = ('member',)

    def __str__(self):
        return self.member'''

class Insod(models.Model):
    PILIH_JENIS = [
        ('1','pemula'),('2','infaq'),('3','shodaqoh'),
        ('4','zakat mal'),('5','ksp'),('6','aqiqah'),
        ('7','temuan'),('8','fidyah'),('9','nazar'),
        ('10','external'),('11','lain-lain')
    ]

    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
    )
    jumlah = models.IntegerField()
    tgl_setor = models.DateField(blank=True,null=True)
    jenis_insod = models.CharField(max_length=2,choices=PILIH_JENIS,default='2')
    keterangan = models.TextField(max_length=500,blank=True,null=True)

    class Meta:
        ordering = ('-tgl_setor','member__individu__jk','member__individu__nama',)

    def __str__(self):
        return self.member.individu.nama

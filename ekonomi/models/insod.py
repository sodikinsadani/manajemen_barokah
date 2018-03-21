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
    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
    )
    jumlah = models.IntegerField()
    tgl_setor = models.DateField(blank=True,null=True)
    keterangan = models.TextField(max_length=500,blank=True,null=True)

    class Meta:
        ordering = ('-tgl_setor','member',)

    def __str__(self):
        return self.member.individu.nama

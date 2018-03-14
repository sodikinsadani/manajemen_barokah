from django.db import models
from personalia.models import Member

class Materi(models.Model):
    PILIH_JEN = [
        ('0','WB'),('1','Pra A1'),('2','A1.1'),('3','A1.2'),('4','A1.3'),('5','A2')
    ]

    judul_materi = models.CharField(max_length=50, unique=True)
    jenjang = models.CharField(max_length=1, choices=PILIH_JEN)

    class Meta:
        ordering = ('jenjang','judul_materi',)

    def __str__(self):
        return self.judul_materi

class Peserta(models.Model):
    PILIH_JEN = [
        ('0','WB'),('1','Pra A1'),('2','A1.1'),('3','A1.2'),('4','A1.3'),('5','A2')
    ]

    id_peserta = models.OneToOneField(
        Member,
        on_delete=models.CASCADE,
        primary_key=True,
        #limit_choices_to={'individu__jk': 'L'},
    )
    jenjang = models.CharField(max_length=1, choices=PILIH_JEN)

    class Meta:
        ordering = ('jenjang','id_peserta__individu__nama',)

    def __str__(self):
        return self.id_peserta

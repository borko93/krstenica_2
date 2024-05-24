from django.db import models

# Create your models here.
class krsteni_list(models.Model):
    knjiga = models.CharField(max_length=10)
    strana = models.CharField(max_length=1000)
    broj = models.CharField(max_length=100000)

    eparhija = models.CharField(max_length=100)
    hram = models.CharField(max_length=100)
    mjesto = models.CharField(max_length=30)
    godina = models.CharField(max_length=4)

    datum_rodjenja = models.CharField(max_length=11)
    datum_krstenja = models.CharField(max_length=11)
    mjesto_rodjenja = models.CharField(max_length=30)
    ime_prezime_i_pol = models.CharField(max_length=50)
    ime_prezime_zanimanje_roditelja = models.TextField()
    dijete_po_rođenju = models.CharField(max_length=10)
    dijete_bračno = models.CharField(max_length=20)
    dijete_blizanac = models.CharField(max_length=10)
    dijete_mana = models.CharField(max_length=5)
    sveštenik = models.CharField(max_length=50)
    kum = models.CharField(max_length=50)
    strana_domovnika = models.CharField(max_length=10)
    primjedba = models.TextField()
    br_protokola = models.CharField(max_length=10)
    datum = models.DateField(auto_now=True)
    mjesto_izdavanja = models.CharField(max_length=20)
    parohija = models.CharField(max_length=30)

    def __str__(self):
        return self.ime_prezime_i_pol




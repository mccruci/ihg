from django.db import models

# Create your models here.
"""
oggetto Mappa
coordinate -> mappa             |-> Stanza -> Reparto -> Edificio
           |-> mappa_allarme    |-^
"""

class Coordinate(models.Model):
    """
    modello coordinate per mappe
    CODICE = crd
    """
    crd_cod = models.AutoField(primary_key=True)
    crd_I = models.CharField(max_length=60)
    crd_X = models.CharField(max_length=60)
    crd_XY = models.CharField(max_length=60)
    crd_Y = models.CharField(max_length=60)

class Mappa(models.Model):
    """
    CODICE = mpp
    """
    TIPO_USO = (
        ('M', 'Mappa_Stanza'),
        ('A','Allarme_Stanza'),
    )
    mpp_cod = models.AutoField(primary_key=True)
    mpp_uso = models.CharField(max_length=1, choices=TIPO_USO)
    mpp_crd_cod = models.ForeignKey(Coordinate, on_delete=models.CASCADE)

class Device(models.Model):
    """
    CODICE = dev
    """
    dev_cod = models.AutoField(primary_key=True)
    dev_ip = models.CharField(max_length=100)
    dev_mpp = models.ForeignKey(Mappa, on_delete=models.CASCADE)

class Sito(models.Model):
    """
    CODICE = sti
    """
    sit_cod = models.AutoField(primary_key=True)
    sit_denominazione = models.CharField(max_length=100)
    #sit-spd_cod = relezione con ospedale
    sit_ospedale = models.CharField(max_length=100)
    sit_indirizzo = models.CharField(max_length=100)


class Edificio(models.Model):
    """
    CODICE = dfc
    """
    dfc_cod = models.AutoField(primary_key=True)
    dfc_sit_cod = models.ForeignKey(Sito, on_delete=models.CASCADE)
    dfc_nome = models.CharField(max_length=100)
    dfc_indirizzo = models.CharField(max_length=100)

class Piano(models.Model):
    """
    CODICE = pno
    """
    pno_cod = models.AutoField(primary_key=True)
    pno_dfc_cod = models.ForeignKey(Edificio, on_delete=models.CASCADE)
    pno_numero = models.IntegerField()

class Reparto(models.Model):
    """
    CODICE = rpt
    """
    rpt_cod = models.AutoField(primary_key=True)
    rpt_spd_cod = models.ForeignKey(Piano, on_delete=models.CASCADE)
    rpt_nome = models.CharField(max_length=100)

class Stanza(models.Model):
    """
    CODICE = dfc
    """
    TIPO_USO = (
        ('D', 'Degenza'),
        ('C','Controllo'),
    )
    stz_cod = models.AutoField(primary_key=True)
    #da vedere
    stz_pno_cod = models.ForeignKey(Piano, on_delete=models.CASCADE)
    stz_rpt_cod = models.ForeignKey(Reparto, on_delete=models.CASCADE)
    stz_numero = models.IntegerField()
    stz_uso = models.CharField(max_length=1, choices=TIPO_USO)
    stz_mpp_cod = models.ForeignKey(Mappa, on_delete=models.CASCADE, null=True)



class Letto(models.Model):
    """
    CODICE = dfc
    """
    ltt_cod = models.AutoField(primary_key=True)
    #ltt_dgn_cod = collegamento a Degenza
    ltt_num = models.IntegerField()
    #ltt_pzt_cod = collegamento a paziente
    #aggiunta da verificare
    ltt_stz_cod = models.ForeignKey(Stanza, on_delete=models.CASCADE)

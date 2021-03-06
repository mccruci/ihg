from django.db import models

# Create your models here.
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""          DEFINIZIONE SITO                            """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class Ospedale(models.Model):
    """
    CODICE = osp
    """
    osp_cod = models.AutoField(primary_key=True)
    osp_societa = models.CharField(max_length=100)

class Sito(models.Model):
    """
    CODICE = sti
    """
    sit_cod = models.AutoField(primary_key=True)
    sit_denominazione = models.CharField(max_length=100)
    sit_osp_cod = models.ForeignKey(Ospedale, on_delete=models.CASCADE)
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
    rpt_spd_cod = models.ForeignKey(Edificio, on_delete=models.CASCADE)
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
    #stz_mpp_cod = models.ForeignKey(Mappa, on_delete=models.CASCADE, null=True)

class Ambiente(models.Model):
    """
    collegato a + zone ed a un Device
    CODICE = amb
    """
    TIPO_AMB=(
            ('F','Finestra'),
            ('B','Bagno'),
            ('L','Letto'),
            )
    amb_cod = models.AutoField(primary_key=True)
    amb_stz_cod = models.ForeignKey(Stanza, on_delete=models.CASCADE)
    amb_tipo = models.CharField(max_length=1, choices=TIPO_AMB)

class Device(models.Model):
    """
    CODICE = dev
    """
    dev_cod = models.AutoField(primary_key=True)
    dev_ip = models.CharField(max_length=100)
    dev_stz_cod = models.ForeignKey(Stanza, on_delete=models.CASCADE)
    dev_soglia_allarme_n_persone = models.CharField(max_length=10)

class Zone(models.Model):
    """
    CODICE zno
    """
    TIPO_ZONA=(
        ('L','Letto'),
        ('B', 'Bagno'),
        ('P', 'Porta'),
        ('S', 'Stanza'),
    )
    zno_cod = models.AutoField(primary_key=True)
    zno_tipo = models.CharField(max_length=1, choices=TIPO_ZONA)
    zno_stz_cod = models.ForeignKey(Stanza, on_delete=models.CASCADE)
    #zno_crd_cod = models.ForeignKey(Coordinate, on_delete=models.CASCADE)
    zno_asse0 = models.CharField(max_length=40)
    zno_asseX = models.CharField(max_length=40)
    zno_asseXY = models.CharField(max_length=40)
    zno_asseY = models.CharField(max_length=40)

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

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""          DEFINIZIONE DEVICE E MAPPE                  """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
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
    mpp_cod = models.AutoField(primary_key=True)
    #mpp_uso = models.CharField(max_length=1, )
    mpp_stz_cod = models.ForeignKey(Stanza, on_delete=models.CASCADE)
    mpp_crd_cod = models.ForeignKey(Coordinate, on_delete=models.CASCADE)


class Persone(models.Model):
    """
    CODICE = prs
    """
    prs_cod = models.AutoField(primary_key=True)
    prs_stz_cod = models.ForeignKey(Stanza, on_delete=models.CASCADE)
    prs_num = models.CharField(max_length=2)
    prs_time = models.DateTimeField()

class CoordinatePersone(models.Model):
    """
    CODICE = cpr
    """
    cpr_cod = models.AutoField(primary_key=True)
    cpr_dev_cod = models.ForeignKey(Persone, on_delete=models.CASCADE)
    cpr_asseX = models.CharField(max_length=10)
    cpr_asseY = models.CharField(max_length=10)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""          DEFINIZIONE ALLARMI                         """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class Allarme_zona(models.Model):
    """
    CODICE = all
    """
    all_cod = models.AutoField(primary_key=True)
    all_zno_cod = models.OneToOneField(Zone, on_delete=models.CASCADE)
    all_inizio_allarme = models.TimeField()
    all_fine_allarme = models.TimeField()
    all_numero_max_persone = models.IntegerField(max_length=2)

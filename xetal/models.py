from django.db import models

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""          DEFINIZIONE SITO OSPEDALE                   """
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

class Reparto(models.Model):
    """
    CODICE = rpt
    """
    rpt_cod = models.AutoField(primary_key=True)
    rpt_spd_cod = models.ForeignKey(Edificio, on_delete=models.CASCADE)
    rpt_nome = models.CharField(max_length=100)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""          DEFINIZIONE LOCALIZZAZIONE APPARATI         """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class Mappa(models.Model):
    """
    CODICE = mpp
    definizione coordinate
    """
    mpp_cod = models.AutoField(primary_key=True)
    mpp_asse0 = models.CharField()
    mpp_asseX = models.CharField()
    mpp_asseY = models.CharField()
    mpp_asseXY = models.CharField()

class Stanza(models.Model):
    """
    CODICE = dfc
    """
    TIPO_USO = (
        ('D', 'Degenza'),
        ('C','Controllo'),
    )
    stz_cod = models.AutoField(primary_key=True)
    stz_pno = models.IntegerField()
    stz_rpt_cod = models.ForeignKey(Reparto, on_delete=models.CASCADE)
    stz_numero = models.IntegerField()
    stz_uso = models.CharField(max_length=1, choices=TIPO_USO)

class Ambiente(models.Model):
    """
    CODICE = amb
    """
    TIPO_AMBIENTE = (
        ('L','ZONA LETTI'),
        ('B','ZONA BAGNO'),
        ('A','ZONA ATRIO'),
    )
    amb_cod = models.AutoField(primary_key=True)
    amb_tipo = models.CharField(max_length=1, choices=TIPO_AMBIENTE)

class Device(models.Model):
    """
    CODICE = dev
    """
    TIPO_DEVICE=(
        ('B','Barra'),
        ('W','WiFi'),
    )
    dev_cod = models.AutoField(primary_key=True)
    dev_ip = models.CharField()
    dev_amb_cod = models.ForeignKey(Ambiente, on_delete=models.CASCADE)
    dev_tipo = models.CharField(max_length=1, choices=TIPO_DEVICE)
    dev_mappa = models.OneToOneField(Mappa, on_delete=models.CASCADE)

class Zone(models.Model):
    """
    CODICE = zno
    """
    TIPO_ZONE= (
        ('L-1','Zona Letto 1'),
        ('L-2','Zona Letto 2'),
        ('L-F','Zona Finestra'),
        ('L-G','Zona Generale'),
        ('B-G','Bagno Generale'),
        ('A-P','Atrio Porta'),
        ('A-G','Atrio Generale')
    )
    TIPO_ALLARME=(
        ('S','Sicuro'),
        ('M','Medio'),
        ('P','Pericolo'),
    )
    zno_cod = models.AutoField(primary_key=True)
    zno_dev_cod = models.ForeignKey(Device, on_delete=models.CASCADE)
    zno_tipo = models.CharField(max_length=3, choices=TIPO_ZONE)
    zno_mappa = models.OneToOneField(Mappa, on_delete=models.CASCADE)
    zno_tipo_allarme = models.CharField(max_length=1, choices=TIPO_ALLARME)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""          DEFINIZIONE Allarmi da rivedere ?????       """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class SogliaAllarme(models.Model):
    """
    CODICE = sll
    """
    TIPO_SOGLIA=(
        ('N', 'Normale'),
        ('M', 'Medio'),
        ('P','Pericolo'),
    )
    sll_cod = models.AutoField(primary_key=True)
    sll_tipo = models.CharField(max_length=1, choices=TIPO_SOGLIA)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""          DEFINIZIONE COORDINATE PERSONE              """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class CoordinatePersone(models.Model):
    """
    CODICE = cpr
    """
    cpr_cod = models.AutoField(primary_key=True)
    cpr_asse0 = models.CharField()
    cpr_asseX = models.CharField()
    cpr_asseY = models.CharField()
    cpr_asseXY = models.CharField()

class Allarme(models.Model):
    """
    CODICE = all
    """
    all_cod = models.AutoField(primary_key=True)
    all_num_persone = models.IntegerField()
    all_tmp = models.DateTimeField()
    all_cpr_cod = models.ForeignKey(CoordinatePersone, on_delete=models.CASCADE)
    all_zno_cod = models.ForeignKey(Zone, on_delete=models.CASCADE)
    



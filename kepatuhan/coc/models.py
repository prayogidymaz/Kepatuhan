from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.functional import cached_property


JENIS_LAYANAN_CHOICE = [
    ('Upload Data Badan Usaha', 'Upload Data Badan usaha'),
    ('Download Sertifikat Badan Usaha', 'Download Sertifikat Badan Usaha'),
]

STATUS_PROSES_CHOICE = [
    ('Terkirim', 'Terkirim'),
    ('Berhasil', 'Berhasil'),
    ('Gagal', 'Gagal'),
]

BACA_NOTIF_CHOICE = [
    ('not_read', 'not_read'),
    ('read', 'read'),
]

class DataBu (models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    jenis_layanan = models.CharField(max_length=50, choices=JENIS_LAYANAN_CHOICE)
    status_proses = models.CharField(max_length=20, choices=STATUS_PROSES_CHOICE, default='Terkirim')
    baca_notif = models.CharField(max_length=100, choices=BACA_NOTIF_CHOICE, default='not_read')
    kode_bu = models.CharField(max_length=8, blank=True, null=True)
    nama_bu = models.CharField(max_length=50, blank=True, null=True)
    nomor_npwp = models.CharField(max_length=15, blank=True, null=True)
    nomor_nib = models.CharField(max_length=13, blank=True, null=True)
    jumlah_pekerja = models.CharField(max_length=5, blank=True, null=True)
    upload_spt = models.FileField(upload_to='documents/', blank=True, null=True)
    upload_data_pekerja = models.FileField(upload_to='documents/', blank=True, null=True)
    upload_data_gaji = models.FileField(upload_to='documents/', blank=True, null=True)
    upload_sipp = models.FileField(upload_to='documents/', blank=True, null=True)
    tgl_kirim = models.DateTimeField(blank=True, null=True)
    tgl_selesai = models.DateTimeField(blank=True, null=True)


    

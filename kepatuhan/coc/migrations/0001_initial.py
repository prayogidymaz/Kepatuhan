# Generated by Django 2.2.16 on 2020-10-25 07:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DataBu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis_layanan', models.CharField(choices=[('Upload Data Badan Usaha', 'Upload Data Badan usaha'), ('Download Sertifikat Badan Usaha', 'Download Sertifikat Badan Usaha')], max_length=50)),
                ('status_proses', models.CharField(choices=[('Terkirim', 'Terkirim'), ('Berhasil', 'Berhasil'), ('Gagal', 'Gagal')], default='Terkirim', max_length=20)),
                ('baca_notif', models.CharField(choices=[('not_read', 'not_read'), ('read', 'read')], default='not_read', max_length=100)),
                ('kode_bu', models.CharField(blank=True, max_length=8, null=True)),
                ('nomor_npwp', models.CharField(blank=True, max_length=15, null=True)),
                ('nomor_nib', models.CharField(blank=True, max_length=13, null=True)),
                ('jumlah_pekerja', models.CharField(blank=True, max_length=5, null=True)),
                ('nama_bu', models.CharField(blank=True, max_length=50, null=True)),
                ('upload_spt', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('upload_data_pekerja', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('upload_data_gaji', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('upload_sipp', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('tgl_kirim', models.DateTimeField(blank=True, null=True)),
                ('tgl_selesai', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

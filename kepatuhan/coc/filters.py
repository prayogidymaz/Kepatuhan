import django_filters
from .models import DataBu

STATUS_PROSES_CHOICE = [
    ('Terkirim', 'Terkirim'),
    ('Berhasil', 'Berhasil'),
    ('Gagal', 'Gagal'),
]

class Filter(django_filters,FilterSet):
    class Meta:
        model = DataBu
        fields =['jenis_layanan', 'kode_bu', 'nama_bu', 'jumlah_pekerja', 'nomor_npwp', 'nomor_nib', 'tgl_kirim', 'tgl_terima', 'status_proses',]
import csv

laboratorium = [
    ('1','Laboratorium Multimedia','135-Ruang Praktek Siswa','12','8','Milik','Baik'),
    ('2','Laboratorium Komputer','301-Ruang Praktek Siswa1','14','8','MilikBaik'),
    ('3','Kamar Mandi/WC Guru Laki-Laki','Ruang Penunjang','2','1','Milik','Baik'),
    ('4','Ruang Teori/Kelas','132-Ruang Teori','9','8','Milik','Baik'),
    ('5','Ruang Teori/Kelas','126-Ruang Teori','9','8','Milik','Baik'),
    ('6','Ruang TU','Ruang Penunjang','8','6','Milik','Baik'),
    ('7','Laboratorium Hotel','125-RPLS','9','8','Milik Baik'),
    ('8','Gudang','404-Ruang Penunjang','7','4','Milik Baik'),
    ('9', 'Kamar Mandi/WC Guru Perempuan', 'Ruang Penunjang', '2', '1', 'Milik', 'Baik'),
    ('10','Laboratorium Komputer','302-Ruang Praktek Siswa1','14','8','MilikBaik')
]
#Lokasi File
f = open('laboratorium.csv','w')
w = csv.writer(f)
w.writerow(('No','Jenis Prasarana','Nama','Panjang (m)','Lebar (m)','Kepemilikan','Kondisi Kerusakan'))

#Menulis Row
for lab in laboratorium:
    w.writerow(lab)

#Menutup ifile
f.close()
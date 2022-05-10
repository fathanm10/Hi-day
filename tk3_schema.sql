CREATE TABLE akun (
	email VARCHAR(50), 
	PRIMARY KEY (email)
);

-- Level tidak usah diimplementasi
-- CREATE TABLE level (
-- 	nomor INT,
-- 	min_xp INT NOT NULL,
-- 	PRIMARY KEY (nomor)
-- );

CREATE TABLE admin (
	email VARCHAR(50),
	password VARCHAR(25) NOT NULL,
	PRIMARY KEY (email),
	FOREIGN KEY (email) REFERENCES akun(email) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE pengguna (
	email VARCHAR(50),
	password VARCHAR(25) NOT NULL,
	nama_area_pertanian VARCHAR(25) NOT NULL,
	xp INT NOT NULL DEFAULT 0,
	koin INT NOT NULL DEFAULT 0,
	level INT NOT NULL DEFAULT 1,
	PRIMARY KEY (email),
	FOREIGN KEY (email) REFERENCES akun(email) ON UPDATE CASCADE ON DELETE CASCADE
	-- FOREIGN KEY (level) REFERENCES level(nomor) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE paket_koin (
	jumlah_koin INT,
	harga INT NOT NULL,
	PRIMARY KEY (jumlah_koin)
);

CREATE TABLE transaksi_pembelian_koin (
	email VARCHAR(50),
	waktu TIMESTAMP,
	jumlah INT NOT NULL,
	cara_pembayaran VARCHAR(15) NOT NULL,
	paket_koin INT NOT NULL,
	total_biaya INT NOT NULL,
	PRIMARY KEY (email, waktu),
	FOREIGN KEY (email) REFERENCES akun(email) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (paket_koin) REFERENCES paket_koin(jumlah_koin) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE lumbung (
	email VARCHAR(50),
	level INT NOT NULL,
	kapasitas_max INT NOT NULL,
	total INT NOT NULL,
	PRIMARY KEY (email),
	FOREIGN KEY (email) REFERENCES akun(email) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE transaksi_upgrade_lumbung (
	email VARCHAR(50),
	waktu TIMESTAMP,
	PRIMARY KEY (email, waktu),
	FOREIGN KEY (email) REFERENCES akun(email) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE aset (
	ID VARCHAR(5),
	nama VARCHAR(50) UNIQUE NOT NULL,
	min_level INT NOT NULL,
	harga_beli INT NOT NULL,
	PRIMARY KEY (ID)
);

CREATE TABLE dekorasi (
	ID_aset VARCHAR(5),
	harga_jual INT NOT NULL,
	PRIMARY KEY (ID_aset),
	FOREIGN KEY (ID_aset) REFERENCES aset(ID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE bibit_tanaman (
	ID_aset VARCHAR(5),
	durasi_panen TIME NOT NULL,
	PRIMARY KEY (ID_aset),
	FOREIGN KEY (ID_aset) REFERENCES aset(ID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE kandang (
	ID_aset VARCHAR(5),
	kapasitas_max TIME NOT NULL,
	jenis_hewan VARCHAR(50) UNIQUE NOT NULL,
	PRIMARY KEY (ID_aset),
	FOREIGN KEY (ID_aset) REFERENCES aset(ID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE hewan (
	ID_aset VARCHAR(5),
	durasi_produksi TIME NOT NULL,
	ID_kandang VARCHAR(5) NOT NULL,
	PRIMARY KEY (ID_aset),
	FOREIGN KEY (ID_aset) REFERENCES aset(ID) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (ID_kandang) REFERENCES kandang(ID_aset) ON UPDATE CASCADE ON DELETE CASCADE
);
CREATE TABLE alat_produksi (
	ID_aset VARCHAR(5),
	kapasitas_max INT NOT NULL,
	PRIMARY KEY (ID_aset),
	FOREIGN KEY (ID_aset) REFERENCES aset(ID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE petak_sawah (
	ID_aset VARCHAR(5),
	jenis_tanaman VARCHAR(50) UNIQUE NOT NULL,
	PRIMARY KEY (ID_aset),
	FOREIGN KEY (ID_aset) REFERENCES aset(ID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE koleksi_aset (
	email VARCHAR(50),
	PRIMARY KEY (email),
	FOREIGN KEY (email) REFERENCES akun(email) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE koleksi_aset_memiliki_aset (
	ID_koleksi_aset VARCHAR(50),
	ID_aset VARCHAR(5),
	jumlah INT NOT NULL,
	PRIMARY KEY (ID_koleksi_aset, ID_aset),
	FOREIGN KEY (ID_koleksi_aset) REFERENCES koleksi_aset(email) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (ID_aset) REFERENCES aset(ID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE transaksi_pembelian (
	email VARCHAR(50),
	waktu TIMESTAMP,
	jumlah INT NOT NULL,
	ID_aset VARCHAR(5) NOT NULL,
	PRIMARY KEY (email, waktu),
	FOREIGN KEY (email) REFERENCES akun(email) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (ID_aset) REFERENCES aset(ID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE produk (
	ID VARCHAR(5),
	nama VARCHAR(50) UNIQUE NOT NULL,
	harga_jual INT NOT NULL,
	sifat_produk VARCHAR(20) NOT NULL,
	PRIMARY KEY (ID)
);

CREATE TABLE produk_hewan (
	ID_produk VARCHAR(5),
	PRIMARY KEY (ID_produk),
	FOREIGN KEY (ID_produk) REFERENCES produk(ID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE hasil_panen (
	ID_produk VARCHAR(5),
	PRIMARY KEY (ID_produk),
	FOREIGN KEY (ID_produk) REFERENCES produk(ID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE produk_makanan (
	ID_produk VARCHAR(5),
	PRIMARY KEY (ID_produk),
	FOREIGN KEY (ID_produk) REFERENCES produk(ID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE produk_dibutuhkan_oleh_produk_makanan (
	ID_produk_makanan VARCHAR(5),
	ID_produk VARCHAR(5),
	jumlah INT NOT NULL,
	PRIMARY KEY (ID_produk_makanan, ID_produk),
	FOREIGN KEY (ID_produk_makanan) REFERENCES produk_makanan(ID_produk) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (ID_produk) REFERENCES produk(ID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE lumbung_memiliki_produk (
	ID_lumbung VARCHAR(5),
	ID_produk VARCHAR(5),
	jumlah INT NOT NULL,
	PRIMARY KEY (ID_lumbung, ID_produk),
	FOREIGN KEY (ID_lumbung) REFERENCES lumbung(email) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (ID_produk) REFERENCES produk(ID) ON UPDATE CASCADE ON DELETE CASCADE
);

-- Tidak usah diimplementasi
-- BIBIT_TANAMAN_MENGHASILKAN_HASIL_PANEN
-- HEWAN_MEMBUTUHKAN_HASIL_PANEN
-- BIBIT_TANAMAN_DITANAM_DI_PETAK_SAWAH
-- HEWAN_MENGHASILKAN_PRODUK_HEWAN

CREATE TABLE produksi (
	ID_alat_produksi VARCHAR(5),
	ID_produk_makanan VARCHAR(5) UNIQUE,
	durasi TIME NOT NULL,
	jumlah_hasil_unit INT NOT NULL,
	PRIMARY KEY (ID_alat_produksi, ID_produk_makanan),
	FOREIGN KEY (ID_alat_produksi) REFERENCES alat_produksi(ID_aset) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (ID_produk_makanan) REFERENCES produk_makanan(ID_produk) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE histori_produksi (
	email VARCHAR(50),
	waktu_awal TIMESTAMP,
	waktu_selesai TIMESTAMP NOT NULL,
	jumlah INT,
	xp INT NOT NULL,
	PRIMARY KEY (email, waktu_awal),
	FOREIGN KEY (email) REFERENCES pengguna(email) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE histori_tanaman (
	email VARCHAR(50),
	waktu_awal TIMESTAMP,
	ID_bibit_tanaman VARCHAR(5) NOT NULL,
	PRIMARY KEY (email, waktu_awal),
	FOREIGN KEY (email, waktu_awal) REFERENCES histori_produksi(email, waktu_awal) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (ID_bibit_tanaman) REFERENCES bibit_tanaman(ID_aset) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE histori_hewan (
	email VARCHAR(50),
	waktu_awal TIMESTAMP,
	ID_hewan VARCHAR(5) NOT NULL,
	PRIMARY KEY (email, waktu_awal),
	FOREIGN KEY (email, waktu_awal) REFERENCES histori_produksi(email, waktu_awal) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (ID_hewan) REFERENCES hewan(ID_aset) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE histori_produksi_makanan (
	email VARCHAR(50),
	waktu_awal TIMESTAMP,
	ID_alat_produksi VARCHAR(5) NOT NULL,
	ID_produk_makanan VARCHAR(5) NOT NULL,
	PRIMARY KEY (email, waktu_awal),
	FOREIGN KEY (email, waktu_awal) REFERENCES histori_produksi(email, waktu_awal) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (ID_alat_produksi, ID_produk_makanan) REFERENCES produksi(ID_alat_produksi, ID_produk_makanan) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE pesanan (
	ID VARCHAR(5),
	status VARCHAR(20) NOT NULL,
	jenis VARCHAR(5) NOT NULL,
	nama VARCHAR(50) NOT NULL,
	total INT,
	PRIMARY KEY (ID)
);

CREATE TABLE detail_pesanan (
	ID_pesanan VARCHAR(5),
	no_urut VARCHAR(20),
	subtotal VARCHAR(15) NOT NULL,
	jumlah INT NOT NULL,
	ID_produk VARCHAR(5) NOT NULL,
	PRIMARY KEY (ID_pesanan, no_urut),
	FOREIGN KEY (ID_pesanan) REFERENCES pesanan(ID) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (ID_produk) REFERENCES produk(ID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE histori_penjualan (
	email VARCHAR(50),
	waktu_penjualan TIMESTAMP,
	koin INT NOT NULL,
	xp INT NOT NULL,
	ID_pesanan VARCHAR(5),
	PRIMARY KEY (email, waktu_penjualan),
	FOREIGN KEY (email) REFERENCES akun(email) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (ID_pesanan) REFERENCES pesanan(ID) ON UPDATE CASCADE ON DELETE CASCADE
);
-- DEKORASI_MEMILIKI_HISTORI_PENJUALAN
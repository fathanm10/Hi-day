CREATE TABLE akun (
	email VARCHAR(50), 
	PRIMARY KEY (email)
);

CREATE TABLE level (
	nomor INT,
	min_xp INT NOT NULL,
	PRIMARY KEY (nomor)
);

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
	FOREIGN KEY (email) REFERENCES akun(email) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (level) REFERENCES level(nomor) ON UPDATE CASCADE ON DELETE CASCADE
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
	kapasitas_max INT NOT NULL,
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
	ID_lumbung VARCHAR(50),
	ID_produk VARCHAR(5),
	jumlah INT NOT NULL,
	PRIMARY KEY (ID_lumbung, ID_produk),
	FOREIGN KEY (ID_lumbung) REFERENCES lumbung(email) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (ID_produk) REFERENCES produk(ID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE bibit_tanaman_menghasilkan_hasil_panen (
	ID_Bibit_Tanaman VARCHAR(5),
	ID_Hasil_Panen  VARCHAR(5),
	PRIMARY KEY (ID_Bibit_Tanaman, ID_Hasil_Panen),
	FOREIGN KEY (ID_Bibit_Tanaman) REFERENCES bibit_tanaman(ID_aset) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (ID_Hasil_Panen) REFERENCES hasil_panen(ID_produk) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE HEWAN_MEMBUTUHKAN_HASIL_PANEN (
	ID_Hewan VARCHAR(5),
	ID_Hasil_Panen  VARCHAR(5),
	jumlah INT NOT NULL,
	PRIMARY KEY (ID_Hewan, ID_Hasil_Panen),
	FOREIGN KEY (ID_Hewan) REFERENCES hewan(ID_aset) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (ID_Hasil_Panen) REFERENCES hasil_panen(ID_produk) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE BIBIT_TANAMAN_DITANAM_DI_PETAK_SAWAH (
	ID_Bibit_Tanaman VARCHAR(5),
	ID_Petak_Sawah VARCHAR(5),
	PRIMARY KEY (ID_Bibit_Tanaman, ID_Petak_Sawah),
	FOREIGN KEY (ID_Bibit_Tanaman) REFERENCES bibit_tanaman(ID_aset) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (ID_Petak_Sawah) REFERENCES petak_sawah(ID_aset) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE HEWAN_MENGHASILKAN_PRODUK_HEWAN (
	ID_Hewan VARCHAR(5),
	ID_Produk_Hewan  VARCHAR(5),
	PRIMARY KEY (ID_Hewan, ID_Produk_Hewan),
	FOREIGN KEY (ID_Hewan) REFERENCES hewan(ID_aset) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (ID_Produk_Hewan) REFERENCES produk_hewan(ID_produk) ON UPDATE CASCADE ON DELETE CASCADE
);

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
	subtotal INT NOT NULL,
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

CREATE TABLE DEKORASI_MEMILIKI_HISTORI_PENJUALAN (
	ID_Dekorasi VARCHAR(5),
	email VARCHAR(50),
	waktu_penjualan TIMESTAMP,
	jumlah INT NOT NULL,
	PRIMARY KEY (ID_Dekorasi, email, waktu_penjualan),
	FOREIGN KEY (ID_Dekorasi) REFERENCES dekorasi(ID_aset) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (email, waktu_penjualan) REFERENCES histori_penjualan(email, waktu_penjualan) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE OR REPLACE FUNCTION add_lumbung_dan_koleksi_aset()
RETURNS trigger AS
$$
BEGIN
INSERT INTO lumbung VALUES (NEW.email, 1, 0, 0);

INSERT INTO koleksi_aset VALUES (NEW.email);
RETURN NEW;
END;
$$
LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER trigger_add_lumbung_dan_koleksi_aset
AFTER INSERT ON pengguna
FOR EACH ROW
EXECUTE PROCEDURE add_lumbung_dan_koleksi_aset();

CREATE OR REPLACE FUNCTION histori_makanan()
RETURNS trigger AS
$$
DECLARE
ID_produk_bahan VARCHAR(5);
jumlah_bahan INT;
jumlah_produk INT;
xp_produksi INT;
jumlah_bahan_dimiliki INT;
ID_alat VARCHAR(5);
BEGIN
SELECT HP.jumlah, HP.xp INTO jumlah_produk, xp_produksi
FROM histori_produksi HP
WHERE HP.email=NEW.email AND HP.waktu_awal=NEW.waktu_awal;
-- RAISE NOTICE 'jumlah %, xp %', jumlah_produk, xp_produksi;

SELECT A.ID_aset INTO ID_alat
FROM produksi P
INNER JOIN koleksi_aset_memiliki_aset A
ON A.ID_aset = P.id_alat_produksi
WHERE A.id_koleksi_aset=NEW.email AND P.id_produk_makanan=NEW.ID_produk_makanan;
IF (ID_alat IS NOT NULL) THEN 
	FOR ID_produk_bahan, jumlah_bahan IN (SELECT id_produk, jumlah
					FROM produk_dibutuhkan_oleh_produk_makanan PPM
					WHERE id_produk_makanan=NEW.ID_produk_makanan)
	LOOP
		-- RAISE NOTICE 'Bahan: % Jumlah: %', ID_produk_bahan, jumlah_bahan;
		SELECT jumlah INTO jumlah_bahan_dimiliki
		FROM lumbung_memiliki_produk
		WHERE id_lumbung=NEW.email AND id_produk=ID_produk_bahan;
		
		-- RAISE NOTICE 'jumlah_bahan*jumlah_produk %', jumlah_bahan*jumlah_produk;
		IF (jumlah_bahan*jumlah_produk > COALESCE(jumlah_bahan_dimiliki, 0)) THEN
			DELETE FROM histori_produksi WHERE email=NEW.email AND waktu_awal=NEW.waktu_awal;
			-- RAISE EXCEPTION 'Error: Bahan kurang';
			RETURN NULL;
		ELSE
			-- RAISE NOTICE 'Bahan cukup';
			UPDATE lumbung_memiliki_produk
			SET jumlah = jumlah - jumlah_bahan*jumlah_produk
			WHERE id_lumbung=NEW.email AND id_produk=ID_produk_bahan;

			-- IF NEW.id_produk_makanan=(SELECT id_produk 
			-- 			FROM lumbung_memiliki_produk
			-- 			WHERE id_lumbung=NEW.email AND id_produk=NEW.id_produk_makanan)
			-- THEN
			-- 	UPDATE lumbung_memiliki_produk
			-- 	SET jumlah = jumlah + jumlah_produk
			-- 	WHERE id_lumbung=NEW.email AND id_produk=NEW.id_produk_makanan;
			-- ELSE
			-- 	INSERT INTO lumbung_memiliki_produk VALUES (NEW.email, NEW.id_produk_makanan, jumlah_produk);
			-- END IF;
		END IF;
	END LOOP;
ELSE
	DELETE FROM histori_produksi WHERE email=NEW.email AND waktu_awal=NEW.waktu_awal;
	RETURN NULL;
END IF;
RETURN NEW;
END;
$$
LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER trigger_add_histori_makanan
BEFORE INSERT ON histori_produksi_makanan
FOR EACH ROW
EXECUTE PROCEDURE histori_makanan();

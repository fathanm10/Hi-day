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

CREATE OR REPLACE FUNCTION pembelian_koin()
    RETURNS trigger AS
$$
DECLARE
    old_koin INTEGER;
    email_pengguna VARCHAR(50);
BEGIN
    SELECT coalesce (P.koin,0), TPK.email
    INTO old_koin, email_pengguna
    FROM PENGGUNA P, TRANSAKSI_PEMBELIAN_KOIN TPK
    WHERE NEW.email = TPK.email;

    UPDATE PENGGUNA
    SET koin = koin + NEW.paket_koin*NEW.jumlah
    WHERE NEW.email = email_pengguna;

    RETURN NEW;

END;
$$
    LANGUAGE plpgsql;

CREATE TRIGGER trigger_pembelian_koin
    AFTER INSERT ON transaksi_pembelian_koin
    FOR EACH ROW
EXECUTE PROCEDURE pembelian_koin();

CREATE OR REPLACE FUNCTION upgrade_lumbung()
    RETURNS trigger AS
$$
DECLARE
    old_koin INTEGER;
    email_pengguna VARCHAR(50);
BEGIN
    SELECT coalesce (P.koin,0), TUL.email
    INTO old_koin, email_pengguna
    FROM PENGGUNA P, TRANSAKSI_UPGRADE_LUMBUNG TUL
    WHERE NEW.email = TUL.email;

    IF old_koin < 200 THEN
        RETURN NULL;
    END IF;

    UPDATE PENGGUNA
    SET koin = koin - 200
    WHERE email = email_pengguna;

    RETURN NEW;
END;
$$
    LANGUAGE plpgsql;

CREATE TRIGGER trigger_upgrade_lumbung
    BEFORE INSERT ON transaksi_upgrade_lumbung
    FOR EACH ROW
EXECUTE PROCEDURE upgrade_lumbung();

CREATE OR REPLACE FUNCTION produksi_tanaman()
    RETURNS trigger AS
$$
DECLARE
    old_jumlah_bibit INTEGER;
    email_pengguna VARCHAR(50);
BEGIN
    SELECT HT.email
    INTO email_pengguna
    FROM HISTORI_TANAMAN HT
    WHERE NEW.email = HT.email;

    SELECT KAMA.jumlah
    INTO old_jumlah_bibit
    FROM KOLEKSI_ASET_MEMILIKI_ASET KAMA
    WHERE NEW.email = KAMA.id_koleksi_aset;

    UPDATE KOLEKSI_ASET_MEMILIKI_ASET
    SET jumlah = jumlah - NEW.jumlah
    WHERE NEW.email = id_koleksi_aset;

    UPDATE LUMBUNG_MEMILIKI_PRODUK
    SET jumlah = jumlah + NEW.jumlah
    WHERE id_lumbung = NEW.email;

    UPDATE PENGGUNA
    SET xp = xp+5*NEW.jumlah
    WHERE email = NEW.email;

    RETURN NEW;

END;
$$
    LANGUAGE plpgsql;

CREATE TRIGGER trigger_produksi_tanaman
    BEFORE INSERT ON histori_produksi
    FOR EACH ROW
EXECUTE PROCEDURE produksi_tanaman();

CREATE OR REPLACE FUNCTION UPDATE_KOLEKSI_ASET()
RETURNS TRIGGER AS
$$
DECLARE
TOTAL INTEGER;

BEGIN

SELECT COALESCE(JUMLAH, 0) INTO TOTAL
FROM KOLEKSI_ASET_MEMILIKI_ASET
WHERE ID_KOLEKSI_ASET = NEW.EMAIL AND ID_ASET = NEW.ID_ASET;

IF (TOTAL = 0) THEN
INSERT INTO KOLEKSI_ASET_MEMILIKI_ASET VALUES
(NEW.EMAIL, NEW.ID_ASET, TOTAL);
ELSE
UPDATE KOLEKSI_ASET_MEMILIKI_ASET
SET JUMLAH = JUMLAH + TOTAL
WHERE ID_KOLEKSI_ASET = NEW.EMAIL AND ID_ASET = NEW.ID_ASET;
END IF;
RETURN NEW;
END;

$$

LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION UPDATE_UANG_TRANSAKSI()
RETURNS TRIGGER AS
$$
DECLARE TOTAL_HARGA INTEGER;
DECLARE HARGA_SATUAN INTEGER;
DECLARE KOIN_SEKARANG INTEGER;
BEGIN
SELECT KOIN INTO KOIN_SEKARANG FROM PENGGUNA WHERE EMAIL=NEW.EMAIL;
SELECT HARGA_BELI INTO HARGA_SATUAN FROM ASET WHERE ID=NEW.ID_ASET;

TOTAL_HARGA = NEW.JUMLAH * HARGA_SATUAN;

IF (TOTAL_HARGA > KOIN_SEKARANG) THEN
RAISE EXCEPTION 'TOTAL HARGA ADALAH %, ANDA HANYA MEMILIKI %', NEW.TOTAL_HARGA, KOIN_SEKARANG;
ELSE
UPDATE PENGGUNA SET KOIN = KOIN_SEKARANG - TOTAL_HARGA WHERE EMAIL = NEW.EMAIL;
END IF;
RETURN NEW;
END;
$$
LANGUAGE plpgsql;


create trigger update_koin_beli_aset BEFORE INSERT ON transaksi_pembelian FOR EACH ROW EXECUTE procedure update_uang_transaksi();
create trigger update_koleksi AFTER INSERT ON transaksi_pembelian FOR EACH ROW EXECUTE procedure update_koleksi_aset();

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
		SELECT jumlah INTO jumlah_bahan_dimiliki
		FROM lumbung_memiliki_produk
		WHERE id_lumbung=NEW.email AND id_produk=ID_produk_bahan;
		
		IF (jumlah_bahan*jumlah_produk > COALESCE(jumlah_bahan_dimiliki, 0)) THEN
			DELETE FROM histori_produksi WHERE email=NEW.email AND waktu_awal=NEW.waktu_awal;
			RETURN NULL;
		ELSE
			UPDATE lumbung_memiliki_produk
			SET jumlah = jumlah - jumlah_bahan*jumlah_produk
			WHERE id_lumbung=NEW.email AND id_produk=ID_produk_bahan;

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

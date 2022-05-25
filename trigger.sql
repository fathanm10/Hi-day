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
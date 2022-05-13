INSERT INTO akun VALUES
    ('admin@admin.com'),
    ('pengguna@pengguna.com');

INSERT INTO admin VALUES 
    ('admin@admin.com', '1234567890');

INSERT INTO pengguna VALUES 
    ('pengguna@pengguna.com', '1234567890', 'Heavenly');

INSERT INTO level VALUES
    (1.0,0.0),
    (2.0,100.0),
    (3.0,200.0),
    (4.0,300.0),
    (5.0,400.0),
    (6.0,500.0),
    (7.0,600.0),
    (8.0,700.0),
    (9.0,800.0),
    (10.0,900.0);

INSERT INTO lumbung VALUES ('pengguna@pengguna.com', 1, 50, 2);

INSERT INTO paket_koin VALUES
    (100.0,15000.0),
    (500.0,60000.0),
    (1000.0,100000.0);

INSERT INTO aset VALUES
    ('bt01','Padi',1.0,1.0),
    ('bt02','Jagung',2.0,2.0),
    ('bt03','Tebu',3.0,3.0),
    ('bt04','Wortel',3.0,4.0),
    ('bt05','Stroberi',4.0,5.0),
    ('ps01','Petak Sawah Padi',1.0,2.0),
    ('ps02','Petak Sawah Jagung',2.0,4.0),
    ('ps03','Petak Sawah Tebu',3.0,6.0),
    ('ps04','Petak Sawah Wortel',3.0,8.0),
    ('ps05','Petak Sawah Stroberi',4.0,10.0),
    ('h01','Ayam',2.0,20.0),
    ('h02','Sapi',3.0,100.0),
    ('h03','Domba',4.0,50.0),
    ('k01','Kandang Ayam',2.0,40.0),
    ('k02','Kandang Sapi',3.0,100.0),
    ('k03','Kandang Domba',4.0,100.0),
    ('d01','Pohon',2.0,4.0),
    ('d02','Rumput',2.0,4.0),
    ('d03','Bunga',3.0,6.0),
    ('d04','Pagar',3.0,8.0),
    ('d05','Foothpath',4.0,2.0),
    ('ap01','Sugar mill',3.0,100.0),
    ('ap02','Rice mill',4.0,200.0),
    ('ap03','Dairy',5.0,400.0),
    ('ap04','Oven',4.0,350.0);

INSERT INTO dekorasi VALUES
    ('d01',2.0),
    ('d02',2.0),
    ('d03',3.0),
    ('d04',4.0),
    ('d05',1.0);

INSERT INTO bibit_tanaman VALUES
    ('bt01','00:01:00'),
    ('bt02','00:02:00'),
    ('bt03','00:02:00'),
    ('bt04','00:03:00'),
    ('bt05','00:05:00');

INSERT INTO kandang VALUES
    ('k01',3.0,'Ayam'),
    ('k02',3.0,'Sapi'),
    ('k03',3.0,'Domba');

INSERT INTO hewan VALUES
    ('h01','00:03:00','k01'),
    ('h02','00:05:00','k02'),
    ('h03','00:10:00','k03');

INSERT INTO alat_produksi VALUES
    ('ap01',3.0),
    ('ap02',3.0),
    ('ap03',3.0),
    ('ap04',1.0);

INSERT INTO petak_sawah VALUES
    ('ps01','Padi'),
    ('ps02','Jagung'),
    ('ps03','Tebu'),
    ('ps04','Wortel'),
    ('ps05','Stroberi');

INSERT INTO produk VALUES
    ('HP1','Padi',3.0,'raw material'),
    ('HP2','Jagung',4.0,'raw material'),
    ('HP3','Tebu',5.0,'raw material'),
    ('HP4','Stroberi',7.0,'finished good'),
    ('PH1','Telur',8.0,'raw material'),
    ('PH2','Susu Sapi',20.0,'raw material'),
    ('PH3','Susu Domba',25.0,'raw material'),
    ('HP5','wortel',21.0,'raw material'),
    ('PM1','Gula Pasir',18.0,'semi finished goods'),
    ('PM2','Tepung',12.0,'semi finished goods'),
    ('PM3','Cheese Cake',10.0,'finished good'),
    ('PM4','Pie Stroberi',4.0,'finished good'),
    ('PM5','Yoghurt',2.0,'finished good'),
    ('PM6','Keju',8.0,'semi finished goods');

INSERT INTO produk_hewan VALUES
    ('PH1'),
    ('PH2'),
    ('PH3');

INSERT INTO hasil_panen VALUES
    ('HP1'),
    ('HP2'),
    ('HP3'),
    ('HP4'),
    ('HP5');

INSERT INTO produk_makanan VALUES
    ('PM1'),
    ('PM2'),
    ('PM3'),
    ('PM4'),
    ('PM5'),
    ('PM6');

INSERT INTO akun VALUES
    ('email1@email.com'),
    ('email2@email.com'),
    ('email3@email.com'),
    ('email4@email.com'),
    ('email5@email.com'),
    ('email6@email.com'),
    ('email7@email.com'),
    ('email8@email.com'),
    ('email9@email.com'),
    ('email10@email.com'),
    ('email11@email.com'),
    ('email12@email.com'),
    ('email13@email.com'),
    ('email14@email.com'),
    ('email15@email.com'),
    ('email16@email.com'),
    ('email17@email.com'),
    ('email18@email.com'),
    ('email19@email.com'),
    ('email20@email.com'),
    ('email21@email.com'),
    ('email22@email.com'),
    ('email23@email.com'),
    ('email24@email.com'),
    ('email25@email.com'),
    ('email26@email.com'),
    ('email27@email.com'),
    ('email28@email.com'),
    ('email29@email.com'),
    ('email30@email.com');

INSERT INTO admin
VALUES
    ('email1@email.com', 'email12345'),
    ('email2@email.com', 'email23456'),
    ('email3@email.com', 'email34567'),
    ('email4@email.com', 'email45678'),
    ('email5@email.com', 'email56789');

INSERT INTO pengguna VALUES
    ('email6@email.com','emailemail','Malaysia',68.0,500.0,1.0),
    ('email7@email.com','emailemail','Denmark',78.0,1883.0,1.0),
    ('email8@email.com','emailemail','Brazil',112.0,2111.0,2.0),
    ('email9@email.com','emailemail','Ukraine',189.0,2497.0,2.0),
    ('email10@email.com','emailemail','China',252.0,986.0,3.0),
    ('email11@email.com','emailemail','Nigeria',301.0,933.0,4.0),
    ('email12@email.com','emailemail','Chile',341.0,3420.0,4.0),
    ('email13@email.com','emailemail','Cuba',424.0,1464.0,5.0),
    ('email14@email.com','emailemail','Azerbaijan',473.0,2543.0,5.0),
    ('email15@email.com','emailemail','China',581.0,3934.0,6.0),
    ('email16@email.com','emailemail','France',610.0,4626.0,7.0),
    ('email17@email.com','emailemail','Russia',732.0,2616.0,8.0),
    ('email18@email.com','emailemail','Serbia',797.0,2360.0,8.0),
    ('email19@email.com','emailemail','Indonesia',890.0,3978.0,9.0),
    ('email20@email.com','emailemail','Cuba',910.0,4564.0,10.0),
    ('email21@email.com','emailemail','CfUoHBbZgH',0.0,11.0,1.0),
    ('email22@email.com','emailemail','fQNTPbfHjy',0.0,11.0,1.0),
    ('email23@email.com','emailemail','UHYfVwmexK',0.0,11.0,1.0),
    ('email24@email.com','emailemail','ZIrnijFzZX',0.0,11.0,1.0),
    ('email25@email.com','emailemail','mpsDevGhYX',0.0,11.0,1.0),
    ('email26@email.com','emailemail','hcdsJtfTJd',0.0,11.0,1.0),
    ('email27@email.com','emailemail','berzYAFaki',0.0,11.0,1.0),
    ('email28@email.com','emailemail','uRbXetZFXI',0.0,11.0,1.0),
    ('email29@email.com','emailemail','KWdVJAutbq',0.0,11.0,1.0),
    ('email30@email.com','emailemail','lthPYEOlDW',0.0,11.0,1.0);

INSERT INTO paket_koin
VALUES
    (100, 15000),
    (500, 60000);

INSERT INTO transaksi_pembelian_koin VALUES
    ('email6@email.com','2022-10-05 10:10:37',1.0,'transfer bank',100.0,15000),
    ('email7@email.com','2022-10-05 09:11:44',1.0,'transfer bank',100.0,15000),
    ('email8@email.com','2022-10-05 09:10:37',2.0,'transfer bank',100.0,30000),
    ('email9@email.com','2022-10-05 09:12:37',2.0,'transfer bank',100.0,30000),
    ('email10@email.com','2022-10-05 08:16:01',2.0,'gopay',100.0,30000),
    ('email11@email.com','2022-10-05 10:11:17',2.0,'gopay',100.0,30000),
    ('email12@email.com','2022-10-05 10:03:17',3.0,'gopay',100.0,45000),
    ('email13@email.com','2022-10-05 10:04:17',3.0,'gopay',100.0,45000),
    ('email14@email.com','2022-10-05 10:05:17',3.0,'gopay',100.0,45000),
    ('email15@email.com','2022-10-05 10:06:17',3.0,'gopay',100.0,45000),
    ('email16@email.com','2022-10-05 10:07:17',3.0,'gopay',100.0,45000),
    ('email17@email.com','2022-10-05 10:08:17',1.0,'gopay',500.0,60000),
    ('email18@email.com','2022-10-05 10:09:17',2.0,'ovo',500.0,120000),
    ('email19@email.com','2022-10-05 10:10:17',2.0,'ovo',500.0,120000),
    ('email20@email.com','2022-10-05 10:11:17',3.0,'ovo',500.0,180000),
    ('email21@email.com','2022-10-05 10:12:17',4.0,'ovo',500.0,240000),
    ('email22@email.com','2022-10-05 10:13:17',4.0,'ovo',500.0,240000),
    ('email23@email.com','2022-10-05 10:14:17',1.0,'ovo',1000.0,100000),
    ('email24@email.com','2022-10-05 10:15:17',2.0,'ovo',1000.0,200000),
    ('email25@email.com','2022-10-05 10:16:17',3.0,'ovo',1000.0,300000);

INSERT INTO lumbung VALUES
    ('email6@email.com',1.0,50.0,22.0),
    ('email7@email.com',1.0,50,38.0),
    ('email8@email.com',2.0,100,18.0),
    ('email9@email.com',2.0,100,64.0),
    ('email10@email.com',2.0,100,82.0),
    ('email11@email.com',2.0,100,10.0),
    ('email12@email.com',3.0,150,44.0),
    ('email13@email.com',3.0,150,88.0),
    ('email14@email.com',3.0,150,123.0),
    ('email15@email.com',3.0,150,137.0),
    ('email16@email.com',3.0,150,144.0),
    ('email17@email.com',3.0,150,95.0),
    ('email18@email.com',4.0,200,142.0),
    ('email19@email.com',4.0,200,169.0),
    ('email20@email.com',4.0,200,177.0);

INSERT INTO transaksi_upgrade_lumbung VALUES
    ('email9@email.com','2022-11-05 10:24:39'),
    ('email10@email.com','2022-11-05 13:09:19'),
    ('email11@email.com','2022-11-05 11:27:05'),
    ('email12@email.com','2022-11-05 13:54:43'),
    ('email13@email.com','2022-11-05 10:24:45'),
    ('email14@email.com','2022-11-05 11:30:14'),
    ('email15@email.com','2022-11-05 13:09:07'),
    ('email16@email.com','2022-11-05 11:27:40'),
    ('email17@email.com','2022-11-05 13:54:33'),
    ('email18@email.com','2022-11-05 10:24:57'),
    ('email19@email.com','2022-11-05 13:54:51'),
    ('email20@email.com','2022-11-05 11:27:50'),
    ('email12@email.com','2022-11-05 13:59:08'),
    ('email13@email.com','2022-11-05 10:25:02'),
    ('email14@email.com','2022-11-05 13:09:33'),
    ('email15@email.com','2022-11-05 13:59:14'),
    ('email16@email.com','2022-11-05 10:25:08'),
    ('email17@email.com','2022-11-05 13:10:40'),
    ('email18@email.com','2022-11-05 14:00:21'),
    ('email19@email.com','2022-11-05 10:25:19'),
    ('email20@email.com','2022-11-05 11:22:33'),
    ('email18@email.com','2022-11-05 12:59:27'),
    ('email19@email.com','2022-11-05 12:27:19'),
    ('email20@email.com','2022-11-05 13:29:29');

INSERT INTO koleksi_aset
VALUES
    ('email6@email.com'),
    ('email7@email.com'),
    ('email8@email.com'),
    ('email9@email.com'),
    ('email10@email.com'),
    ('email11@email.com'),
    ('email12@email.com'),
    ('email13@email.com'),
    ('email14@email.com'),
    ('email15@email.com'),
    ('email16@email.com'),
    ('email17@email.com'),
    ('email18@email.com'),
    ('email19@email.com'),
    ('email20@email.com');

INSERT INTO koleksi_aset_memiliki_aset VALUES
    ('email6@email.com','ps04',3.0),
    ('email6@email.com','ap03',11.0),
    ('email6@email.com','ap04',11.0),
    ('email7@email.com','bt04',15.0),
    ('email7@email.com','d03',10.0),
    ('email8@email.com','bt02',3.0),
    ('email8@email.com','d01',5.0),
    ('email9@email.com','h01',5.0),
    ('email9@email.com','bt01',9.0),
    ('email9@email.com','h02',13.0),
    ('email10@email.com','h02',11.0),
    ('email10@email.com','bt02',8.0),
    ('email10@email.com','k01',14.0),
    ('email11@email.com','bt01',15.0),
    ('email11@email.com','k03',13.0),
    ('email12@email.com','ps05',13.0),
    ('email12@email.com','ap04',5.0),
    ('email12@email.com','h02',9.0),
    ('email13@email.com','ps02',14.0),
    ('email13@email.com','ap01',8.0),
    ('email13@email.com','ap02',9.0),
    ('email14@email.com','ps01',14.0),
    ('email14@email.com','d05',14.0),
    ('email14@email.com','ap01',11.0),
    ('email15@email.com','k02',6.0),
    ('email15@email.com','bt05',12.0),
    ('email15@email.com','d01',5.0),
    ('email16@email.com','ps03',3.0),
    ('email16@email.com','ap02',8.0),
    ('email16@email.com','ap03',3.0),
    ('email17@email.com','k01',7.0),
    ('email17@email.com','bt04',5.0),
    ('email17@email.com','k03',15.0),
    ('email18@email.com','bt05',13.0),
    ('email18@email.com','d04',3.0),
    ('email19@email.com','h03',14.0),
    ('email19@email.com','bt03',12.0),
    ('email19@email.com','k02',10.0),
    ('email20@email.com','bt03',14.0),
    ('email20@email.com','d02',14.0);

INSERT INTO transaksi_pembelian VALUES
    ('email6@email.com','2022-11-05 08:06:31',3.0,'ps04'),
    ('email6@email.com','2022-10-05 09:12:37',11.0,'ap03'),
    ('email7@email.com','2022-11-05 08:20:48',15.0,'bt04'),
    ('email7@email.com','2022-10-05 10:06:37',10.0,'d03'),
    ('email8@email.com','2022-11-05 10:05:47',3.0,'bt02'),
    ('email8@email.com','2022-10-05 09:10:37',5.0,'d01'),
    ('email9@email.com','2022-11-05 01:26:47',5.0,'h01'),
    ('email9@email.com','2022-10-05 10:11:17',9.0,'bt01'),
    ('email10@email.com','2022-11-05 09:31:06',11.0,'h02'),
    ('email10@email.com','2022-10-05 10:03:17',8.0,'bt02'),
    ('email11@email.com','2022-11-05 10:10:37',15.0,'bt01'),
    ('email11@email.com','2022-10-05 10:05:47',13.0,'k03'),
    ('email12@email.com','2022-11-05 11:24:52',13.0,'ps05'),
    ('email12@email.com','2022-10-05 08:16:01',5.0,'ap04'),
    ('email13@email.com','2022-11-05 11:25:23',14.0,'ps02'),
    ('email13@email.com','2022-10-05 09:11:44',8.0,'ap01'),
    ('email14@email.com','2022-11-05 01:15:15',14.0,'ps01'),
    ('email14@email.com','2022-10-05 10:10:37',14.0,'d05'),
    ('email15@email.com','2022-11-05 08:06:19',6.0,'k02'),
    ('email15@email.com','2022-10-05 10:06:17',12.0,'bt05'),
    ('email16@email.com','2022-11-05 08:21:05',3.0,'ps03'),
    ('email16@email.com','2022-10-05 09:10:37',8.0,'ap02'),
    ('email17@email.com','2022-11-05 01:30:22',7.0,'k01'),
    ('email17@email.com','2022-10-05 10:05:17',5.0,'bt04'),
    ('email18@email.com','2022-11-05 09:30:49',13.0,'bt05'),
    ('email18@email.com','2022-10-05 10:30:49',3.0,'d04'),
    ('email19@email.com','2022-11-05 11:25:16',14.0,'h03'),
    ('email19@email.com','2022-10-05 10:04:17',12.0,'bt03'),
    ('email20@email.com','2022-11-05 11:25:05',14.0,'bt03'),
    ('email20@email.com','2022-10-05 10:10:37',14.0,'d02');

INSERT INTO produk_dibutuhkan_oleh_produk_makanan VALUES
    ('PM1','HP1',12.0),
    ('PM2','HP2',4.0),
    ('PM3','HP3',5.0),
    ('PM4','HP4',2.0),
    ('PM5','PH1',7.0),
    ('PM6','PH2',5.0);

INSERT INTO lumbung_memiliki_produk VALUES
    ('email6@email.com','HP1',4.0),
    ('email7@email.com','HP2',2.0),
    ('email8@email.com','HP3',7.0),
    ('email9@email.com','HP4',3.0),
    ('email10@email.com','PH1',14.0),
    ('email11@email.com','PH2',2.0),
    ('email12@email.com','PH3',7.0),
    ('email13@email.com','HP5',2.0),
    ('email14@email.com','PM1',4.0),
    ('email15@email.com','PM2',2.0),
    ('email16@email.com','PM3',7.0),
    ('email17@email.com','PM4',9.0),
    ('email18@email.com','PM5',3.0),
    ('email19@email.com','PM6',10.0);

INSERT INTO produksi VALUES
    ('ap01','PM1','10:21:15',4.0),
    ('ap02','PM2','10:34:44',3.0),
    ('ap03','PM3','11:23:42',4.0),
    ('ap04','PM4','13:44:51',2.0),
    ('ap01','PM5','13:45:11',7.0),
    ('ap03','PM6','13:12:16',1.0);

SELECT PM.nama AS produk, A.nama AS alat, P.durasi, P.jumlah_hasil_unit
FROM produksi AS P
INNER JOIN aset AS A
ON A.ID = P.ID_alat_produksi
INNER JOIN produk AS PM
ON PM.ID = P.ID_produk_makanan
WHERE P.ID_produk_makanan='ap02' AND P.ID_alat_produksi='PM2';

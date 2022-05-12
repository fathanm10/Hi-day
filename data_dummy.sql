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
    ('p1264','Padi',3.0,'raw material'),
    ('p6532','Jagung',4.0,'raw material'),
    ('d7y53','Tebu',5.0,'raw material'),
    ('ji83','Stroberi',7.0,'finished good'),
    ('b683','Telur',8.0,'raw material'),
    ('s892','Susu Sapi',20.0,'raw material'),
    ('hu82','Susu Domba',25.0,'raw material'),
    ('g632d','wortel',21.0,'raw material'),
    ('97ebf','Gula Pasir',18.0,'semi finished goods'),
    ('hu28','Tepung',12.0,'semi finished goods'),
    ('hy231','Cheese Cake',10.0,'finished good'),
    ('hdy88','Pie Stroberi',4.0,'finished good'),
    ('gd6s','Yoghurt',2.0,'finished good'),
    ('6ys5','Keju',8.0,'semi finished goods');

INSERT INTO produk_hewan VALUES
    ('b683'),
    ('s892'),
    ('hu82');

INSERT INTO hasil_panen VALUES
    ('p1264'),
    ('p6532'),
    ('d7y53'),
    ('ji83'),
    ('g632d');

INSERT INTO produk_makanan VALUES
    ('97ebf'),
    ('hu28'),
    ('hy231'),
    ('hdy88'),
    ('gd6s'),
    ('6ys5');
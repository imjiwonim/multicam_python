-- table 생성 
CREATE TABLE TopGainerStockList(
	no int not null PRIMARY KEY,
    name VARCHAR(255),
    percent_change VARCHAR(255),
    last_price VARCHAR(20),
    high_price VARCHAR(20),
    low_price VARCHAR(20),
    volume VARCHAR(20)
);

-- 컬럼 수정 
ALTER TABLE TopGainerStockList
MODIFY COLUMN last_price FLOAT,
MODIFY COLUMN high_price FLOAT,
MODIFY COLUMN low_price FLOAT;

-- 테이블 확인 
DESCRIBE TopGainerStockList;

ALTER TABLE TopGainerStockList
MODIFY COLUMN percent_change VARCHAR(255);

-- 버전 확인 
SELECT VERSION();

-- 데이터 추가
INSERT INTO TopGainerStockList(no, name, percent_change, last_price, high_price, low_price, volume)
VALUES(1, 'Agrify Corp(AGFY)', '1,315.16', 47.62, 54.25, 40.0, '774.43K'),
(2, 'BTC Digital(BTCT)', '848.86', 16.7, 17.4, 15.6, '1.58M'),
(3, 'Exicure Inc(XCUR)', '675.53', 18.38, 19.62, 12.64, '4.59M'),
(4, 'Quantum Computing Inc(QUBT)', '459.63', 6.1, 6.4, 4.51, '98.81M'),
(5, 'M(Mercurity Fintech Holding Inc(MFH)', '299.20', 4.99, 5.22, 4.07, '253.18K'),
(6, 'Advent Technologies Holdng Inc(ADN)', '282.20', 7.3, 7.9, 6.82, '130.91K'),
(7, 'FOXO TECHNOLOGIES(FOXO)', '253.22', 0.54, 0.57, 0.51, '2.33M'),
(8, 'Simpple Ltd(SPPL)', '252.94', 1.2, 1.3, 1.13, '533.41K'),
(9, 'D(Destiny Tech100(DXYZ)', '250.04', 41.97, 46.2, 38.3, '3.55M'),
(10, 'Forte Biosciences Inc(FBRX)', '241.99', 16.0, 16.67, 14.04, '396.66K'),
(11, 'Red Cat Hldgs Inc(RCAT)', '233.46', 8.97, 9.6, 7.6, '17.75M'),
(12, 'M(Microvast Holdings Inc(MVST)', '211.80', 0.67, 0.71, 0.61, '17.21M'),
(13, 'Pulmatrix(PULM)', '202.99', 6.12, 6.58, 5.96, '119.03K'),
(14, 'B(Btcs Inc(BTCS)', '200.85', 3.55, 3.77, 3.4, '1.46M'),
(15, 'Root, Inc.(ROOT)', '188.89', 109.23, 109.39, 101.52, '548.67K'),
(16, 'CERo Therapeutics(CERO)', '183.25', 0.22, 0.25, 0.21, '9.80M'),
(17, 'D(D Wave Quantum(QBTS)', '181.73', 2.93, 3.0, 1.97, '84.84M'),
(18, 'U(Unusual Machines(UMAC)', '173.29', 4.4, 5.21, 3.88, '461.87K'),
(19, 'Bakkt Holdings Inc(BKKT)', '172.14', 29.31, 31.17, 28.26, '1.59M'),
(20, 'Bloom Energy(BE)', '171.16', 25.76, 26.26, 23.61, '10.58M'),
(21, 'Kingsoft Cloud Holdings Ltd(KC)', '171.05', 7.21, 7.24, 6.11, '7.78M'),
(22, 'Porch Group Inc(PRCH)', '169.53', 3.45, 3.72, 3.43, '3.08M'),
(23, 'Lemonade Inc(LMND)', '167.39', 49.28, 51.67, 47.15, '4.44M'),
(24, 'Omeros(OMER)', '160.38', 10.91, 10.99, 7.46, '4.07M'),
(25, 'S&W Seed Co(SANW)', '157.65', 6.57, 7.27, 5.25, '163.31K'),
(26, 'Cerence Inc(CRNC)', '146.58', 7.2, 7.6, 5.71, '17.43M'),
(27, 'Safe Pro Group Inc.(SPAI)', '144.39', 4.57, 4.66, 3.78, '1.35M'),
(28, 'Freyr Battery(FREY)', '140.20', 2.45, 2.63, 2.41, '3.67M'),
(29, 'Aligos Therapeutics, Inc.(ALGS)', '138.57', 20.04, 20.44, 18.75, '437.71K'),
(30, 'Autozi Internet Technology (Global) Ltd.(AZI)', '135.90', 1.84, 2.04, 1.8, '1.60M'),
(31, 'Thredup Inc.(TDUP)', '135.45', 1.55, 1.58, 1.3, '1.37M'),
(32, 'Semler Scientific Inc(SMLR)', '132.13', 63.65, 67.82, 60.35, '1.36M'),
(33, 'BioSig Technologies Inc(BSGM)', '130.28', 2.0, 2.02, 1.79, '231.78K'),
(34, 'Honest Company, Inc.(HNST)', '127.65', 8.15, 8.29, 7.61, '5.77M'),
(35, 'Aclaris Therapeutics Inc(ACRS)', '124.85', 3.8, 4.44, 3.8, '2.99M'),
(36, 'DAVE INC(DAVE)', '122.66', 86.26, 89.98, 83.0, '600.81K'),
(37, 'The Arena Group Holdings(AREN)', '121.43', 1.55, 1.73, 1.45, '429.20K'),
(38, 'Innodata(INOD)', '120.54', 44.77, 48.25, 44.66, '2.36M'),
(39, 'S(Sezzle Inc.(SEZL)', '117.87', 463.98, 477.53, 437.25, '113.57K'),
(40, 'Applied Optoelec(AAOI)', '117.83', 37.99, 38.94, 35.17, '4.94M'),
(41, 'Quantum-Si Incorporated(QSI)', '117.45', 1.62, 1.71, 1.17, '27.33M'),
(42, 'Chromadex Corp(CDXC)', '114.41', 7.44, 7.52, 7.09, '1.10M'),
(43, 'Inotiv Inc(NOTV)', '109.94', 3.59, 3.82, 3.3, '590.52K'),
(44, 'N(Next Technology(NXTT)', '108.70', 2.4, 2.5, 2.18, '196.75K'),
(45, 'Rocket Lab Usa Inc(RKLB)', '108.05', 23.26, 23.81, 22.38, '28.38M'),
(46, 'Applovin Corp(APP)', '106.22', 333.31, 335.39, 303.5, '6.88M'),
(47, 'PALLADYNE AI CORP(PDYN)', '105.36', 4.6, 5.05, 2.15, '83.07M'),
(48, 'Paragon 28 Inc(FNA)', '105.32', 10.04, 10.71, 9.9, '909.82K'),
(49, 'Trilogy Metals(TMQ)', '104.55', 1.33, 1.4, 1.29, '579.32K'),
(50, 'Canaan Inc.(CAN)', '102.86', 1.97, 1.99, 1.71, '19.14M');

-- 데이터 확인
SELECT *
FROM TopGAINERSTOCKLIST;
DROP DATABASE gastrocrm_db;
CREATE SCHEMA gastrocrm_db;
USE gastrocrm_db;

CREATE TABLE `zamowienie` (
    `id` int AUTO_INCREMENT NOT NULL ,
    -- increment
    `klientId` int  NOT NULL ,
    `zamowienieWynos` boolean  NOT NULL ,
    `kelnderId` int  NOT NULL ,
    `dataZamowienia` datetime  NOT NULL ,
    `status` text  NOT NULL ,
    `faktura` boolean  NOT NULL ,
    PRIMARY KEY (
        `id`
    )
);

CREATE TABLE `zamowienie_produkty` (
    `id` int AUTO_INCREMENT NOT NULL ,
    `zamowienieId` int  NOT NULL ,
    `idPotrawy` int  NOT NULL ,
    `iloscPotrawy` int  NOT NULL ,
    `sumarycznaWartoscPotrawy` float  NOT NULL ,
    PRIMARY KEY (
        `id`
    )
);

CREATE TABLE `platnosc` (
    `zamowienieId` int  NOT NULL ,
    `dataPlatnosci` date  NOT NULL ,
    `wartoscZamowienia` float  NOT NULL ,
    `typPlatnosciId` text  NOT NULL 
);

CREATE TABLE `przerwa_kelnerska` (
    `id` int AUTO_INCREMENT NOT NULL ,
    `idCzasPracy` int  NOT NULL ,
    `startPrzerwy` datetime  NULL ,
    `koniecPrzerwy` datetime  NULL ,
    PRIMARY KEY (
        `id`
    )
);

CREATE TABLE `czas_pracy` (
    `id` int AUTO_INCREMENT NOT NULL ,
    `idKelnera` int  NOT NULL ,
    `czasStartu` datetime  NULL ,
    `czasKonca` datetime  NULL ,
    PRIMARY KEY (
        `id`
    )
);

CREATE TABLE `grafik_pracy` (
    `id` int AUTO_INCREMENT NOT NULL ,
    `idPracownika` int  NOT NULL ,
    `czasStartu` datetime  NULL ,
    `czasKonca` datetime  NULL ,
    PRIMARY KEY (
        `id`
    )
);

CREATE TABLE `menu` (
    `id` int AUTO_INCREMENT NOT NULL ,
    `tytul` text  NOT NULL ,
    `aktywne` boolean  NOT NULL ,
    `menuOd` date  NULL ,
    `menuDo` date  NULL ,
    -- danie dnia
    `idPotrawyDnia` int  NULL ,
    `idMenuListy` int  NOT NULL ,
    PRIMARY KEY (
        `id`
    )
);

CREATE TABLE `menu_lista` (
    `id` int AUTO_INCREMENT NOT NULL ,
    `numerPotrawyWMenu` int  NOT NULL ,
    `potrawaWMenu` int  NOT NULL ,
    PRIMARY KEY (
        `id`
    )
);

CREATE TABLE `potrawy` (
    `id` int AUTO_INCREMENT NOT NULL ,
    `idAlegenu` int  NOT NULL ,
    `name` varchar(200)  NOT NULL ,
    `cena` float  NOT NULL ,
    -- Czy makaron,zupa, etc...
    `kategoriaPotrawy` text  NOT NULL ,
    PRIMARY KEY (
        `id`
    ),
    UNIQUE (`name`)
);

CREATE TABLE `alergeny` (
    `id` int AUTO_INCREMENT NOT NULL ,
    `vegan` boolean  NOT NULL ,
    `wegetarian` boolean  NOT NULL ,
    `gluten` boolean  NOT NULL ,
    `laktoza` boolean  NOT NULL ,
    `orzechy` boolean  NOT NULL ,
    PRIMARY KEY (
        `id`
    )
);

CREATE TABLE `uzytkownik` (
    `id` int AUTO_INCREMENT NOT NULL ,
    -- Kelner/Szef
    `nazwaUzytkownika` text  NOT NULL ,
    `haslo` text  NOT NULL ,
    `imie` text  NOT NULL ,
    `nazwisko` text  NOT NULL ,
    `telefon` varchar(12)  NOT NULL ,
    `email` text  NOT NULL ,
    `uprawnienia` text  NOT NULL ,
    `tempHaslo` boolean  NOT NULL DEFAULT 1 ,
    PRIMARY KEY (
        `id`
    )
);

ALTER TABLE `zamowienie` ADD CONSTRAINT `fk_zamowienie_kelnderId` FOREIGN KEY(`kelnderId`)
REFERENCES `uzytkownik` (`id`);

ALTER TABLE `zamowienie_produkty` ADD CONSTRAINT `fk_zamowienieProdukty_zamowienieId` FOREIGN KEY(`zamowienieId`)
REFERENCES `zamowienie` (`id`);

ALTER TABLE `zamowienie_produkty` ADD CONSTRAINT `fk_zamowienieProdukty_idPotrawy` FOREIGN KEY(`idPotrawy`)
REFERENCES `potrawy` (`id`);

ALTER TABLE `platnosc` ADD CONSTRAINT `fk_platnosc_zamowienieId` FOREIGN KEY(`zamowienieId`)
REFERENCES `zamowienie` (`id`);

ALTER TABLE `przerwa_kelnerska` ADD CONSTRAINT `fk_przerwaKelnerska_idCzasPracy` FOREIGN KEY(`idCzasPracy`)
REFERENCES `czasPracy` (`id`);

ALTER TABLE `czas_pracy` ADD CONSTRAINT `fk_czasPracy_idKelnera` FOREIGN KEY(`idKelnera`)
REFERENCES `uzytkownik` (`id`);

ALTER TABLE `grafik_pracy` ADD CONSTRAINT `fk_grafikPracy_idPracownika` FOREIGN KEY(`idPracownika`)
REFERENCES `uzytkownik` (`id`);

ALTER TABLE `menu` ADD CONSTRAINT `fk_menu_idMenuListy` FOREIGN KEY(`idMenuListy`)
REFERENCES `menuLista` (`id`);

ALTER TABLE `menu_lista` ADD CONSTRAINT `fk_menuLista_potrawaWMenu` FOREIGN KEY(`potrawaWMenu`)
REFERENCES `potrawy` (`id`);

ALTER TABLE `potrawy` ADD CONSTRAINT `fk_potrawy_idAlegenu` FOREIGN KEY(`idAlegenu`)
REFERENCES `alergeny` (`id`);

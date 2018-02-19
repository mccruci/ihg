BEGIN;
--
-- Create model Edificio
--
CREATE TABLE `xetal_edificio` (`dfc_cod` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `dfc_nome` varchar(100) NOT NULL, `dfc_indirizzo` varchar(100) NOT NULL);
--
-- Create model Letto
--
CREATE TABLE `xetal_letto` (`ltt_cod` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `ltt_num` integer NOT NULL);
--
-- Create model Piano
--
CREATE TABLE `xetal_piano` (`pno_cod` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `pno_numero` integer NOT NULL, `pno_dfc_cod_id` integer NOT NULL);
--
-- Create model Reparto
--
CREATE TABLE `xetal_reparto` (`rpt_cod` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `rpt_nome` varchar(100) NOT NULL, `rpt_spd_cod_id` integer NOT NULL);
--
-- Create model Sito
--
CREATE TABLE `xetal_sito` (`sit_cod` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `sit_denominazione` varchar(100) NOT NULL, `sit_ospedale` varchar(100) NOT NULL, `sit_indirizzo` varchar(100) NOT NULL);
--
-- Create model Stanza
--
CREATE TABLE `xetal_stanza` (`stz_cod` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `stz_numero` integer NOT NULL, `stz_uso` varchar(1) NOT NULL, `stz_pno_cod_id` integer NOT NULL, `stz_rpt_cod_id` integer NOT NULL);
--
-- Add field ltt_stz_cod to letto
--
ALTER TABLE `xetal_letto` ADD COLUMN `ltt_stz_cod_id` integer NOT NULL;
--
-- Add field dfc_sit_cod to edificio
--
ALTER TABLE `xetal_edificio` ADD COLUMN `dfc_sit_cod_id` integer NOT NULL;
ALTER TABLE `xetal_piano` ADD CONSTRAINT `xetal_piano_pno_dfc_cod_id_ffcb3aee_fk_xetal_edificio_dfc_cod` FOREIGN KEY (`pno_dfc_cod_id`) REFERENCES `xetal_edificio` (`dfc_cod`);
ALTER TABLE `xetal_reparto` ADD CONSTRAINT `xetal_reparto_rpt_spd_cod_id_370dbf60_fk_xetal_piano_pno_cod` FOREIGN KEY (`rpt_spd_cod_id`) REFERENCES `xetal_piano` (`pno_cod`);
ALTER TABLE `xetal_stanza` ADD CONSTRAINT `xetal_stanza_stz_pno_cod_id_0f568818_fk_xetal_piano_pno_cod` FOREIGN KEY (`stz_pno_cod_id`) REFERENCES `xetal_piano` (`pno_cod`);
ALTER TABLE `xetal_stanza` ADD CONSTRAINT `xetal_stanza_stz_rpt_cod_id_8bd8c4e4_fk_xetal_reparto_rpt_cod` FOREIGN KEY (`stz_rpt_cod_id`) REFERENCES `xetal_reparto` (`rpt_cod`);
ALTER TABLE `xetal_letto` ADD CONSTRAINT `xetal_letto_ltt_stz_cod_id_54868e4d_fk_xetal_stanza_stz_cod` FOREIGN KEY (`ltt_stz_cod_id`) REFERENCES `xetal_stanza` (`stz_cod`);
ALTER TABLE `xetal_edificio` ADD CONSTRAINT `xetal_edificio_dfc_sit_cod_id_c72cb838_fk_xetal_sito_sit_cod` FOREIGN KEY (`dfc_sit_cod_id`) REFERENCES `xetal_sito` (`sit_cod`);
COMMIT;

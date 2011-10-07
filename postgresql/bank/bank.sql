-- Pere László: Linux felhasználói ismeretek II., Adatkezelés, Kiskapu,
-- Pécs, 2002

-- Bevihető a
-- psql -f bank.sql
-- paranccsal.

--
-- A relációk létrehozása
--

-- Ha már léteznek töröljük ezeket, hogy újra létrehozhassuk:
DROP VIEW betetesek;
DROP TABLE egyenleg;
DROP TABLE naplo;
DROP TABLE szemelyes_adatok;


CREATE TABLE szemelyes_adatok (
	nev	varchar(30) NOT NULL,
	cim	varchar(30) NOT NULL,
	szamlaszam integer PRIMARY KEY
);

CREATE TABLE egyenleg (
	szamlaszam integer REFERENCES szemelyes_adatok,
	egyenleg   integer DEFAULT 0
       			CONSTRAINT eladósodott
			CHECK ( EGYENLEG >= -20000 )
);


CREATE TABLE naplo (
	szamlaszam integer REFERENCES szemelyes_adatok(szamlaszam),
	penzmozgas integer,
        idopont timestamp
);

--
--
-- Új betétes létrehozása nulla egyenleggel
--
--				     név,  cím
CREATE OR REPLACE FUNCTION uj_szamla(text, text, integer)
  RETURNS boolean
  AS $$
	  INSERT INTO szemelyes_adatok VALUES (
		$1, $2, $3 );
	  INSERT INTO egyenleg VALUES ( $3 );
	SELECT true;
  $$ LANGUAGE 'SQL';

--
-- Betét és kivét
--			 ide	  ezt
-- DROP FUNCTION befizet (integer, integer);
CREATE OR REPLACE FUNCTION befizet (integer, integer)
  RETURNS boolean
  AS $$
	  UPDATE egyenleg SET egyenleg= egyenleg+$2
	    WHERE szamlaszam = $1;
	  INSERT INTO naplo VALUES ( $1, $2, now() );
	 
	SELECT true;
     $$
	LANGUAGE 'SQL';

--
--  Átutalás
--			innen    ide      ennyit

-- DROP FUNCTION átutal (integer, integer, integer);
CREATE OR REPLACE FUNCTION atutal (integer, integer, integer)
  RETURNS boolean
  AS $$
	-- BEGIN;
	  UPDATE egyenleg SET egyenleg= egyenleg+$3
	    WHERE szamlaszam = $2;

	  UPDATE egyenleg SET egyenleg= egyenleg-$3
	    WHERE szamlaszam = $1;

	  INSERT INTO naplo VALUES ( $1, -1*$3, now() );
	  INSERT INTO naplo VALUES ( $2, $3, now() );
	 
	-- COMMIT;
	SELECT true;
  $$ LANGUAGE 'SQL';

--
--  Próbák a kipróbálásra
--
SELECT uj_szamla('Buksi', 'Futrinka u. 3.', 1);
SELECT uj_szamla('Sün Aladár', 'Erdő u. 2.', 2);
SELECT uj_szamla('Sün Dorottya', 'Erdő u. 1.', 3);
SELECT uj_szamla('Sün Demeter', 'Erdő u. 1.', 4);
SELECT uj_szamla('Süsü', 'Vár u. 2.', 5);
SELECT befizet( 1, 1000 );
SELECT befizet( 1, 5000 );
SELECT atutal ( 1, 2, 5500 );
SELECT atutal ( 2, 4, 500 );
SELECT atutal ( 2, 3, 1000 );

--
-- Nézettábla, amelyben látszik a név, cím és az összeg
--
CREATE VIEW betetesek AS
  SELECT nev, cim, egyenleg FROM szemelyes_adatok, egyenleg
      WHERE szemelyes_adatok.szamlaszam = egyenleg.szamlaszam
      ORDER BY nev;

SELECT 'Betétesek';
SELECT * FROM betetesek;
SELECT 'Napló';
SELECT * FROM naplo;

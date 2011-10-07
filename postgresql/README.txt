A PostgreSQL kezelése

---------------------------------------
Az alábbiakban azt feltételezzük, hogy létrehoztunk egy felhasználót
diak felhasználónévvel pl. a

   # adduser diak
   (vagy sudo adduser diak)

paranccsal.
Ha diak helyett más felhasználónevünk van, akkor a diak-ot mindenhol
helyettesítsük azzal.

---------------------------------------

0. Telepítés beállítás:

 a) telepítés (root-ként vagy sudo-val)

   # aptitude install postgresql
   (vagy sudo aptitude install postgresql)

 b) diak adatbázisfelhasználó létrehozása

   # su postgres
   (vagy sudo su postgres)

   $ createuser diak
   (y után n, ha jogot akarunk adni a felhasználónak
   adatbázisok létrehozására)

---------------------------------------

1. Adatbázis létrehozása:

 (postgres-ként, vagy ha a felhasználónak adtunk
 adatbázis létrehozására jogokat, felhasználóként)

 $ createdb diak

 Alapból mindenkinek egy saját nevével azonos
 nevű adatbázist érdemes létrehozni.

---------------------------------------

2. SQL-fájl tanulmányozása és beolvasása:

Normál felhasználóként:

 $ vim bank.sql
 $ psql -f bank.sql

Milyen függvényeket és táblázatokat hoztunk létre, és azok mit
csinálnak?

---------------------------------------

3. Interaktív munka:

Indítsuk el a PostgreSQL parancssorát!

  $ psql

Használhatjuk a bash-hez hasonlóan felfele gombot és a <Tab>-ot.
Minden SQL-parancsot pontosvesszővel kell lezárni. Ha elfelejtettük
a következő sorba csak a pontosvesszűt írjuk, ne az egész parancssort.
A psql saját parancsai \-vel kezdődnek, utánuk nem kell pontosvessző.

Listázzuk a táblákat!

 \d

Irassuk ki a táblázatok és a "betetesek" nézetmód mezőit!

 \d <táblanév>

Listázzuk a függvényeinket!

 \df public.*

Hozzunk létre új betétest!
(Találjuk ki a bank.sql és az előző feladatban szereplő függvények
segítségével, hogyan kell.)

Próbáljunk létrehozni nem létező névvel befizetést!

Próbáljunk törölni olyan sorokat, amelynek valamelyik mezőjére
	REFERENCES hivatkozik.

Hozzunk létre új táblázatot!

 \h CREATE TABLE

Például iranyitoszamok néven (iranyitoszam, telepulés) mezőkkel.
Segíthet az ebben a fájlban található puska (keressünk rá a Cheat Sheet
szövegre).

Hozzunk létre sorokat benne!

Kihagyható:
Keressünk benne reguláris kifejezésekkel (Cheat Sheet)

Lépjünk ki a psql-ből!
(Vajon melyik billentyűkombinációval lehet?)

---------------------------------------

4. Adatbázis mentése és visszaállítása

Adatbázis mentése:

 $ pg_dump diak >mentes.sql

Érdemes belenézni a mentett fájlba, tanulságos.

Adatbázis törlése:
 (postgres-ként, vagy ha a felhasználónak adtunk
 adatbázis létrehozására jogokat, felhasználóként)

 $ dropdb diak

Adatbázis létrehozása:
 (postgres-ként, vagy ha a felhasználónak adtunk
 adatbázis létrehozására jogokat, felhasználóként)

 $ createdb diak

Adatbázis visszatöltése:

 $ psql -f mentes.sql

Ellenőrizzük, hogy tényleg megvan-e minden.


---------------------------------------

5. Törlések

Próbáljuk törölni a szemelyes_adatok táblázatot!

 DROP TABLE szemelyes_adatok;

Milyen sorrendben törölhetem a táblázatokat? Tegyük meg!

Listázzuk a függvényeinket:

 \df public.*

Töröljünk közülük:

 DROP FUNCTION ...;

Mára ennyi. Köszönöm a figyelmet!
	HÁ

-------------------------------------
-------------------------------------

6.
PostgreSQL Cheat Sheet
from http://www.petefreitag.com/cheatsheets/postgresql/
Create database

CREATE DATABASE dbName;

Create table (with auto numbering integer id)

CREATE TABLE tableName (
 id serial PRIMARY KEY,
 name varchar(50) UNIQUE NOT NULL,
 dateCreated timestamp DEFAULT current_timestamp
);

Add a primary key

ALTER TABLE tableName ADD PRIMARY KEY (id);

Create an INDEX

CREATE UNIQUE INDEX indexName ON tableName (columnNames);

Backup a database (command line)

pg_dump dbName > dbName.sql

Backup all databases (command line)

pg_dumpall > pgbackup.sql

Run a SQL script (command line)

psql -f script.sql databaseName

Search using a regular expression

SELECT column FROM table WHERE column ~ 'foo.*';

The first N records

SELECT columns FROM table LIMIT 10;

Pagination

SELECT cols FROM table LIMIT 10 OFFSET 30;

Prepared Statements

PREPARE preparedInsert (int, varchar) AS
  INSERT INTO tableName (intColumn, charColumn) VALUES ($1, $2);
EXECUTE preparedInsert (1,'a');
EXECUTE preparedInsert (2,'b');
DEALLOCATE preparedInsert;

Create a Function

CREATE OR REPLACE FUNCTION month (timestamp) RETURNS integer 
 AS 'SELECT date_part(''month'', $1)::integer;'
LANGUAGE 'sql';

*** Table Maintenance

VACUUM ANALYZE table;

Reindex a database, table or index

REINDEX DATABASE dbName;

Show query plan

EXPLAIN SELECT * FROM table;

Import from a file

COPY destTable FROM '/tmp/somefile';

Show all runtime parameters

SHOW ALL;

Grant all permissions to a user

GRANT ALL PRIVILEGES ON table TO username;

Perform a transaction

BEGIN TRANSACTION 
 UPDATE accounts SET balance += 50 WHERE id = 1;
COMMIT;

**** Basic SQL
Get all columns and rows from a table

SELECT * FROM table;

Add a new row

INSERT INTO table (column1,column2)
VALUES (1, 'one');

Update a row

UPDATE table SET foo = 'bar' WHERE id = 1;

Delete a row

DELETE FROM table WHERE id = 1;

---------------------------------------

7. SQL-kezelése Pythonból:
$ vim pgdb_pygres_proba.py
$ ./pgdb_pygres_proba.py


------------------------------------
Tanári jegyzet:

sudo kell ezekre:
apt-get
su postgres

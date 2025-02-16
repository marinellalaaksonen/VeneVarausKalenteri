# Käyttötapaukset

## Venevaraukset
- käyttäjä pystyy varaamaan yhden veneen

Vapaana olevien veneiden hakeminen:
```
SELECT bo.id FROM boat bo WHERE bo.id NOT IN (
    SELECT b.id FROM boat b
    LEFT JOIN boat_reservation br ON b.id = br.boat_id
    LEFT JOIN reservation r ON br.reservation_id = r.id
    WHERE (r.starting_time < '2019-11-30 16:30:00.000000' AND r.ending_time > '2019-11-30 13:30:00.000000')
```
Veneen varaaminen:
```
INSERT INTO reservation VALUES(1,'2019-11-30 13:30:00.000000','2019-11-30 16:30:00.000000',1);
INSERT INTO boat_reservation VALUES(1,1);
```
- käyttäjä pystyy muokkaamaan varaustaan

Vapaana olevien veneiden hakeminen:
```
SELECT bo.id FROM boat bo WHERE bo.id NOT IN (
    SELECT b.id FROM boat b
    LEFT JOIN boat_reservation br ON b.id = br.boat_id
    LEFT JOIN reservation r ON br.reservation_id = r.id
    WHERE ((r.starting_time < '2019-12-04 18:30:00.000000' AND r.ending_time > '2019-12-04 15:30:00.000000')
        AND r.id <> 2)
```
Varauksen ajan muuttaminen:
```
UPDATE reservation SET starting_time='2019-12-04 15:30:00.000000', ending_time='2019-12-04 18:30:00.000000'
    WHERE reservation.id = 2
```
Veneiden vaihtaminen:
```
INSERT INTO boat_reservation (reservation_id, boat_id) VALUES (2, 2)
DELETE FROM boat_reservation WHERE boat_reservation.reservation_id = 3 AND boat_reservation.boat_id = 2
```
- käyttäjä pystyy poistamaan varauksensa
```
DELETE FROM reservation WHERE reservation.id = 2
DELETE FROM boat_reservation WHERE boat_reservation.reservation_id = 2 AND boat_reservation.boat_id = 1
```
- seura tai admin-käyttäjä pystyy varaamaan kerralla useamman veneen

Vapaana olevien veneiden hakeminen:
```
SELECT bo.id FROM boat bo WHERE bo.id NOT IN (
    SELECT b.id FROM boat b
    LEFT JOIN boat_reservation br ON b.id = br.boat_id
    LEFT JOIN reservation r ON br.reservation_id = r.id
    WHERE (r.starting_time < '2019-11-30 16:30:00.000000' AND r.ending_time > '2019-11-30 13:30:00.000000')
```
Veneen varaaminen:
```
INSERT INTO reservation VALUES(1,'2019-11-30 13:30:00.000000','2019-11-30 16:30:00.000000',1);
INSERT INTO boat_reservation VALUES(1,1);
```
- käyttäjä pystyy muokkaamaan useamman veneen varausta

Vapaana olevien veneiden hakeminen:
```
SELECT bo.id FROM boat bo WHERE bo.id NOT IN (
    SELECT b.id FROM boat b
    LEFT JOIN boat_reservation br ON b.id = br.boat_id
    LEFT JOIN reservation r ON br.reservation_id = r.id
    WHERE ((r.starting_time < '2019-12-04 18:30:00.000000' AND r.ending_time > '2019-12-04 15:30:00.000000')
        AND r.id <> 2)
```
Varauksen ajan muuttaminen:
```
UPDATE reservation SET starting_time='2019-12-04 15:30:00.000000', ending_time='2019-12-04 18:30:00.000000'
    WHERE reservation.id = 2
```
Veneiden määrän muuttaminen:
```
INSERT INTO boat_reservation (reservation_id, boat_id) VALUES (2, 2)
DELETE FROM boat_reservation WHERE boat_reservation.reservation_id = 3 AND boat_reservation.boat_id = 2
```
- käyttäjä pystyy tarkastelemaan tekemiään varauksia
- käyttäjä pystyy listaamaan veneet ja niiden tiedot
```
SELECT b.name, b.boat_type, b.boat_class FROM boat b
```

## Statistiikka
- käyttäjä pystyy tarkastelemaan tekemiään varauksia
```
SELECT count(*) FROM boat_reservation br
JOIN reservation r ON r.id = br.reservation_id
WHERE (r.starting_time < "2020-01-01 00:00:00"
    AND r.ending_time > "2019-01-01 00:00:00"
    AND r.user_id = 1)
```
- käyttäjät näkevät yhteenvedon kaikista vuoden aikana tehdyistä varauksista
Varauksia yhteensä kuluvana vuonna (kaikkien käyttäjäryhmien varaukset):
```
SELECT count(*) FROM boat_reservation br
JOIN reservation r ON r.id = br.reservation_id
WHERE (r.starting_time < "2020-01-01 00:00:00"
    AND r.ending_time > "2019-01-01 00:00:00"
```
Kipparilla varauksia keskimäärin (mukaan lasketaan kuluvan vuoden aikana varauksia tehneet kipparit, joilla ei ole ryhmä- tai admin-oikeuksia):
```
SELECT avg(result) FROM(
    SELECT count(*) AS result FROM boat_reservation br
    JOIN reservation r ON r.id = br.reservation_id
    WHERE (r.starting_time < "2020-01-01 00:00:00"
        AND r.ending_time > "2019-01-01 00:00:00"
        AND r.user_id NOT IN (
            SELECT ar.account_id FROM account_role ar
            JOIN role r ON r.id = ar.role_id
            WHERE r.name = 'admin'
                OR r.name = 'club'))
    GROUP BY r.user_id)
```
## Veneiden hallinnointi
- admin pystyy lisäämään veneen
```
INSERT INTO boat VALUES(1,'YoT','sailboat','J/80');
```
- admin pystyy poistamaan veneen
```
DELETE FROM boat WHERE boat.id = 2
```
Jos veneellä on varauksia:
```
DELETE FROM boat_reservation WHERE boat_reservation.reservation_id = 3 AND boat_reservation.boat_id = 2
```
- admin pystyy muokkaamaan veneen tietoja
```
UPDATE boat SET boat_name = 'YoT'
```

## Käyttäjien hallinnointi
- käyttäjä pystyy rekisteröitymään
```
INSERT INTO account VALUES(2,'test','test','test','bcrypted hash');
```
- käyttäjä pystyy kirjautumaan
```
SELECT account.id AS account_id, account.name AS account_name, account.username AS account_username, 
        account.email AS account_email, account.password AS account_password
    FROM account
    WHERE account.username = 'test'
```

# Käyttötapaukset

## Venevaraukset
- käyttäjä pystyy varaamaan yhden veneen
- käyttäjä pystyy muokkaamaan varaustaan
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
    WHERE (r.starting_time < :ending_time AND r.ending_time > :starting_time))
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
    WHERE ((r.starting_time < :ending_time AND r.ending_time > :starting_time)
        AND r.id <> :reservation_id))
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
- käyttäjä pystyy listaamaan veneet ja niiden tiedot
```
SELECT b.name, b.boat_type, b.boat_class FROM boat b
```

## Statistiikka
- käyttäjä pystyy tarkastelemaan yhteenvetoa tekemistään varauksista
- seura tai admin-käyttäjä pystyy tarkastelemaan yhteenvetoa veneiden käyttöasteesta

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
- admin pystyy estämään varaukset veneille jotka eivät ole kunnossa

## Käyttäjien hallinnointi
- käyttäjä pystyy rekisteröitymään
```
INSERT INTO account VALUES(2,'test','test','test','testtest');
```
- käyttäjä pystyy kirjautumaan
```
SELECT account.id AS account_id, account.name AS account_name, account.username AS account_username, 
        account.email AS account_email, account.password AS account_password
    FROM account
    WHERE account.id = 1
```
# Käyttötapaukset

## Venevaraukset
- käyttäjä pystyy varaamaan yhden veneen
- käyttäjä pystyy muokkaamaan varaustaan
- käyttäjä pystyy poistamaan varauksensa
- seura tai admin-käyttäjä pystyy varaamaan kerralla useamman veneen
- käyttäjä pystyy muokkaamaan useamman veneen varausta
- käyttäjä pystyy listaamaan veneet ja niiden tiedot

## Statistiikka
- käyttäjä pystyy tarkastelemaan yhteenvetoa tekemistään varauksista
- seura tai admin-käyttäjä pystyy tarkastelemaan yhteenvetoa veneiden käyttöasteesta

## Veneiden ja käyttäjien hallintointi
- admin pystyy lisäämään veneen
- admin pystyy poistamaan veneen
- admin pystyy muokkaamaan veneen tietoja
- admin pystyy lisäämään käyttäjän
- admin pystyy poistamaan käyttäjän
- admin pystyy muokkaamaan käyttäjän tietoja
- admin pystyy estämään varaukset veneille jotka eivät ole kunnossa

## Jatkokehitysideoita (ei toteuteta harjoitustyön puitteissa)
- mahdollisuus useamman erillisen venevarauskalenterin luomiseen (606 ja följebåtar)
    - moottoriveneillä veneet erilaisia, eli pitäisi yksilöidä veneet varauskalenterissa
- veneraportin integroiminen varausjärjestelmään:
    - varausjärjestelmä näyttää veneen statuksen varauskalenterin vieressä (ok, pientä korjattavaa mutta voi käyttää, käyttökiellossa) ja mitä on rikki
    - mahdollisuus tehdä veneraportti ilman kirjautumista
    - veneraporttiin ajat jolloin statistiikat veneraporttien perusteella?
    - veneraportin sitominen purjehtijoilla varaukseen siten, että uusien varausten teko estyy kunnes veneraportti on tehty
        - tällöin myös joku nappula "treenit peruttu" ja syy siihen
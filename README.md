# Venevarauskalenteri

Tehdään venevarauskalenteri, jossa käytäjä voi varata yhden tai useamman veneen haluammalleen ajanjaksolle. Käyttäjäryhmiä ovat purjehtijat, seura-käyttäjät ja admin. Kipparit varaavat veneen omalle tiimilleen ja pystyy varaamaan kerrallaan vain yhden veneen. Kipparilla voi olla voimassa korkeintaan neljä varausta kerralla. Seura- ja admin-käyttäjät varaavat veneitä seuran järjestämiin harjoituksiin ja kilpailuihin ja pystyvät varaamaan useita veneitä kerralla. Varausten kokonaismäärää ei ole rajoitettu. Käyttäjä pystyy myös muokkaamaan ja poistamaan varauksiaan. 

Veneitä varataan kalenterissa vain tiettyy määrä eikä jotain yksittäistä tiettyä venettä. Veneeseen kuitenkin liittyy jatkokehitettävyyden takia nimi, tyyppi ja luokka. Admin pystyy lisäämään, muokkaamaan ja poistamaan veneitä. Sovelluksesta voi myös tarkastella veneiden käyttömääriä sekä yhteenvetoa käyttäjän varauksista.

[Tietokantakaavio](https://github.com/marinellalaaksonen/Venevarauskalenteri/blob/master/documentation/tietokantakaavio.png)  
[Käyttötapaukset](https://github.com/marinellalaaksonen/Venevarauskalenteri/blob/master/documentation/kayttotapaukset.md)

## Käyttöohje

Sovellusta pääsee käyttämään [Herokussa](https://boat-booking-calendar.herokuapp.com/) luomalla oman käyttäjän yläpalkin register-painikkeesta tai kirjautumalla seuraavilla testitunnuksilla login-painikkeesta:

```
tavallinen käyttäjä: 
  username: test  
  password: testtest
admin:
  username: admin  
  password: adminadmin
```

Sovelluksessa pystyy tekemään uuden varauksen painikkeesta reserve boat ja syöttämällä pyydetyt tiedot. Kaikkia tehtyjä varaukset pystyy listaamaan show reservation -painikkeesta. Varausten listaus tarjoaa myös omien varausten kohdalla mahdollisuuden muokata tai poistaa varauksen. Järjestelmässä olevat veneet pystyy listaamaan list boats -painikkeesta.

Lisäksi admin-käyttäjä pystyy lisäämään veneen add boat -painikkeesta. Admin pystyy myös muokkaamaan veneiden tietoja tai poistamaan veneen veneiden listauksesta löytyvien painikkeiden avulla.

## Asennusohje

Jos haluat käyttää sovellusta paikallisesti omalla koneellasi voit ladata sovelluksen koneellesi GitHubin clone or download -painikkeen alta löytyvästä kohdasta download zip. Sovelluksen käyttöön tarvitset myös Pythonin (versio 3.5 tai uudempi) sekä Pythonin pip- ja venv-kirjastot. [Täältä](https://materiaalit.github.io/tsoha-19/tyovalineet/) löydät tarvittaessa ohjeet niiden lataamiseen.

Kun olet ladannut ohjelman koneellesi, pura zip-tiedosto ja mene terminalissa projektin kansioon. Luo tämän jälkeen Python virtuaaliympäristö komennolla ```python3 -m venv venv``` ja aktivoi se komennolla ```source venv/bin/activate```. Asenna vielä projektin riippuvuudet komennolla ```pip install -r requirements.txt```. Nyt voit käynnistää sovelluksen komennolla ```python run.py```. Voit käyttää paikallista sovellusta osoitteessa http://127.0.0.1:5000/ ohjelman ollessa käynnissä koneellasi.

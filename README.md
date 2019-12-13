# Venevarauskalenteri

Tehdään venevarauskalenteri, jossa käytäjä voi varata yhden tai useamman veneen haluammalleen ajanjaksolle. Käyttäjäryhmiä ovat purjehtijat, seura-käyttäjät ja admin. Kipparit varaavat veneen omalle tiimilleen ja pystyy varaamaan kerrallaan vain yhden veneen. Kipparilla voi olla voimassa korkeintaan neljä varausta kerralla. Seura- ja admin-käyttäjät varaavat veneitä seuran järjestämiin harjoituksiin ja kilpailuihin ja pystyvät varaamaan useita veneitä kerralla. Varausten kokonaismäärää ei ole rajoitettu. Käyttäjä pystyy myös muokkaamaan ja poistamaan varauksiaan. 

Veneitä varataan kalenterissa vain tiettyy määrä eikä jotain yksittäistä tiettyä venettä. Veneeseen kuitenkin liittyy jatkokehitettävyyden takia nimi, tyyppi ja luokka. Admin pystyy lisäämään, muokkaamaan ja poistamaan veneitä. Veneitä poistetaan pääasiassa kausien välillä(talvella). Sovelluksesta voi myös tarkastella veneiden käyttömääriä sekä yhteenvetoa käyttäjän varauksista.

[Tietokantakaavio](https://github.com/marinellalaaksonen/Venevarauskalenteri/blob/master/documentation/tietokantakaavio.png)  
[Käyttötapaukset](https://github.com/marinellalaaksonen/Venevarauskalenteri/blob/master/documentation/kayttotapaukset.md)

## Käyttöohje

Sovellusta pääsee käyttämään [Herokussa](https://boat-booking-calendar.herokuapp.com/) luomalla oman käyttäjän yläpalkin register-painikkeesta tai kirjautumalla seuraavilla testitunnuksilla login-painikkeesta:

```
tavallinen käyttäjä: 
  username: test  
  password: testtest
seurakäyttäjä: 
  username: club  
  password: clubclub
admin:
  username: admin  
  password: adminadmin
```

Sovelluksessa pystyy tekemään uuden varauksen painikkeesta reserve boat ja syöttämällä pyydetyt tiedot. Kaikkia tehtyjä varaukset pystyy listaamaan show reservation -painikkeesta. Varausten listaus tarjoaa myös omien varausten kohdalla mahdollisuuden muokata tai poistaa varauksen. Järjestelmässä olevat veneet pystyy listaamaan list boats -painikkeesta.

Lisäksi admin-käyttäjä pystyy lisäämään veneen add boat -painikkeesta. Admin pystyy myös muokkaamaan veneiden tietoja tai poistamaan veneen veneiden listauksesta löytyvien painikkeiden avulla.

Sovellus toimii parhaiten riittävän isolla ruudulla, pienempi ruutu saattaa kadottaa osan valinnoista.

## Asennusohje

Jos haluat käyttää sovellusta paikallisesti omalla koneellasi voit ladata sovelluksen koneellesi GitHubin clone or download -painikkeen alta löytyvästä kohdasta download zip. Sovelluksen käyttöön tarvitset myös Pythonin (versio 3.5 tai uudempi) sekä Pythonin pip- ja venv-kirjastot. Jos haluat ladata sovelluksen Herokuun tarvitset lisäksi PostgreSQL-tietokannanhallintajärjestelmän käyttäjätunnuksen Herokuun sekä työvälineet Herokun ja git:n käyttöön. [Täältä](https://materiaalit.github.io/tsoha-19/tyovalineet/) löydät tarvittaessa ohjeet niiden lataamiseen.

Kun olet ladannut ohjelman koneellesi, pura zip-tiedosto ja mene terminalissa projektin kansioon. Luo tämän jälkeen Python virtuaaliympäristö komennolla ```python3 -m venv venv``` ja aktivoi se komennolla ```source venv/bin/activate```. Asenna vielä projektin riippuvuudet komennolla ```pip install -r requirements.txt```. Nyt voit käynnistää sovelluksen komennolla ```python run.py```. Voit käyttää paikallista sovellusta osoitteessa http://127.0.0.1:5000/ ohjelman ollessa käynnissä koneellasi. Sovelluksen saa suljettua painamalla ctrl+c.

Jos haluat siirtää sovelluksen Herokuun mene terminalissa projektin kansioon ja alusta ensin git komennolla ```git init```. Lisää tämän jälkeen projekti herokuun komennolla ```heroku create [project_name]```. Nyt voit ladata projektin Herokuun ajamalla seuraavat komennot:
```git add .```
```git commit -m "lisätty herokuun"```
```git push heroku master```
Alusta vielä Heroku käyttämään PostgreSQL-tietokantaa:
```heroku addons:add heroku-postgresql:hobby-dev```
```heroku config:set HEROKU=1```
Nyt sovellus pyörii Herokussa osoitteessa https://[project_name].herokuapp.com/

Lisää asennuksen jälkeen sovellukseen roolit. Jos ajat sovellusta paikallisesti, muodosta yhteys tietokantaan komennolla ```sqlite3 application/venevarauskalenteri.db```. Herokussa tietokantaan saa yhteyden komennolla ```heroku pg:psql```. Lisää tämän jälkeen roolit komennolla ```INSERT INTO role VALUES(1, 'admin')```, ```INSERT INTO role VALUES(2, 'club')``` ja ```INSERT INTO role VALUES(3, 'skipper')```.

Kaikki käyttäjät saavat käyttäjän luomisen yhteydessä roolikseen "skipper", muita rooleja ovat "club" ja "admin". Ainoastaan admin käyttäjä pystyy lisäämään järjestelmään veneitä. Seura-käyttäjillä ("club") varausoikeutta ei ole rajoitettu toisin kuin kippareilla. Jos haluat lisätä käyttäjälle oikeuksia se onnistuu tällä hetkellä ainoastaan tietokannan kautta. Tämän jälkeen käyttäjälle saa lisättyä oikeuksia komennolla ```INSERT INTO account_role VALUES (account_id, role_id);```, jossa account_id on haluamasi käyttäjän id ja role_id haluamasi roolin id. Käyttäjän id:n saat tietoosi komennolla ```SELECT a.id FROM account a  WHERE a.username = "käyttäjän_käyttäjänimi";``` ja admin-roolin id:n komennolla ```SELECT r.id FROM role r  WHERE r.name = "admin";```. Jos haluat saada tietoosi seura-roolin id:n muuta jälkimmäisestä komennosta "admin" muotoon "club". Tiotokannan yhteyden saa lopetettua painamalla ctrl+d.

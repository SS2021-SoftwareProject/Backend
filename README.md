# Backend
# Team

Name | Github | Role
------------ | ------------ | ------------
Jan Ehreke | Epixware | Project lead
Michel Dudas | smierx | Backend Developer
Niklas Lange | niklas9937 | Backend Developer
Sören Kröger | FlatCatSociety | Backend Developer
Jannis Herbertz | Kushurando | Backend Developer
Thomas Morbe| tmorbe | Backend Developer
Oliver Maciejewski | Saryna42 | Backend Developer      


## Virtual Enviroment
install.sh ausführen

```
sudo mysql -u root -p

create database backend;

use backend;

CREATE USER 'rootApi'@'localhost' IDENTIFIED BY 'thiel';

GRANT ALL PRIVILEGES ON backend.* TO 'rootApi'@'localhost';

FLUSH PRIVILEGES;

quit;
```

Wenn ihr Bibliotheken benötigt die noch nicht im requirements stehen einfach eintragen und 
```
source venv/bin/activate
pip3 install -r requirements.txt
```
ausführen


**Wallet Zugang**
  1. Empfolenes Wallet --> MetaMask (Chrome Erweiterung --> https://metamask.io/)
  2. Metamask öffnen und auf "import using Secret Recovery Phrase" klicken.
  3. Secret Recovery Phrase eingeben "shove tone tilt fly zoo pottery artefact omit okay mistake egg core" eingeben
  4. Ein eigenes Passwort wählen (Ist nur für euren eigenen PC damit ihr nicht immer die Passphrase eingeben müsst)
  5. Sicherstellen, dass oben rechts "Ropsten Testnetzwerk" steht. Wenn dort etwas anderes muss dies ausgewählt werden.
  6. Buy und Send empfehle ich erst einmal zu meiden. Wenn getestet werden will macht dies bitte nach Anleitung da es auch im Testnetzwerk nur eine begrenzte anzahl an Coins gibt und es nicht gerne gesehen wird wenn Coins gehortet werden.
  7. Die Passphrase ist unter normalen umständen auf keinen Fall rauszugeben. Da dies aber nur ein Test Wallet ist habe ich sie hier einfach eingefügt.

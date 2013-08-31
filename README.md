* Instaliraj Flask

> sudo pip install Flask

Ako ti javi grešku da pip ne postoji onda ga instaliraj sa:

    sudo apt-get -y install python-pip python-dev build-essential
    sudo pip install --upgrade pip
    sudo pip install --upgrade virtualenv

* Raspakiraj zip u neki folder, npr:

    unzip WebApp.zip  -d /home/dario/webapp

Ako nemaš unzip instaliraj ga sa:

    sudo apt-get install zip

* Sad već možeš pokrenuti web aplikaciju sa:

    cd /home/dario/webapp
    python server.py

Server će biti na portu 5000, pa u web browseru otvori stranicu:

http://localhost:5000/

Možda ti je port 5000 zabranjen na firewallu pa ga moraš enejblati ako želiš otvoriti tu stranicu na drugom kompjuteru.

* Pokretanje web aplikacije unutar Apache servera na portu 80 je kompliciranije. Ovo je najjednostavnija procedura ako si na debian distribuciji. Kreiraj conf. fajl u apache2 direktoriju:

    sudo nano /etc/apache2/sites-available/webapp

i unesi ovo:

    <VirtualHost *:80>
        WSGIDaemonProcess webapp user=dario group=dario threads=5
        WSGIScriptAlias / /home/dario/webapp/server.wsgi

        <Directory /home/dario/webapp/>
            WSGIProcessGroup webapp
            WSGIApplicationGroup %{GLOBAL}
            Order deny,allow
            Allow from all
        </Directory>
    </VirtualHost>

zatim izvrši:

    sudo a2ensite default
    sudo rm /etc/apache2/sites-enabled/000-default
    sudo service apache2 reload
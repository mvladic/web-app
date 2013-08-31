#!/bin/bash
sudo apt-get -y update

sudo apt-get -y install python-pip python-dev build-essential
sudo pip install --upgrade pip
sudo pip install --upgrade virtualenv
sudo pip install Flask

sudo apt-get -y install apache2 libapache2-mod-wsgi
#!/bin/bash

clear
echo "Installing."
wget "nonpersviluppatori.altervista.org/github/dist.zip"
unzip dist.zip
sleep 1
./dist/PyWeb

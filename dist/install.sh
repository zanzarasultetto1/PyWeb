#!/bin/bash

clear
echo "Installing."
sleep 2
wget "nonpersviluppatori.altervista.org/github/dist.zip"
unzip dist.zip
sleep 1
./dist/PyWeb

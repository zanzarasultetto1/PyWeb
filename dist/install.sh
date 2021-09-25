#!/bin/bash

clear
echo "Installing."
sleep 2
wget "nonpersviluppatori.altervista.org/github/dist.zip"
unzip dist.zip
sleep 1
clear
rm dist.zip
echo "Installed. Your file is now in the dist folder."
echo "Press ENTER to exit..."
read 

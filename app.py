#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Ce fichier nommer font_controleur permets préparer les données à transmettre
au adéquat back_controleur

Auteur
-------
Elmes
electromecatronique01@gmail.com

Date de création
-----------------
17/Mai/2022 14:40
"""

#Importation
import vues

#Définitions

#Affectations
nom = "";
if __name__ == '__main__':
	print("<<<<<<<< Bonjour, veuillez nous communiquer votre nom svp! >>>>>>>>>\n")
	nom = input("Taper votre nom ici : ")

	vues.bienvenue(nom)
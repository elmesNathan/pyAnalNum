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
17/Mai/2022 14:30
"""

#Importation
import back_controleurs

#Définitions
def rectangle(choix, a, b, f, n):
	"""
	Cette fonction va appeler le controleur methode_rectangle avec 
	les paramètres provenants de la vues 

	"""
	return back_controleurs.methonde_rectangle(a, b, n, f, choix, )

def euler(a, b, f, n, x0, y0):
	"""
	Cette fonction va appeler le controleur euler avec les données en 
	paramètres lesquels provenant de la vue euler
	"""
	return back_controleurs.euler(a, b, n, f, x0, y0)

#Affectations
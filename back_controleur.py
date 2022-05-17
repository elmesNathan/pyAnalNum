#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Ce fichier nommer back_controleur permets de faire le calcul
numérique.

Pour ce faire, il rappatrie les données provenant du fichier 
front_controleur et les formules du fichier models.

En suite il évalue le résultat en faisant correspondre les données 
et la formules correspondant aux données.

Le résultat est directement envoyer au fichier vues
Auteur
-------
Elmes
electromecatronique01@gmail.com

Date de création
-----------------
17/Mai/2022 12:00
"""

#Importation
from models import *
from front_controleurs import *
from vues import *
import math

#Définitions
def methonde_rectagles(a, b, n, f, choix):
	"""
	Calcul de l'intégrale par la méthode du Rectagle
	On définit h par :
		 b - a
	h = -------
	       n	
	On trouve les abscices X par :
	X = xi (Pour la méthode du Rectangle à Gauche)
	X = xi + h (Pour la méthode du Rectangle à Droite)

	On trouve les ordonnées Y par :
	Y = yi

	Et enfin, on détermine la valeur approchée en 
	évaluant la formule de l'approximation par le rectangle.
	"""
	h = (b - a)/n
	xi = []
	yi = []

	if choix == "G":
		for x in range(a,b,h):
			yi.append(eval(f))
	else:
		for x in range(a+h, b+h, h):
			yi.append(eval(f))

	solution = eval(rectagles())

	return vue_rectangle(xi, yi, solution)


#Affectation

#if __name__ == '__main__' :


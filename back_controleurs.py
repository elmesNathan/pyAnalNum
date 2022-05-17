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
import models 
import front_controleurs 
import vues 
import math
import numpy as np

#Définitions
def methonde_rectangle(a, b, n, f, choix):
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
	h = (b-a)/n
	xi = []
	yi = []
	i = 0

	if choix == "0":
		while i < n :
			xi.append(a + i*h)
			i = i + 1

		for x in xi:
			yi.append(eval(f))
	else:
		while i <= n :
			xi.append(a+h + i*h)
			i = i + 1

		for x in xi:
			yi.append(eval(f))

	solution = eval(models.rectangle())

	return vues.vue_rectangle(xi, yi, solution)


#Affectations
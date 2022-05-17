#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Ce fichier nommer vues permet d'intérargir avec l'utilisateur,

Auteur
-------
Elmes
electromecatronique01@gmail.com

Date de création
-----------------
17/Mai/2022 13:00
"""
#Importation
from numpy as np
from matplotlib.pyplot as plt
import front_controleurs

#Définitions
def vue_rectangle(xi, yi, solution):
	x = np.array(xi)
	y = np.array(yi)

	plt.plot(x, y, label="Val approximative de f dans xn - xi")

	plt.xlabel("Discretisation avec écart h")
	plt.ylabel("Approximation de f")

	plt.title("Proximation de l'intégrale par la méthode du Rectangle")
	plt.legend()

	plt.show()

def bienvenue():
	print("""
		--------------------------------------------------------------------------------
		Bienvenue chez elmes
		
		Cette application console, va vous permettre de résoudre par les
		méthodes dites numériques, les élements suivantes :
		  1. Les intégrales simples
		  2. Les équations différentielles
		  3. Les problèmes de l'alagèbre linéaires

		Pour ce faire veuillez faire le choix de l'opération que vous désirer.
		Appuyez sur la touche (0) pour l'intégrale avec la méthode du rectangle à gauche
		Appuyez sur la touche (1) pour l'intégrale avec la méthode du rectangle à droite
		Appuyez sur la touche (2) pour l'équation différentielle ordinaire du 1er ordre
		Appuyez sur la touche (3) pour l'équation différentielle ordinaire du 2d ordre
		Appuyez sur la touche (4) pour l'équation elliptique du 2d ordre
		Appuyer sur la touche (5) pour l'équation parabolique du 2d ordre
		Appuyez sur la touche (6) pour l'équation hyperbolique du 2d ordre
		Appuyez sur la touche (7) pour résoudre les problèmes de l'algèbre linéaire
		-------------------------------------------------------------------------------
		""")
	choix = input("\n\nVeuillez faire votre choix ici : ")
	if eval(choix).is_integer() :
		return eval(choix)
	else
		print("\n\nSVP Veuillez insérer une parmis les valeurs indiquées...\nAllez on recommence à partir de zero\n\n")
		return bienvenue()

def data_rectangle():
	choix = bienvenue()
	if choix == 0 OR choix == 1 :
		print("\n\nSi vous utiliserer des fonctions trigonométriques, insérer les angles en radiant ex. 3*math.pi/2 pour 270°")
		intervalle = input("\n\nVeuillez enter l'intervale, de la manière suivante a;b : ")

		a, b = intervalle.split(';')
		a , b = eval(a), eval(b)

		fonction = input("\n\nVeuillez entrer la fonction, avec x comme variable")

		dicret = input("\n\nVeuillez entrer les nombres entier n de l'étendue : ")

		n = eval(dicret)

		return front_controleurs.rectangle(choix, a, b, fonction, n)
	else :
		return bienvenue()


#Affectation

#if __name__ == '__main__' :
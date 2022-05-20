#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Ce fichier nommer vues permet d'intérargir avec l'utilisateur.
Il sait comment recupérer les données insérer par l'unitisateur
et le envoie au front controleur adéquat.

Auteur
-------
Elmes
electromecatronique01@gmail.com

Date de création
-----------------
17/Mai/2022 13:00
"""
#Importation
import numpy as np
import matplotlib.pyplot as plt
import front_controleurs
from app import nom

#Définitions
def vue_rectangle(xi, yi, solution, nom=nom):
	x = np.array(xi)
	y = np.array(yi)
	print(x)
	print(y)
	plt.plot(x, y)

	plt.xlabel("Discretisation avec écart h")
	plt.ylabel("Approximation de f")
	text = "La valeur approchée de l'intégrale est : {}". format(solution)
	plt.title(text)
	plt.legend()

	plt.show()
	continuer = input("Voulez vous reutiliser l'application.\nAppuyez sur 1 pour oui et toute autre touche pour non : > ")
	if continuer == "1":
		bienvenue(nom)
	else:
		print("Bye bye {}, Elmes est très ravis d'avoir travailler avec toi...".format(nom))

def vue_euler(xk, yk_1, h):
	x = np.array(xk)
	y = np.array(yk_1)
	print(x)
	print(y)
	plt.plot(x, y)
	text = "intervalle fixé à {}".format(h)
	plt.xlabel(text)
	plt.ylabel("Approximation de Y_k+1")
	text = "La fonction approchée par la méthode d'Euler"
	plt.title(text)

	plt.show()
	continuer = input("Voulez vous reutiliser l'application.\nAppuyez sur 1 pour oui et toute autre touche pour non : > ")
	if continuer == "1":
		bienvenue(nom)
	else:
		print("""Bye bye, Elmes est très ravis d'avoir travailler avec toi...""".format(nom))


def bienvenue(nom):
	nom = nom
	print("""
		--------------------------------------------------------------------------------
		Bienvenue chez elmes {}
		
		Cette application console, va vous permettre de résoudre par les
		méthodes dites numériques, les élements suivants :
		  1. Les intégrales simples
		  2. Les équations différentielles
		  3. Les problèmes de l'alagèbre linéaires

		Pour ce faire veuillez faire le choix de l'opération que vous désirer.
		Appuyez sur la touche (0) pour l'intégrale avec la méthode du rectangle à gauche
		Appuyez sur la touche (1) pour l'intégrale avec la méthode du rectangle à droite
		Appuyez sur la touche (2) pour l'équation différentielle ordinaire du 1er ordre
		Appuyer sur la touche (3) pour l'équation parabolique du 2d ordre
		-------------------------------------------------------------------------------
		Pour quitter ce programme appuyer sur la touche q
		""".format(nom))

	choix = input("\n\nVeuillez faire votre choix ici : ")
	
	if choix == "0" or choix == "1":
		return data_rectangle(choix)

	elif choix == "2":
		return data_euler()

	elif choix == "3":
		return data_parabolique()

	elif choix == "q" or choix == "Q":
		return """.....  Bye  bye ..... \n\n\n"""

	else:
		print("""
			\n\nSVP Veuillez insérer une parmis les valeurs indiquées...\n
			Allez on recommence à partir de zero\n\n""")
		return bienvenue(nom)

def data_rectangle(choix, nom=nom):
	print("\n\nSi vous utiliserer des fonctions trigonométriques, insérer les angles en radiant ex. 3*np.pi/2 pour 270°")
	intervalle = input("\n\nVeuillez enter l'intervale, de la manière suivante a;b : """)

	a, b = intervalle.split(';')
	a , b = eval(a), eval(b)

	fonction = input("\n\nVeuillez entrer la fonction, avec x comme variable : ")

	discret = input("\n\nVeuillez entrer les nombres entier n de l'étendue : ")

	n = eval(discret)

	return front_controleurs.rectangle(choix, a, b, fonction, n)

def data_euler():
	print("\n\nSi vous utiliserer des fonctions trigonométriques, insérer les angles en radiant ex. 3*np.pi/2 pour 270°")
	intervalle = input("\n\nVeuillez enter l'intervale, de la manière suivante a;b : """)

	a, b = intervalle.split(';')
	a , b = eval(a), eval(b)

	fonction = input("\n\nVeuillez entrer le second f(x,y(x)) : ")

	discret = input("\n\nVeuillez entrer les nombres entier n de l'étendue : ")

	n = eval(discret)

	ci = input("\n\nVeuiller entre la condition initian sous forme x0;y0 : ")
	
	x0, y0 = ci.split(';')

	x0 = float(x0)
	y0 = float(y0)

	return front_controleurs.euler(a, b, fonction, n, x0, y0)

def data_parabolique():
	print("\nQuelles sont les conditions aux initiales [ti,tf] ? \n")
	val = input("Entrez les valeurs de cette manière ti;tf --> ")
	ti, tf = val.split(';')
	ci = [eval(ti), eval(tf)]

	print("\nQuelles sont les conditions limites [a,b]? \n")
	val = input("Entrez les valeurs de cette manière a;b --> ")
	a, b = val.split(';')
	cl = [eval(a), eval(b)]

	print("\nQuelle est le matériaux utiliser (conductivité) ?\n")
	val = input("Entrez la valeur numérique ici --> ")
	D = eval(val)

	print("\nQuelle est la valeur de l'espacement (hx) ?\n")
	val = input("Entrez la numérique ici --> ")
	hx = eval(val)

	print("\nQuelle est le comportement du matériaux\n")
	val = input("Entrer la fonction en ici --> ")
	fx = val

	return front_controleurs.parabolique(ci, cl, fx, D, hx, ht)
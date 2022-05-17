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

#Définitions
def vue_rectangle(xi, yi, solution):
	x = np.array(xi)
	y = np.array(yi)
	plt.plot(x, y, label="Val approximative de f dans xn - xi")
	plt.xlabel("Discretisation avec écart h")
	plt.ylabel("Approximation de f")
	plt.title("Proximation de l'intégrale par la méthode du Rectangle")

	plt.show()



#Affectation

#if __name__ == '__main__' :
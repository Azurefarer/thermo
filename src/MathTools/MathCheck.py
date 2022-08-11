from tkinter import E
import numpy as np
import sympy as sp
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import pygame as pg
from abc import ABC, abstractmethod


a = np.cos(-np.pi/3)
b = np.cos(np.pi*5/3)
print(a, b)
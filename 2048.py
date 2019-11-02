import tkinter as tk
from tkinter import ttk,Frame,CENTER
from tkinter import scrolledtext as st
import random


class App:

	def __init__(self):
		#configuracion de ventana
		self.ventana = tk.Tk()		
		self.ventana.title("GUI")
		self.ventana.geometry("480x480")	
		self.ventana.configure(background='#BBADA0'	)
		
		#variables         
		#DICCIONARIO CON COLORES DE ACUERDO AL VALOR
		self.COLOR_FONDO_CELDA =	{
			2: '#EEE4DA',
			4: '#EDE0C8',
			8: '#EDE0C8',
			16: '#F59563',
			32: '#F67C5F',
			64: '#F65E3B',
			128: '#EDCF72',
			256: '#EDCC61',
			512: '#EDC850',
			1024: '#EDC53F', 
			2048: '#edc22e'	
		}

		self.CELDA_COLOR_LETRA = {
			2: "#776e65", 
			4: "#776e65", 
			8: "#f9f6f2", 
			16: "#f9f6f2",
			32: "#f9f6f2",
			64: "#f9f6f2",
			128: "#f9f6f2",
			256: "#f9f6f2",
			512: "#f9f6f2",
			1024: "#f9f6f2",
			2048: "#f9f6f2",
		}
		

		self.ventana.bind('<Key>',self.direccionales)
		#INICIAR MATRIZ QUE CONTIENE VALORES
		self.matriz_de_valores = self.inicializar_matriz_de_valores()
		
		#INICIAR TABLA
		self.iniciar_tabla()

		#INICIAR JUEGO CON 2 CUADROS "2" RANDOM		
		self.cuadro_random()		
		self.cuadro_random()		
		self.actualizar_celdas()


		self.ventana.mainloop()
	
	def inicializar_matriz_de_valores(self):
		matrix = [[0 for i in range(4)]for j in range(4)]
		return matrix
	
	def iniciar_tabla(self):
		self.tabla = []
		for i in range(4) :
			self.fila = []
			for j in range(4):				
				self.fondo = tk.Frame(
					self.ventana,
					heigh=100,
					width=100,
					background='#CDC1B4')
				self.fondo.grid(row=i,column=j,padx=10,pady=10)

				self.cuadro_activo = tk.Frame(
					self.ventana,
					heigh=100,
					width=100,
					background='#CDC1B4')
				self.cuadro_activo.grid(row=i,column=j,padx=10,pady=10)
				self.cuadro_activo.grid_propagate(False)
				self.cuadro_activo.columnconfigure(0, weight=1)
				self.cuadro_activo.rowconfigure(0, weight=1) 

				self.texto = tk.Label(
					master=self.cuadro_activo,
					text="",bg='#CDC1B4',font=("Clear Sans", 30, "bold"),
					heigh=4,width=4)
				self.texto.grid()
				self.fila.append(self.texto)
			self.tabla.append(self.fila)	

	def cuadro_random(self):
		self.randomrow = random.randint(0,3)
		self.randomcolumn = random.randint(0,3)	
		while(self.matriz_de_valores[self.randomrow][self.randomcolumn] != 0):
			self.randomrow = random.randint(0,3)
			self.randomcolumn = random.randint(0,3)	
		self.matriz_de_valores[self.randomrow][self.randomcolumn] = 2		

	def actualizar_celdas(self):
		for i in range(4):
			for j in range(4):
				if(self.matriz_de_valores[i][j] == 0):
					self.tabla[i][j].configure(
						text="",bg='#CDC1B4')
				else:
					self.tabla[i][j].configure(
						text=str(self.matriz_de_valores[i][j]),
						bg=self.COLOR_FONDO_CELDA[self.matriz_de_valores[i][j]],
						fg=self.CELDA_COLOR_LETRA[self.matriz_de_valores[i][j]])


	#acciones para los botones	
	
	def direccionales(self,event):
		pass
		
	

App()
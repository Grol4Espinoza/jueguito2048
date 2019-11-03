import tkinter as tk
from tkinter import ttk,Frame,CENTER
from tkinter import scrolledtext as st
import random


class App:

	def __init__(self):
		#configuracion de ventana
		self.ventana = tk.Tk()		
		self.ventana.title("2048")
		self.ventana.geometry("480x480")	
		self.ventana.configure(background='#BBADA0'	)
		
		#variables         
		#DICCIONARIO CON COLORES DE ACUERDO AL VALOR
		self.COLOR_FONDO_CELDA =	{
			2: '#EEE4DA',
			4: '#EDE0C8',
			8: '#F2B179',
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
		
		#CREAMOS EVENTOS PARA CUANDO PRESIONES LAS TECLAS
		self.ventana.bind('<Key>',self.direccionales)
		#INICIAR MATRIZ QUE CONTIENE VALORES
		self.matriz_de_valores = self.inicializar_matriz_de_valores()
		
		#INICIAR TABLA
		self.iniciar_tabla()

		#INICIAR JUEGO CON 2 CUADROS "2" RANDOM		
		self.cuadro_random()		
		self.cuadro_random()		
		self.actualizar_celdas()

		print(self.matriz_de_valores)
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
		probabilidad = ['2'] * 10 + ['4']
		self.matriz_de_valores[self.randomrow][self.randomcolumn] = int(random.choice(probabilidad))

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
		self.temporal = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
		key = event.char 
		valor = 3
		reemplazable = True
		self.temporal = self.matriz_de_valores.copy()
		
		self.copia = self.temporal[:]	
		#print("valor copia antes de= "+str(self.copia))
		cambio = False
		print("JAJAJAcambio antes de "+str(cambio))

		if key == 'w':
			cambio = False
			for i in range(4):
				for j in range(4):
					#for k in range(valor):
						if i == 0 :
							self.temporal[i][j] = self.matriz_de_valores[i][j]							
						elif self.matriz_de_valores[i][j] == 0 and self.matriz_de_valores[i-1][j] != 0:
							self.temporal[i][j] = self.matriz_de_valores[i][j]	
						elif self.matriz_de_valores[i][j] != 0 :							
							valor = i
							while valor > 0 :
								if self.matriz_de_valores[valor-1][j] == 0:
									self.temporal[valor-1][j] = self.matriz_de_valores[valor][j]
									self.matriz_de_valores[valor][j] = 0
									cambio = True
								elif self.matriz_de_valores[valor][j] == self.matriz_de_valores[valor-1][j]:							
									self.temporal[valor-1][j] = self.matriz_de_valores[valor][j] * 2
									self.matriz_de_valores[valor][j] = 0
									cambio = True
									valor = 0
								valor -=1								
						elif self.matriz_de_valores[i][j] == self.matriz_de_valores[i-1][j] != 0:							
							self.temporal[i-1][j] = self.matriz_de_valores[i][j] * 2
							self.matriz_de_valores[i][j] = 0
							cambio = True	
							break						
						elif self.matriz_de_valores[i][j] != 0 and self.matriz_de_valores[i-1][j] != 0:
							self.temporal[i][j] = self.matriz_de_valores[i][j]
							
							self.matriz_de_valores = self.temporal															
							#print("i="+str(i)+" j="+str(j)+" temporal = "+str(self.temporal))
						
			self.matriz_de_valores = self.temporal				
			self.actualizar_celdas()	
			#print(self.matriz_de_valores)
			#print("valor copia= "+str(self.copia))	
			print("cambio "+str(cambio))

		elif key == 's':
			cambio = False
			for i in range(3,-1,-1):
				for j in range(4):
					#for k in range(valor):
						if i == 3 :
							self.temporal[i][j] = self.matriz_de_valores[i][j]
						elif self.matriz_de_valores[i][j] == 0 and self.matriz_de_valores[i+1][j] != 0 :
							self.temporal[i][j] = self.matriz_de_valores[i][j]						
						elif self.matriz_de_valores[i][j] != 0 :
							valor = i
							while valor < 3 :
								if self.matriz_de_valores[valor+1][j] == 0:
									self.temporal[valor+1][j] = self.matriz_de_valores[valor][j]
									self.matriz_de_valores[valor][j] = 0
									cambio = True
									#print("ASAAAA["+str(i)+"]["+str(j)+"]= "+str(cambio))
								elif self.matriz_de_valores[valor][j] == self.matriz_de_valores[valor+1][j]:							
									self.temporal[valor+1][j] = self.matriz_de_valores[valor][j] * 2
									self.matriz_de_valores[valor][j] = 0
									cambio = True
									#print("ASAAAADOS["+str(i)+"]["+str(j)+"]= " +str(cambio))
									valor = 3
								valor +=1		
						elif self.matriz_de_valores[i][j] == self.matriz_de_valores[i+1][j] != 0:							
							self.temporal[i+1][j] = self.matriz_de_valores[i][j] * 2
							self.matriz_de_valores[i][j] = 0
							cambio = True
							break
							#print("ASAAAATRES["+str(i)+"]["+str(j)+"]= " +str(cambio))
						elif self.matriz_de_valores[i][j] != 0 and self.matriz_de_valores[i+1][j] != 0:
							self.temporal[i][j] = self.matriz_de_valores[i][j]	
						self.matriz_de_valores = self.temporal
			
			self.matriz_de_valores = self.temporal				
			self.actualizar_celdas()	
			#print(self.matriz_de_valores)
			#print("valor copia= "+str(self.copia))
			print("cambio "+str(cambio))

		elif key == 'a':
			cambio = False
			for i in range(4):
				for j in range(4):
					#for k in range(valor):
						if j == 0 :
							self.temporal[i][j] = self.matriz_de_valores[i][j]							
						elif self.matriz_de_valores[i][j] == 0 and self.matriz_de_valores[i][j-1] != 0:
							self.temporal[i][j] = self.matriz_de_valores[i][j]	
						elif self.matriz_de_valores[i][j] != 0 :
							valor = j
							while valor > 0 :
								if self.matriz_de_valores[i][valor-1] == 0:
									self.temporal[i][valor-1] = self.matriz_de_valores[i][valor]
									self.matriz_de_valores[i][valor] = 0
									cambio = True
								elif self.matriz_de_valores[i][valor] == self.matriz_de_valores[i][valor-1]:							
									self.temporal[i][valor-1] = self.matriz_de_valores[i][valor] * 2
									self.matriz_de_valores[i][valor] = 0
									cambio = True
									valor = 0
								valor -=1
						elif self.matriz_de_valores[i][j] == self.matriz_de_valores[i][j-1] != 0:
							self.temporal[i][j-1] = self.matriz_de_valores[i][j] * 2
							self.matriz_de_valores[i][j] = 0
							cambio = True
							break
						elif self.matriz_de_valores[i][j] != 0 and self.matriz_de_valores[i][j-1] != 0:
							self.temporal[i][j] = self.matriz_de_valores[i][j]							
						self.matriz_de_valores = self.temporal
			self.matriz_de_valores = self.temporal				
			self.actualizar_celdas()	
			#print(self.matriz_de_valores)
			#print("valor copia= "+str(self.copia))
			print("cambio "+str(cambio))

		elif key == 'd':
			cambio = False
			for i in range(4):
				for j in range(3,-1,-1):
					#for k in range(valor):
						if j == 3 :
							self.temporal[i][j] = self.matriz_de_valores[i][j]							
						elif self.matriz_de_valores[i][j] == 0 and self.matriz_de_valores[i][j+1] != 0 :
							self.temporal[i][j] = self.matriz_de_valores[i][j]						
						elif self.matriz_de_valores[i][j] != 0 :
							valor = j
							while valor < 3 :
								if self.matriz_de_valores[i][valor+1] == 0:
									self.temporal[i][valor+1] = self.matriz_de_valores[i][valor]
									self.matriz_de_valores[i][valor] = 0
									cambio = True
								elif self.matriz_de_valores[i][valor] == self.matriz_de_valores[i][valor+1]:							
									self.temporal[i][valor+1] = self.matriz_de_valores[i][valor] * 2
									self.matriz_de_valores[i][valor] = 0
									cambio = True
									valor = 3
								valor +=1	
						elif self.matriz_de_valores[i][j] == self.matriz_de_valores[i][j+1] != 0:
							self.temporal[i][j+1] = self.matriz_de_valores[i][j] * 2
							self.matriz_de_valores[i][j] = 0
							cambio = True
							break
						elif self.matriz_de_valores[i][j] != 0 and self.matriz_de_valores[i][j+1] != 0:
							self.temporal[i][j] = self.matriz_de_valores[i][j]	
						self.matriz_de_valores = self.temporal
			self.matriz_de_valores = self.temporal				
			self.actualizar_celdas()	
			#print(self.matriz_de_valores)
			#print("valor copia= "+str(self.copia))
			print("cambio "+str(cambio))

		print("cambio despues de "+str(cambio))
		#print("valor copia despues = "+str(self.copia))
		#print("valor matriz= "+str(self.matriz_de_valores))
		if cambio:
			self.cuadro_random()
			self.actualizar_celdas()
		else:
			self.actualizar_celdas()
App()
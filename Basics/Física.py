import numpy as np
import matplotlib.pyplot as plt

#Gráficas
x = np.arange(0,10,2)
y1 = 2*x + -1
y2 = 1.5*x + -5

f, ax = plt.subplots(1, 2, figsize=(10, 6))
ax[0].axis([0, 10, -50, 50])
ax[0].set_xlabel('Etiqueta Eje x', fontsize=14)
ax[0].set_ylabel('Etiqueta Eje y', fontsize=14)
ax[0].set_title('Título de la Figura.', fontsize=14)
ax[0].plot(x,y1)
ax[0].plot(x,y2)

ax[1].axis([0, 10, -50, 50])
ax[1].set_xlabel('Etiqueta Eje x', fontsize=14)
ax[1].set_ylabel('Etiqueta Eje y', fontsize=14)
ax[1].set_title('Título de la Figura.', fontsize=14)
ax[1].plot(x,y2, '.b')

#Cambiar color de la linea
#'r' en el ultimo renglón ejecutable como si se tratase de una variable mas

f.show()

---------------------------------------------------------------------------------------------------------

#Movimiento parabolico

g = 9.8   
v0 = 2.88  
theta0_ = 60             

theta0 = theta0_*np.pi/180
tmax = 2*v0*np.sin(theta0)/g

t = np.arange(0, tmax+tmax/50, tmax/50)
x = v0*np.cos(theta0)*t
y = v0*np.sin(theta0)*t - 0.5*g*t**2
vx = v0*np.cos(theta0)*np.ones((len(t)))
vy = v0*np.sin(theta0) - g*t

fig, ax = plt.subplots(figsize=(15, 6))
ax.set_xlim((0, 1))           
ax.set_ylim((0, 0.6))
ax.set_ylabel('Altura (m)', fontsize=16)
ax.set_xlabel('Alcance (m)', fontsize=16)
xpta = np.arange(-2,280,10)
ypta = np.zeros((len(xpta),1))
ax.plot(xpta,ypta,'k',lw=1)
ypta = np.arange(-2,120,10)
xpta = 1.00*np.ones((len(ypta),1))
ax.plot(xpta,ypta,'k',lw=1)
ax.plot(x,y,'k--',lw=2)
txt_title = ax.set_title('')

print("El proyectil se lanzo con una velocidad de",v0, "con un angulo de", theta0_, "grados")
print("La posición de impacto fue en", x[-1-1], "m en un tiempo de",tmax, "s" )
print("La altura maxima fue de", max(y))
print()

------------------------------------------------------------------------------------------------------------------------

#Gráfico para rebotes 

#Ingresar los promedios de ambos rebotes
x1 = 0.625
x2 = 0.714
x3 = 0.783

y1 = 0.475
y2 = 0.521
y3 = 0.568

x = [x1, x2, x3]
y = [y1, y2, y3]
Pendiente_1 = (y3-y2)/(x3-x2)
Pendiente_2 = (y2-y1)/(x2-x1)
Promedio = (Pendiente_1+Pendiente_2)/2

if Pendiente_1 == Pendiente_2:
  print("Los puntos son colineales")
else:
  print("Los puntos no son colineales")

fig, ax = plt.subplots()
ax.plot(x,y,'k',lw=2)
ax.set_title("Pelota de espuma")
ax.scatter(x, y)
ax.set_ylabel('Rebote_2', fontsize=13)
ax.set_xlabel('Rebote_1', fontsize=13)
plt.show()

print("Pendiente 1 = ",Pendiente_1)
print("Pendiente 2 = ",Pendiente_2)
print(Promedio)

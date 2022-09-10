import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

err = []                                                                # Error a graficar
v_inputs = [0,0,0]                                                       # Variables independientes

def hypothesis(v_inputs, data):                                   # Acumulador de los valores de prediccion (hipotesis) por cada época

    h_acum = 0                                                          
    for i in range(len(v_inputs)):                                      
        h_acum = h_acum + v_inputs[i]*data[i]							# Formula para acumular las predicciones
    return h_acum

def g_descent(v_inputs, data, v_output, alfa):                    # Modelo de optimizacion para entrenar el algoritmo 

    aux = list(v_inputs)                                                # Auxiliar con variables independientes
    for j in range(len(v_inputs)):                                      
        gderr_ac = 0                                                    
        for i in range(len(data)):
            gd_error = hypothesis(v_inputs,data[i]) - v_output[i]		# Obtener el error de cada prediccion con el valor real
            gderr_ac = gderr_ac + gd_error*data[i][j]                   
        aux[j] = v_inputs[j] - alfa*(1/len(data))*gderr_ac              # Formula para modelar el Gradient descent
    return aux                                                          # Lista con valores correctamente optimizados

def normalize(data):                                               # Normalizacion de los datos para aumentar su calidad y obtener un mejor
																   # desempeño de los algoritmos

	data = np.asarray(data).T.tolist()                                  # Extraer los datos a una lista transpuesta
	for i in range(1,len(data)):	
		min_val = min(data[i])                          
		max_val = max(data[i])                                          # Obtener el maximo y el minimo valor de la lista
		for j in range(len(data[i])):
			data[i][j] = (data[i][j]-min_val)/max_val-min_val           # Metodo de normalizacion de maximos y minimos
	return np.asarray(data).T.tolist()                                  # Se transponen los datos para regresarlos a la normalidad  

def graph(v_inputs, data,v_output):                                 # Graficar el promedio de los errores en la prediccion

	global err                                                          # Lista de errores por epoca 
	e_ac = 0                                                            # Error acumulado
	for i in range(len(data)):
		h = hypothesis(v_inputs,data[i])                                # Valores de prediccion
		e_ac=+((h-v_output[i])**2)                                      # Acumulamos los errores obtenidos entre cada prediccion y su valor real
		print( "hyp  %f  v_output %f " % (h,  y[i]))   
	e_prom=e_ac/len(data)                                               # Promediar error
	err.append(e_prom)                                                  # Guardar el promedio del error

    # ----------------------     PRUEBAS       ----------------------------------


alfa =.00002  # Learning rate
epochs = 0   # Epocas
 
df = pd.read_csv('SeoulBikeData.csv', encoding= 'unicode_escape')                        # Leer archivo
df_x = df[['Hour', 'Temperature(°C)','Wind speed (m/s)']]
df_y = df[['Rented Bike Count']]                                              # Definir variables dependientes e independientes

x = df_x.values.tolist()
y = df_y.values.tolist()                                          # Convertir las columnas en una lista de datos

arr_y = np.array(y)                                                 
arr_y = np.reshape(arr_y,(len(arr_y),))                             # Definimos el tamaño de la lista de datos convirtiendolo en un nparray

y = arr_y.tolist()                                                  # Ajustar la lista al tamaño redefinido

x_tr, x_t, y_tr, y_t = train_test_split(x,y,random_state=1)         # Unicamente usamos Sklearn para definir los datos de training y datos para el test


while True:

	v_inputs=g_descent(v_inputs, x_tr, y_tr, alfa)              # Optimizar las variables independientes
	print(v_inputs)
	
	graph(v_inputs, x_tr, y_tr)                                 # Guardar el error acumulado para graficar al final

	epochs = epochs + 1                                         # Iterar epoca

	if(epochs == 50):                                           # Parar algoritmo al tener 50 epocas
		print ("final v_inputs:")
		print (v_inputs)
		print(epochs)
		break

plt.plot(err)
plt.show()
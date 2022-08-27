import numpy
import matplotlib.pyplot as plt

err = []

def hipotesis(params, datos):

    hip_ac = 0
    for i in range(len(params)):
        hip_ac = hip_ac + params[i]*datos[i]    # thetan*xn.....+b
        #print(hip_ac)
    return hip_ac

def gradiente_des(params, datos, y, alfa):

    aux = list(params)
    for j in range(len(params)):
        gde_ac = 0
        for i in range(len(datos)):
            gd_error = hipotesis(params,datos[i]) - y[i]
            gde_ac = gde_ac + gd_error*datos[i][j] 
        aux[j] = params[j] - alfa*(1/len(datos))*gde_ac 
    return aux

def normalization(datos):

	datos = numpy.asarray(datos).T.tolist() 
	for i in range(1,len(datos)):	
		min_val = min(datos[i])
		max_val = max(datos[i])
		for j in range(len(datos[i])):
			datos[i][j] = (datos[i][j]-min_val)/max_val-min_val
	return numpy.asarray(datos).T.tolist()

def graficar(params, datos,y):

	global err
	e_ac = 0
	for i in range(len(datos)):
		h = hipotesis(params,datos[i])
		er=h-y[i]
		e_ac=+er**2
		print( "hyp  %f  y %f " % (h,  y[i]))   
	e_prom=e_ac/len(datos)
	err.append(e_prom)


# ----------------------     PRUEBAS       ----------------------------------

#  univariate example
params = [0,0]
datos = [1,2,3,4,5]
y = [2,4,6,8,10]

#  multivariate example trivial
#params = [0,0,0]
#datos = [[1,1],[2,2],[3,3],[4,4],[5,5]]
#y = [2,4,6,8,10]


#  multivariate example
#params = [0,0,0]
#datos = [[1,1],[2,2],[3,3],[4,4],[5,5],[2,2],[3,3],[4,4]]
#y = [2,4,6,8,10,2,5.5,16]

alfa =.1  #  learning rate
for i in range(len(datos)):
	if isinstance(datos[i], list):
		datos[i]=  [1]+datos[i]
	else:
		datos[i]=  [1,datos[i]]
#print ("original datos:")
#print (datos)
datos = normalization(datos)
#print ("scaled samples:")
#print (datos)

epochs = 0

while True:  #  run gradient descent until local minima is reached
	oldparams = list(params)
	#print (params)
	params=gradiente_des(params, datos,y,alfa)	
	graficar(params, datos, y)  #only used to show errors, it is not used in calculation
	#print (params)
	epochs = epochs + 1
	print (epochs)
	if(epochs == 10000 or oldparams == params):   #  local minima is found when there is no further improvement
		print ("datos:")
		print(datos)
		print ("final params:")
		print (params)
		print(epochs)
		break

import matplotlib.pyplot as plt  #use this to generate a graph of the errors/loss so we can see whats going on (diagnostics)
plt.plot(err)
plt.show()
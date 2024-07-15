import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def temperature_calculation_fileinput(path , time , inputs):
  values = {}
  with open(path , 'rt') as file:
      for i in range(inputs):
          values[i] = list(map(float, file.readline().split()))

  temperatures = {}
  for i in range(inputs):
      temperatures[i] = values[i][0] * (time ** 2) + values[i][1] * time + values[i][2]
  return temperatures , values

time_values = np.linspace(0 , 10 , 50)
path = "multiinput.txt"
temperatures , values = temperature_calculation_fileinput(path , time_values , 3)

for i in range(len(temperatures)):
    plt.plot(time_values , temperatures[i] , label = "set" + str(i+1) + ' : ' + ' , '.join(map(str , values[i])))
plt.legend()
plt.xlabel('Time')
plt.ylabel('Temperatures')
plt.grid(True)
plt.title('Weather Modelling using quadratic equation for multi-set file input')
plt.show()
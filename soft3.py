import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def temperature_calculation_fileinput(path , time):
  with open(path , 'rt') as file:
      values = list(map(float, file.readlines()))

  temperature = values[0] * (time ** 2) + values[1] * time + values[2]
  return temperature

time_values = np.linspace(0 , 10 , 50)
path = "input.txt"
temperatures = temperature_calculation_fileinput(path , time_values)

plt.plot(time_values , temperatures , label = "File Input values")
plt.legend()
plt.xlabel('Time')
plt.ylabel('Temperatures')
plt.grid(True)
plt.title('Weather Modelling using quadratic equation for Single-set file input values')
plt.show()
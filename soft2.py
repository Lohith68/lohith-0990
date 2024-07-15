import matplotlib.pyplot as plt
import numpy as np

def temperature_calculation_keyboardinput(time):
  a = float(input("Enter the value for 'a' : "))
  b = float(input("Enter the value for 'b' : "))
  c = float(input("Enter the value for 'c' : "))

  temperature = a * (time ** 2) + b * time + c
  return temperature

time_values = np.linspace(0 , 10 , 50)
temperatures = temperature_calculation_keyboardinput(time_values)

plt.plot(time_values , temperatures , label = "keyboard input values")
plt.legend()
plt.xlabel('Time')
plt.ylabel('Temperatures')
plt.grid(True)
plt.title('Weather Modelling using quadratic equation for keyboard input values')
plt.show()
import matplotlib.pyplot as plt
import numpy as np
def temperature_calculation_hardcoded(time):
    a = 0.1
    b = -1
    c = 3.0

    temperature = a * (time ** 2) + b * time + c
    return temperature
time_values = np.linspace(0 , 10 , 50)
temperatures = temperature_calculation_hardcoded(time_values)

plt.plot(time_values , temperatures , label = "Hard-coded coefficients")
plt.legend()
plt.xlabel('Time')
plt.ylabel('Temperatures')
plt.grid(True)
plt.title('Weather Modelling using quadratic equation for Hard coded variables')
plt.show()
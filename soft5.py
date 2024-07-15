import matplotlib.pyplot as plt
import numpy as np
from google.colab import files

def quadratic_model(time, a, b, c):
    temperature = a * (time**2) + b * time + c
    return temperature

def main():
    try:
        uploaded = files.upload()
        for filename in uploaded.keys():
            with open(filename, "r") as file:
                lines = file.readlines()
                if len(lines) >= 3:
                    a = float(lines[0].strip())
                    b = float(lines[1].strip())
                    c = float(lines[2].strip())

                    time_values = np.linspace(0, 10, 50)
                    temperature_hardcoded = quadratic_model(time_values, a, b, c)

                    plt.figure()
                    plt.plot(time_values, temperature_hardcoded, label=f"{filename} coefficients")
                    plt.xlabel('Time')
                    plt.ylabel('Temperature')
                    plt.legend()
                    plt.title(f"Weather Modeling with Quadratic Equation ({filename} coefficients)")
                    plt.show()
                else:
                    print(f"Error: Insufficient lines in {filename}. Expected 3 lines.")

    except Exception as e:
        print(f"Error: {str(e)}")

if _name_ == "_main_":
    main()
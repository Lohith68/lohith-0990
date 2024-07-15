import numpy as np
import matplotlib.pyplot as plt

def quadratic_model1(time, a1, b1, c1):
    temp1 = a1 * (time**2) + b1 * time + c1
    return temp1

def quadratic_model2(time, a2, b2, c2):
    temp2 = a2 * (time**2) + b2 * time + c2
    return temp2

def main():
    time = np.arange(0, 50, 10)

    # Taking coefficients as input from the user
    a1 = float(input('Enter a value: '))
    b1 = float(input('Enter b value: '))
    c1 = float(input('Enter c value: '))

    # Hard-coded coefficients for quadratic_model2
    a2 = 0.1
    b2 = -1
    c2 = 3.0

    temp1 = quadratic_model1(time, a1, b1, c1)
    temp2 = quadratic_model2(time, a2, b2, c2)

    plt.plot(time, temp1, label='user input coefficients', color='black')
    plt.plot(time, temp2, label='hard-coded coefficients', color='red')
    plt.xlabel('time')
    plt.ylabel('temperature')
    plt.title('Weather modeling with quadratic equation')
    plt.legend()
    plt.show()

if _name_ == "_main_":
    main()
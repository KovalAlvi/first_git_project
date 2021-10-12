# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import matplotlib.pyplot as plt

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi CHANGED, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('New one, Alex')
    x = np.linspace(0, 1, 100)
    plt.plot(np.sin(2* np.pi*x))
    plt.show()

    plt.plot(np.cos(2* np.pi*x))
    plt.plot(np.cos(2* np.pi*x))

    plt.show()


import numpy as np

def plot_boundary(X, theta, ax1):

    a = X[..., 1]
    b = X[..., 2]

    min_x1 = np.max(a)
    max_x1 = np.min(a)
    ia = np.where(a == min_x1)
    ib = np.where(a == max_x1)
    x2_on_min_x1 = b[ia]
    x2_on_max_x1 = b[ib]
    
    #########################################
    # Write your code here
    # Re-arrange the terms in the equation of the hypothesis function, and solve with respect to x2, to find its values on given values of x1
    
    ########################################/
    
    x_array = np.array([min_x1, max_x1])
    y_array = np.array([x2_on_min_x1, x2_on_max_x1])
    ax1.plot(x_array, y_array, c='black', label='decision boundary')
    
    # add legend to the subplot
    ax1.legend()

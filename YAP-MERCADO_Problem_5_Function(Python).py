import matplotlib.pyplot as p
from math import *
# Enter a user-input equation for x(n)
X = input("Enter an equation for x(n): ")
# create a function that will evaluate x(n), which is the user input X, for every n called 
def x(n):
    return eval(X) 

# Create a function that will evaluate y(n) with conditions that depends on the value of n
# This function consists of equations that uses the value of x(n)
def y(n): 
    if n == 0: #First equation where n is equal to 0
        f1 = -1.5*x(n) + 2*x(n+1) - 0.5*x(n+2)
        return f1
    elif n>0 and n<=198: #Second equation where n is greater than 0 but less than or equal to 198
        f2 = 0.5*x(n+1) - 0.5*x(n-1)
        return f2
    elif n == 199: #Final equation where n is equal to 199
        f3 = 1.5*x(n) - 2*x(n-1) +0.5*x(n-2)
        return f3

# Create a list for the value of n from 0 to 199
N = list(range(0,200))
x_n = [x(n) for n in N] #evaluate the equation of x(n) for every n called, which will be stored in an array for the x-values
y_n = [y(n) for n in N] #evaluate the equation of y(n) for every n called, which will be stored in an array for the y-values

# Plot graphs of x(n) and y(n) from n = 0 to n = 199
p.plot(N,x_n,'b',label = 'x(n)') #set the color for the graph of x(n) to blue and label the graph 'x(n)'
p.plot(N,y_n,'g', label = 'y(n)') #set the color for the graph of y(n) to green and label the graph 'y(n)'
p.title('Graph of x(n) and y(n)') #Name the plot or put a title on the graph
p.xlabel('n') #label the x-axis 'n'
p.ylabel('x(n) and y(n)') #label the y-axis 'x(n) and y(n)'
p.legend() #input the legend for x(n) and y(n)
p.show




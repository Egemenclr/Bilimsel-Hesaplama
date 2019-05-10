from math import e

def f(x,y):
    return(4 -x**2 - y**2)
def g(x,y):
    return(1 -e**x -y)
def fx(x,y):
    return(-2*x)
def fy(x,y):
    return(-2*y)
def gx(x,y):
    return(-e**x)
def gy(x,y):
    return(-1)

xi = float(input("x: "))
yi = float(input("y: "))
h=10
while((h-xi) >0.0001):
    h=xi
    deltayi = (-f(xi,yi)*gx(xi,yi) + g(xi,yi)*fx(xi,yi)) / (gx(xi,yi)*fy(xi,yi) - fx(xi,yi)*gy(xi,yi))
    deltaxi = (-f(xi,yi)-fy(xi,yi)*deltayi)/fx(xi,yi)
    xi = xi + deltaxi
    yi = yi + deltayi
print(xi,yi)
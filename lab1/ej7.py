import numpy as np

def main():
    print(integral(f,0,5,0.0001))

def f(x):
    return 2*x + 1

def integral(f,a,b,s):
    sum = 0
    for i in np.arange(a,b,s):
        sum += (s)*f(i)
    return sum

if __name__ == "__main__":
    main()
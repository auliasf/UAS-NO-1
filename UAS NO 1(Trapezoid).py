from trapezoid import*

def Integral(f):
    a = float(input('batas bawah = '))
    b = float(input('batas atas = '))
    n = 100

    integral = trapezoid(f,a,b,n)

    print(a,',',b,',', integral)

    
Integral(lambda x: x**2+4)
Integral(lambda x: x**2-4)
Integral(lambda x: x**2+2)
Integral(lambda x: x**3+4)
Integral(lambda x: x**2-1)
Integral(lambda x: x**4+1)
Integral(lambda x: x**3-1)
Integral(lambda x: x**2-2)
Integral(lambda x: x**4+2)
Integral(lambda x: x**2+6)

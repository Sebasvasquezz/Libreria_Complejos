import math
def sum_complex(a,b):
    parte_real = a[0]+b[0]
    parte_imaginaria = a[1]+b[1]
    return (parte_real,parte_imaginaria)

def rest_complex(a,b):
    parte_real = a[0]-b[0]
    parte_imaginaria = a[1]-b[1]
    return (parte_real,parte_imaginaria)
def mult_complex(a,b):
    parte_real = a[0]*b[0] - a[1]*b[1]
    parte_imaginaria = a[0]*b[1] + a[1]*b[0]
    return parte_real,parte_imaginaria

def div_complex(a,b):
    divisor = b[0]*b[0] + b[1]*b[1]
    if divisor !=0:
        parte_real = (a[0]*b[0] + a[1]*b[1])/divisor
        parte_imaginaria = (b[0]*a[1] - a[0]*b[1])/divisor
        return parte_real,parte_imaginaria
    return print ("El divisor el cero")

def mod_complex(a):
    return ((a[0]*a[0])+(a[1]*a[1]))**(1/2)

def conj_complex(a):
    return a[0],-a[1]

def car_pol_complex(a):
    return mod_complex(a),math.atan2(a[1],a[0])

def pol_car_complex(a):
    return a[0]*math.cos(a[1]),a[0]*math.sin(a[1])

def fase_complex(a):
    return math.atan2(a[1],a[0])
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Ejemplo suma:",sum_complex((3,2),(-5,5.2)))
    print("Ejemplo resta:",rest_complex((3,2),(-5,5.2)))
    print("Ejemplo multiplicación:",mult_complex((3,2),(-5,5.2)))
    print("Ejemplo division:",div_complex((3,2),(-5,5.2)))
    print("Ejemplo modulo:",mod_complex((3,2)))
    print("Ejemplo conjugado:",conj_complex((3,2)))
    print("Verificación propiedad a X conj(A) = mod(A): ",mult_complex(conj_complex((3,2)),(3,2))[0],"=",mod_complex((3,2))**2)
    print("Ejemplo cartesiano a polar:",car_pol_complex((3,2)))
    print("Ejemplo polar a cartesiano:",pol_car_complex((3, math.pi/6)))
    print("Ejemplo fase:",fase_complex((3, 2)))


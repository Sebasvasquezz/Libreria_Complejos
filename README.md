# Librería de Operaciones con Números Complejos

Esta librería de Python brinda funciones para llevar a cabo diferentes operaciones con números complejos. Esto abarca desde operaciones simples hasta transformaciones de sus representaciones y cálculos relacionados con sus características.

## Operaciones Incluidas

La librería consta de las siguientes operaciones para números complejos, los números complejos se representan por medio de tuplas, donde la primera componente es la parte real y la segunda, la imaginaria:

- **Suma:** `sum_complex(complex1, complex2)`
- **Producto:** `mult_complex(complex1, complex2)`
- **Resta:** `rest_complex(complex1, complex2)`
- **División:** `div_complex(complex1, complex2)`
- **Módulo:** `mod_complex(complex)`
- **Conjugado:** `conj_complex(complex)`
- **Conversión Polar a Cartesiano:** `pol_car_complex(complex_polares)`
- **Conversión Cartesiano a Polar:** `car_pol_complex(complex_cartesianas)`
- **Fase:** `fase_complex(complex)`

## Requisitos

- [PyCharm 3.11](https://www.jetbrains.com/pycharm/)

## Uso

1. Clona este repositorio en tu máquina local.
2. Abre el proyecto en PyCharm.
3. Importa el módulo de la librería en tus scripts.
4. Utiliza las funciones de para realizar operaciones con números complejos.

## Ejemplo de Uso

```python
import Lib_complex as lc

# Operaciones básicas
complex1 = (2, 9)
complex2 = (4, -5)
result = lc.mult_complex(complex1, complex2)
print("Multiplicación:", result)

# Conversión cartesiano a polar
complex = (5, -2)
result = lc.car_pol_complex(complex)
print("Complejo en coordenadas polares:", result)
```
## Autor
**Ing. Juan Sebastian Vasquez Vega**
En los primeros 77 puntos no ten�as que preocuparte por si hab�a zumbadores que intervinieran en las casillas de la respuesta (las filas 1 y 2), 
por lo que pod�as recorrer el mundo y por cada vez que encontrabas un barco, usando par�metros y la pila recursiva, obten�as su fila (contando espacios hac�a abajo)
y columna (contando espacios a su izquierda) correspondiente. Al final contabas el id del barco y colocabas la respuesta en la columna correspodiente 
y volv�as a recorrer buscando otro barco si hubiera.

Saltar de esta idea a la de 100 puntos era f�cil observando que en los �ltimos casos pod�an haber casillas que intervinieran al momento de colocar respuestas, 
entonces tienes que usar la pila recursiva guardando el id tambi�n. As� se puede recorrer todo el mundo guardando fila, columna y id del barco y al finalizar el
recorrido, el mundo queda sin zumbadores, para poner las coordenadas usando los regresos recursivos en sus casillas correspondientes.


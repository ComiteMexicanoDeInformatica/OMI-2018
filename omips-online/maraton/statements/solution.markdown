# Marat�n

Para resolver este problema, podemos dividir este problema en dos procesos independientes. El primero ser�a obtener el tiempo en el que cada corredor tarda en llegar a la meta. El segundo ser�a elegir al competidor que menos tiempo tard�.

Para obtener el tiempo que tard� un corredor en llegar podemos simplemente dividir la distancia de el a su meta entre el n�mero de casillas que avanza por paso. Para lograr esto, podemos usar las primeras dos casillas de la columna para implementar una divisi�n en Karel. 

Hay que tener mucho cuidado con los corredores que chocan con la pared y con los que nunca van a llegar a la meta. Esto es, los corredores cuya divisi�n antes descrita no es entera y los corredores cuya velocidad es cero. Para facilitarnos las cosas, sugerimos denotar el tiempo que van a tardad como $0$.

Despu�s de esto, nos queda elegir al corredor que tard� menos tiempo (distinto de 0). Para esto podemos aplicar la siguiente idea. Buscar entre todos los competidores alguno que se haya tardado tiempo 1. Si no lo hay, restarle a todos una unidad al tiempo que hicieron y repetir este procedimiento hasta hallar el 1. Es evidente que al final terminaremos sobre el corredor que hizo menos tiempo en llegar.
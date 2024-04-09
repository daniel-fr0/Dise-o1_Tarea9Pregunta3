# MIN-COVER
## Acerca de la solución planteada
Dado un grafo $G = (N, C)$ se desea encontrar el minimum vertex cover.
Para ello se plantea el siguiente algoritmo de aproximación:
1. Se inicializa un conjunto $R = \emptyset$.
2. Se itera sobre cada $(u, v)\in C$.
3. Mientras existan aristas en $C$:
	- Se agrega $u$ a $R$.
	- Se agrega $v$ a $R$.
	- Se eliminan todas las aristas que tengan a $u$ o $v$ como vértice. Terminamos con $C = C\setminus \{(p,q) \in C\ |\ p = u \vee q = u \vee q = v \vee p = v\}$.

Se puede implementar marcando como visitados a los vertices que se agregan a la respuesta y cualquier otro incidente en estos. Así, se evita tener que eliminar aristas, simplemente se ignoran los vertices marcados como visitados. El algoritmo tiene una complejidad en tiempo de $O(N+C)$ al iterar principalente sobre las aristas del grafo y por la creacion/consulta de la estructura de vértices visitados.

El algoritmo resulta en una aproximación 1-relativa a MIN-COVER, es decir, el tamaño de $R$ es a lo sumo el doble del tamaño del resultado óptimo.

## Demostración
Sea $R$ el conjunto de vértices obtenido por el algoritmo y $R^*$ el conjunto de vértices del resultado óptimo.

Sea $A$ el conjunto de aristas seleccionadas por el algoritmo.

Como se agregan los dos vértices incidentes a cada arista en $A$, se tiene que 
	$$|R| = 2|A|$$

Como cada vez que se selecciona una arista, se eliminan todas las aristas incidentes a los vértices de la arista seleccionada, no pueden haber dos aristas diferentes en $A$ que compartan un vértice. Por lo tanto, $A$ es un conjunto de aristas disjuntas.

Como $R^*$ es un vertex cover, cada arista en $A$ tiene al menos un vértice en $R^*$, por lo tanto $|R^*| \geq |A|$.

Si juntamos esto con la ecuación anterior, se tiene que
	$$|R^*| \geq |A| = \frac{|R|}{2}$$
Y por lo tanto finalmente
	$$|R| \leq 2|R^*|$$

Por lo que se concluye que el algoritmo es una aproximación 1-relativa a MIN-COVER.
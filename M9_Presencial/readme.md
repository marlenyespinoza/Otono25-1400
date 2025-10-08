En cunato terminen los TODO del inventario.py, analizen y respondan las siguientes preguntas:


## 1. Mutabilidad vs. Inmutabilidad: 
En el código, el valor de cada producto en el diccionario inventario es una tupla (por ejemplo, (1200.00, 15)). Si quisieras cambiar solo la cantidad en stock de un producto (el segundo elemento de la tupla) sin cambiar su precio, ¿por qué no podrías hacerlo directamente (como inventario["Laptop"][1] = 20)? ¿Qué modificación al código de la función agregar_producto tendrías que hacer para lograr actualizar el stock de un producto?

# 2. Claves Únicas del Diccionario:
¿Qué sucede si llamas a la función agregar_producto con un producto que ya existe en el diccionario (por ejemplo, agregar_producto("Laptop", 1250.00, 5))? Explica cómo se comporta el diccionario en este caso, y cómo esta propiedad de las claves únicas es útil para garantizar que solo haya una entrada por producto en el inventario.

# 3. Tuplas en Acceso: 
En la función valor_total_inventario, se utiliza la línea for detalles in inventario.values():. ¿Cómo aprovecha el código la naturaleza ordenada de la tupla detalles para acceder al precio y al stock dentro del bucle sin usar un índice numérico ([0], [1])? ¿Por qué fue una buena decisión de diseño usar una tupla en lugar de una lista para almacenar los detalles fijos del producto?
Explicación del Código

    Importación de random: Importamos el módulo random, que nos permite seleccionar elementos aleatorios de una lista.

    Listas de Prefijos y Sufijos: Creamos listas de prefijos y sufijos que se usarán para generar nombres. Puedes personalizar estas listas para incluir más opciones.

    Función generar_nombre_aleatorio():
        Selecciona un prefijo y un sufijo aleatorios usando random.choice().
        Combina el prefijo y el sufijo para formar un nombre y lo retorna.

    Función main():
        Imprime un mensaje de bienvenida.
        Ejecuta un bucle que genera y muestra nombres aleatorios hasta que el usuario decide detenerse.
        Usa input() para preguntar al usuario si quiere generar otro nombre y controla el flujo del bucle basado en la respuesta del usuario.

    Bloque if __name__ == "__main__":: Asegura que la función main() se ejecute solo si el script se ejecuta directamente, no si se importa como módulo en otro script.

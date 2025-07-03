#Variables locales Sólo son visibles en el ámbito donde fueron declaradas.

# def funcion1():
#     a = 3
#     print(a) # 3

# funcion1()
# print(a) # ERROR

# a = 5
# def funcion1():
#     a = 3
#     print(a) # 3

# funcion1()
# print(a) # 5


#Variables globales se pueden acceder en cualquier parte del programa.
# a = 5
# def funcion1():
#     global a
#     a = 3
#     print(a) # 3

# funcion1()
# print(a) # 3

#Variable libre
def funcion_externa():
    mensaje = "Hola desde la función externa"  # Variable en el ámbito "Enclosing"

    def funcion_interna():
        # 'mensaje' es una variable libre aquí, porque no está definida
        # localmente, pero se utiliza.
        print(mensaje)

    funcion_interna()

funcion_externa()
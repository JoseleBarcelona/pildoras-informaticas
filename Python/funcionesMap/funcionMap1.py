class Empleado:

    def __init__(self, nombre, cargo, salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario


    def __str__(self):
        return "{} trabaja como {} y tiene un salario de {}€".format(
            self.nombre, self.cargo, self.salario)

listaEmpleados=[
    Empleado("Juan", "Director", 5000),
    Empleado("Ana", "Presidenta", 4000),
    Empleado("Antonio", "Administrativo", 1800),
    Empleado("Sara", "Secretaria", 1950),
    Empleado("Mario", "Botones", 950)
]

def calculo_comision(empleado):
    if empleado.salario<=1800:
        empleado.salario=empleado.salario * 1.03
    return empleado

listaEmpleadosComision=map(calculo_comision, listaEmpleados)
for empleado in listaEmpleadosComision:
    print(empleado)
class Persona():
    
    def __init__(self, nombre, edad, lugarResidencia):

        self.nombre=nombre
        self.edad=edad
        self.lugarResidencia=lugarResidencia

    def descripcion(self):
        print("Nombre:", self.nombre, "\nEdad:", self.edad, "\nResidencia:", self.lugarResidencia)

    
class Empleado(Persona):

    def __init__(self, salario, antiguedad, nombreEmpleado, edadEmpleado, redidenciaEmpleado):

        super().__init__(nombreEmpleado, edadEmpleado, redidenciaEmpleado)
        self.salario=salario
        self.antiguedad=antiguedad

    def descripcion(self):
        super().descripcion()
        print("Salario: ", self.salario, "\nAntiguedad: ", self.antiguedad)


# Antonio=Persona("Antonio", 55, "España")
# Antonio.descripcion()

Antonio=Empleado(15000, 15, "Antonio", 55, "España")
Antonio.descripcion()

print(isinstance(Antonio, Empleado))
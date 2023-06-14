package Poo.ClasesAbstractas;


public class PersonaPrototipo {
    public static void main(String[] args) {

        Persona[] lasPersonas = new Persona[2];
        lasPersonas[0] = new Empleado2("Luís Conde", 54587.69);
        lasPersonas[1] = new Alumno("Ana López", "Biología");

        for (Persona p : lasPersonas) {
            System.out.println(p.dameNombre() + ", " + p.dameDescripcion());
        }

        }


    }
abstract class Persona{
    private String nombre;


    public Persona(String nom){ //Constructor
        nombre = nom;
    }
    public String dameNombre(){ //Getter
        return nombre;
    }
    public abstract String dameDescripcion(); //Así se declara un método abstracto, por lo que obliga a hacer la clase también abstracta.



}

class Empleado2 extends Persona{

    private double sueldo;
    private final int Id;
    private static int Idsiguiente = 1;


    public Empleado2(String nom, double suel){ //Constructor

        super(nom); //Invocamos al constructor de la clase padre o superclase, para heredar sus métodos.
        sueldo = suel;
        Id = Idsiguiente;
        Idsiguiente++;

    }
    public String dameDescripcion() { //Implementamos el método abstracto de la clase Persona.
        return "empleado de MCM Obres i serveis SA, tiene un Id= " + Id + " con un sueldo= " + sueldo;
    }


}
class Alumno extends Persona{
    private String carrera;


    public Alumno(String nom, String carrera){
        super(nom);
        this.carrera = carrera;

    }
    public String dameDescripcion(){ //Implementamos el método abstracto de la clase Persona.
        return "alumna del Instituto Cervantes, está estudiando la carrera de " + carrera;
    }
}
/*
Luís Conde, empleado de MCM Obres i serveis SA, tiene un Id= 1 con un sueldo= 54587.69
Ana López, alumna del Instituto Cervantes, está estudiando la carrera de Biología
 */
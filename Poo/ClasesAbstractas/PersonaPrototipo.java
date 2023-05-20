package Poo.ClasesAbstractas;

import java.util.Date;
import java.util.GregorianCalendar;

public class PersonaPrototipo {
    public static void main(String[] args) {

        Persona[] lasPersonas = new Persona[2];
        lasPersonas[0] = new Empleado2("Luís Conde", 50000, 2009, 2, 25);
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
    private final Date altaContrato;
    private final int Id;
    private static int Idsiguiente = 1;


    public Empleado2(String nom, double suel, int year, int mes, int dia){ //Constructor

        super(nom); //Invocamos al constructor de la clase padre o superclase, para heredar sus métodos.
        sueldo = suel;
        GregorianCalendar calendario = new GregorianCalendar(year, mes-1, dia);
        altaContrato = calendario.getTime();
        Id = Idsiguiente;
        Idsiguiente++;

    }
    public String dameDescripcion() { //Implementamos el método abstracto de la clase Persona.
        return "este empleado tiene un Id= " + Id + " con un sueldo= " + sueldo;
    }
    public double dameSueldo(){ //GETTER
        return sueldo;
    }
    public Date dameFechaContrato(){ //GETTER
        return altaContrato;
    }
    public void subeSueldo(double porcentaje){ //SETTER
        double aumento = sueldo * porcentaje/100;
        sueldo += aumento;
    }

}
class Alumno extends Persona{
    private String carrera;


    public Alumno(String nom, String carrera){
        super(nom);
        this.carrera = carrera;

    }
    public String dameDescripcion(){ //Implementamos el método abstracto de la clase Persona.
        return "Este alumno está estudiando la carrera de " + carrera;
    }
}
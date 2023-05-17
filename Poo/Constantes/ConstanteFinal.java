package Poo.Constantes;

public class ConstanteFinal {
    public static void main(String[] args) {

        Empleados trabajador1 = new Empleados("José A. Guerrero");
        Empleados trabajador2 = new Empleados("Neus Guerrero");
        Empleados trabajador3 = new Empleados("Núria Barbero");
        trabajador1.cambiaSeccion("Recursos Humanos");

        System.out.println(trabajador1.devuelveDatos());
        System.out.println(trabajador2.devuelveDatos());
        System.out.println(trabajador3.devuelveDatos());
    }
}
class Empleados{

    private final String nombre; //Ponemos la constante Final, para una vez asignado el nombre de una persona, mantenerlo inalterable.
    private String seccion;

    public Empleados(String nom){ //Constructor

        nombre = nom;
        seccion = "Administración";

    }
    public void cambiaSeccion(String seccion){ //SETTER
        this.seccion = seccion;
    }
    public String devuelveDatos(){ //GETTER
        return "El nombre es " + nombre + " y su sección es " + seccion;
    }

}
/*
El nombre es José A. Guerrero y su sección es Recursos Humanos
El nombre es Neus Guerrero y su sección es Administración
El nombre es Núria Barbero y su sección es Administración
 */
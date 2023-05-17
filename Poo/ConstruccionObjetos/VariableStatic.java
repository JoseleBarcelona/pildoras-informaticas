package Poo.ConstruccionObjetos;



public class VariableStatic {
    public static void main(String[] args) {
        Empleados trabajador1 = new Empleados("José A. Guerrero");
        Empleados trabajador2 = new Empleados("Neus Guerrero");
        Empleados trabajador3 = new Empleados("Núria Barbero");
        Empleados trabajador4 = new Empleados("Juanjo Barbero");

        trabajador1.cambiaSeccion("Recursos Humanos"); //Se instancia con el objeto
        trabajador4.cambiaSeccion("Marketing");

        System.out.println(trabajador1.devuelveDatos() + "\n" + trabajador2.devuelveDatos() + "\n" +
                trabajador3.devuelveDatos() + "\n" + trabajador4.devuelveDatos());

        System.out.println(Empleados.dameIdSiguiente());//Se instancia con el nombre de la clase al ser static
    }
}
class Empleados{

    private final String nombre; //Ponemos la constante Final, para una vez asignado el nombre de una persona, mantenerlo inalterable.
    private String seccion;
    private int Id;
    private static int Idsiguiente = 1; //Variable estática

    //Al hacer la variable static, hacemos que sea compartida por la clase, como si fuera el método de clase Math, por
    //lo que no hay que contruir un objeto que tenga una copia de los atributos del construtor, sino que usamos la misma
    //y podemos hacer que aumente la misma cada vez que instanciamos un nuevo objeto, sin saltarnos las reglas de la encapsulación.


    public Empleados(String nom){ //Constructor

        nombre = nom;
        seccion = "Administración";
        Id = Idsiguiente;
        Idsiguiente++;

    }
    public void cambiaSeccion(String seccion){ //SETTER
        this.seccion = seccion;
    }
    public String devuelveDatos(){ //GETTER
        return "El nombre es " + nombre + " y su sección es " + seccion + " con Id:" + Id;
    }

    public static String dameIdSiguiente(){ //Método estático
        return "El Idsiguiente es: " + Idsiguiente;
    }
}
/*
El nombre es José A. Guerrero y su sección es Recursos Humanos con Id:1
El nombre es Neus Guerrero y su sección es Administración con Id:2
El nombre es Núria Barcero y su sección es Administración con Id:3
El nombre es Juanjo Barbero y su sección es Marketing con Id:4
El Idsiguiente es: 5
 */

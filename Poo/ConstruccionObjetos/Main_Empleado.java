package Poo.ConstruccionObjetos;

import java.util.Date;
import java.util.GregorianCalendar;

public class Main_Empleado { // la clase principal que contenga el main, será pública.
    public static void main(String[] args) {

        //Llamamos al constructor y le pasamos los argumentos a los 3 empleados.
        Empleado empleado1 = new Empleado("Paco Gómez", 85000, 1990, 12, 17);
        Empleado empleado2 = new Empleado("Antonio García", 95000, 1995, 6, 2);
        Empleado empleado3 = new Empleado("María Martín", 105000, 2002, 3, 15);

        empleado1.subeSueldo(5);
        empleado2.subeSueldo(5);
        empleado3.subeSueldo(5);

        System.out.println("Nombre: " + empleado1.dameNombre() + " \nSueldo: " + empleado1.dameSueldo() + "€"
        + " \nFecha de Alta: " + empleado1.dameFechaContrato());
        System.out.println("\nNombre: " + empleado2.dameNombre() + " \nSueldo: " + empleado2.dameSueldo() + "€"
        + " \nFecha de Alta: " + empleado2.dameFechaContrato());
        System.out.println("\nNombre: " + empleado3.dameNombre() + " \nSueldo: " + empleado3.dameSueldo() + "€"
        + " \nFecha de Alta: " + empleado3.dameFechaContrato());

        //Otra forma de hacer lo mismo con un array y menos código

        Empleado[] misEmpleados = new Empleado[4];
        misEmpleados[0] = new Empleado("Paco Gómez", 85000, 1990, 12, 17);
        misEmpleados[1] = new Empleado("Antonio García", 95000, 1995, 6, 2);
        misEmpleados[2] = new Empleado("María Martín", 105000, 2002, 3, 15);
        misEmpleados[3] = new Empleado("Margarito");

        for (int i = 0; i < 4; i++){
            misEmpleados[i].subeSueldo(5);
        }
        for (int i = 0; i < 4; i++){
            System.out.println("\nNombre: " + misEmpleados[i].dameNombre() + " \nSueldo: " + misEmpleados[i].dameSueldo() + "€"
                    + " \nFecha de Alta: " + misEmpleados[i].dameFechaContrato());
        }

        //Otra manera más de hacer lo mismo con menos código

        for (Empleado e : misEmpleados){
            System.out.println("\nNombre: " + e.dameNombre() + " \nSueldo: " + e.dameSueldo() + "€"
                    + " \nFecha de Alta: " + e.dameFechaContrato());
        }
    }
}
class Empleado{

    //las clases dentro de un mismo fichero (class Empleado), no pueden llevar el modificador de acceso public.
    public Empleado(String nom, double suel, int year, int mes, int dia){ //Constructor

        //El constructor debe ser public, para ser llamado por otras clases, en especial por el main.

        nombre = nom;
        sueldo = suel;
        GregorianCalendar calendario = new GregorianCalendar(year, mes-1, dia);
        altaContrato = calendario.getTime(); //getTime() devuelve un dato del tipo Date, por lo que se almacena en altaContrato.(Variable de tipo Date).

        //Este método solo tiene como objetivo, el crear una fecha.
        //GregorianCalendar(int year, int month, int dayOfMonth), ponemos mes-1 ya que Enero tiene el índice 0
        //de esa manera cuando pongamos 1 sobreentenderemos que será Enero y no Febrero.
    }
    public Empleado(String nom){ //Sobrecarga de constructor
        this(nom, 3000, 1971, 12, 11);

        //this(); llama al constructor que tenga los parámetros coincidentes entre paréntesis, para rellenar los campos
        //por defecto que desconozcamos del nuevo empleado.
    }
    public String dameNombre(){ //GETTER
        return nombre;
    }
    public double dameSueldo(){ //GETTER
        return sueldo;
    }
    public Date dameFechaContrato(){ //GETTER
        return altaContrato;
    }
    public void subeSueldo(double porcentaje){ //SETTER
        double aumento = sueldo * porcentaje/100; //Variable local
        sueldo += aumento;
    }
    //Las variables globales pueden ir tanto al principio, como al final de la clase.
    private String nombre;
    private double sueldo;     //Date es una variable del tipo objeto
    private Date altaContrato; //Date es una clase, al igual que lo es String, por lo que altaContrato es un objeto de la clase Date

}
/*
Nombre: Paco Gómez
Sueldo: 89250.0€
Fecha de Alta: Mon Dec 17 00:00:00 CET 1990

Nombre: Antonio García
Sueldo: 99750.0€
Fecha de Alta: Fri Jun 02 00:00:00 CEST 1995

Nombre: María Martín
Sueldo: 110250.0€
Fecha de Alta: Fri Mar 15 00:00:00 CET 2002

Nombre: Paco Gómez
Sueldo: 89250.0€
Fecha de Alta: Mon Dec 17 00:00:00 CET 1990

Nombre: Antonio García
Sueldo: 99750.0€
Fecha de Alta: Fri Jun 02 00:00:00 CEST 1995

Nombre: María Martín
Sueldo: 110250.0€
Fecha de Alta: Fri Mar 15 00:00:00 CET 2002

Nombre: Margarito
Sueldo: 3150.0€
Fecha de Alta: Sat Dec 11 00:00:00 CET 1971

Nombre: Paco Gómez
Sueldo: 89250.0€
Fecha de Alta: Mon Dec 17 00:00:00 CET 1990

Nombre: Antonio García
Sueldo: 99750.0€
Fecha de Alta: Fri Jun 02 00:00:00 CEST 1995

Nombre: María Martín
Sueldo: 110250.0€
Fecha de Alta: Fri Mar 15 00:00:00 CET 2002

Nombre: Margarito
Sueldo: 3150.0€
Fecha de Alta: Sat Dec 11 00:00:00 CET 1971
 */

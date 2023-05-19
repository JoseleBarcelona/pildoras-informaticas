package Poo.Herencia.Herencia2;

import java.util.Date;
import java.util.GregorianCalendar;

public class Main_Empleado {
    public static void main(String[] args) {

        Jefatura jefe_RRHH = new Jefatura("Marc Solà", 55000, 2017, 1, 10);

        jefe_RRHH.estableceIncentivo(2570);

        Empleado[] misEmpleados = new Empleado[6];

        misEmpleados[0] = new Empleado("Paco Gómez", 30000, 1990, 12, 17);
        misEmpleados[1] = new Empleado("Antonio García", 50000, 1995, 6, 2);
        misEmpleados[2] = new Empleado("María Martín", 25000, 2002, 3, 15);
        misEmpleados[3] = new Empleado("Margarito");

        misEmpleados[4] = jefe_RRHH; //Polimorfismo. Es lo mismo que poner = new Jefatura("Marc Solà", 3500, 2017, 1, 10);
        misEmpleados[5] = new Jefatura("Federica García", 95000, 2016, 8, 24);

        Jefatura jefa_Finanzas = (Jefatura) misEmpleados[5];
        jefa_Finanzas.estableceIncentivo(250000);

        //Casting (Jefatura) del objeto misEmpleados[5] en el índice 5.
        //Esto es un casting (Refundición) de métodos, para poder llamar a los métodos de la clase Jefatura.
        //Convertimos el objeto misEmpleados en un objeto de la clase Jefatura en el índice definido.

        for (Empleado e : misEmpleados){
            e.subeSueldo(5);
        }
        for (Empleado e : misEmpleados){

            System.out.println("\nNombre: " + e.dameNombre() + " \nSueldo: " + e.dameSueldo() + "€"
                    + " \nFecha de Alta: " + e.dameFechaContrato());
        }
    }
}
class Empleado{

    public Empleado(String nom, double suel, int year, int mes, int dia){ //Constructor

        nombre = nom;
        sueldo = suel;
        GregorianCalendar calendario = new GregorianCalendar(year, mes-1, dia);
        altaContrato = calendario.getTime();
        Id = Idsiguiente;
        Idsiguiente++;

    }
    public Empleado(String nom){ //Sobrecarga de constructor
        this(nom, 3000, 1971, 12, 11);

    }
    public String dameNombre(){ //GETTER
        return nombre + " Id: " + Id;
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

    private final String nombre;
    private double sueldo;
    private final Date altaContrato;
    private final int Id;
    private static int Idsiguiente = 1;


}
class Jefatura extends Empleado{

    public Jefatura(String nom, double suel, int year, int mes, int dia) { //Constructor

        super(nom, suel, year, mes, dia);
    }
    public void estableceIncentivo(double incentivo){ //Setter
        this.incentivo = incentivo;
    }
    public double dameSueldo(){ //Sobrescribimos el método dameSueldo() de la clase padre Empleado.

        double sueldoJefe = super.dameSueldo();
        return sueldoJefe + incentivo;

        /*super llama al método de la clase Empleado, para que no sea una
        llamada recursiva y no se llame a si mismo (No se llame al método dameSueldo() de la clase Jefatura, llama
        al método de la clase Empleado.*/
    }
    public double incentivo;

}
/*
Nombre: Paco Gómez Id: 2
Sueldo: 31500.0€
Fecha de Alta: Mon Dec 17 00:00:00 CET 1990

Nombre: Antonio García Id: 3
Sueldo: 52500.0€
Fecha de Alta: Fri Jun 02 00:00:00 CEST 1995

Nombre: María Martín Id: 4
Sueldo: 26250.0€
Fecha de Alta: Fri Mar 15 00:00:00 CET 2002

Nombre: Margarito Id: 5
Sueldo: 3150.0€
Fecha de Alta: Sat Dec 11 00:00:00 CET 1971

Nombre: Marc Solà Id: 1
Sueldo: 60320.0€
Fecha de Alta: Tue Jan 10 00:00:00 CET 2017

Nombre: Federica García Id: 6
Sueldo: 349750.0€
Fecha de Alta: Wed Aug 24 00:00:00 CEST 2016
 */

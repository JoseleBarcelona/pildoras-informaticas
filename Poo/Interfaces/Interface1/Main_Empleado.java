package Poo.Interfaces.Interface1;

import java.util.Arrays;
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

        System.out.println(jefa_Finanzas.tomarDecisiones("dar más días de vacaciones a los empleados"));

        System.out.println("La jefa " + jefa_Finanzas.dameNombre() + " tiene un bonus de " + jefa_Finanzas.estableceBonus(500) + "€");

        System.out.println("El empleado " + misEmpleados[3].dameNombre() + " tiene un bonus de " + misEmpleados[3].estableceBonus(200) + "€");


        for (Empleado e : misEmpleados){
            e.subeSueldo(5);
        }

        for (Empleado e : misEmpleados){

            System.out.println("\nNombre: " + e.dameNombre() + " \nSueldo: " + e.dameSueldo() + "€"
                    + " \nFecha de Alta: " + e.dameFechaContrato());
        }
    }
}
class Empleado implements Trabajadores{

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


    @Override
    public double estableceBonus(double gratificacion) {
        return Trabajadores.bonusBase + gratificacion;
    }
}
class Jefatura extends Empleado implements Jefes{

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

    @Override
    public String tomarDecisiones(String decision) {
        return "\nUn miembro de la dirección ha tomado la decisión de "+ decision;
    }

    @Override
    public double estableceBonus(double gratificacion) {

        double prima = 2000;
        return Trabajadores.bonusBase + gratificacion + prima;
    }
}
/*

 */

package InputOutput;

import java.util.Scanner;

public class ClaseNumberFormat {
    public static void main(String[] args) {
       double x = 1578.1548;
        System.out.printf("%1.2f", (x/2)); //789,08
        //System.out.printf("%1.3f", x); printf formatea el resultado a que se muestren en pantalla
        //los decimales que se le pasen a través de "%1.5f" siempre dando el primer parámetro entre comillas
        System.out.println("");

        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un número: ");
        double y = entrada.nextDouble();
        System.out.print("La raiz cuadrada del número " + y + " es: ");
        System.out.printf("%1.3f", Math.sqrt(y)); //Da la raiz cuadrada del número con tres decimales

    }
}
/*
789,08
Digite un número:
16
La raiz cuadrada del número 16.0 es: 4,000
 */
package InputOutput;

import java.util.Scanner;

public class ClaseScanner {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in); //System.in significa que metas los datos en la consola
        System.out.println("Digite su nombre: ");
        String nombre = entrada.nextLine();
        System.out.println("Digite su edad: ");
        int edad = entrada.nextInt();

        System.out.println("Su nombre es " + nombre + " y el año que viene tendrá " + (edad + 1) + " años");

    }
}
/*
Digite su nombre:
José
Digite su edad:
51
Su nombre es José y el año que viene tendrá 52 años
 */

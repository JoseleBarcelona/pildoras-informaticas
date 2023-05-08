package EstructControlFlujo.Bucles;

import java.util.Scanner;

public class BucleDoWhile {
    public static void main(String[] args) {
        int aleatorio = (int)(Math.random() * 100);
        Scanner entrada = new Scanner(System.in);
        int numero = 0;
        int intentos = 0;

        /*
        Imaginemos que el número aleatorio sea 0.00005879, con el método (Math.random() * 100) nos daría 0, por lo
        que el búcle jamás entraría en la ejecución, por eso con el do while, nos aseguramos de que por lo menos
        entre la primera vez.
         */
        do{
            intentos++;
            System.out.println("Introduce un número, por favor");
            numero = entrada.nextInt();
            if (aleatorio < numero){
                System.out.println("El número oculto es menor, digite otro número");
            } else if (aleatorio > numero) {
                System.out.println("El número oculto es mayor, digite otro número");
            }

        }while (numero != aleatorio);

        System.out.println("El número es correcto, ¡ENHORABUENA!, lo has conseguido en " + intentos + " intentos.");
    }
}

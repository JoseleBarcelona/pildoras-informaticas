package EstructControlFlujo.Bucles;

import java.util.Scanner;

//ADIVINA EL NÚMERO ALEATORIO DEL 0 AL 100
public class BucleWhile2 {
    public static void main(String[] args) {
        int aleatorio = (int)(Math.random() * 100);

        /*Math.random te devuelve un double desde el 0.0 al 1.0, por lo que si queremos que nos dé un número
        del 0 al 100 sin decimales, primero tenemos que hacer una refundición (CAST) y después multiplicarlo
        por 100 para que el número aleatorio sea del 0 al 100 y por 1000 si quisiéramos que el número
        fuera del 0 al 1000.
         */
        Scanner entrada = new Scanner(System.in);
        int numero = 0;
        int intentos = 0;

        while (numero != aleatorio){
            intentos++;
            System.out.println("Introduce un número, por favor");
            numero = entrada.nextInt();
            if (aleatorio < numero){
                System.out.println("El número oculto es menor, digite otro número");
            } else if (aleatorio > numero) {
                System.out.println("El número oculto es mayor, digite otro número");
            }

        }

        System.out.println("El número es correcto, ¡ENHORABUENA!, lo has conseguido en " + intentos + " intentos.");
    }
}
/*
Introduce un número, por favor
50
El número oculto es mayor, digite otro número
Introduce un número, por favor
60
El número oculto es menor, digite otro número
Introduce un número, por favor
55
El número oculto es mayor, digite otro número
Introduce un número, por favor
57
El número es correcto, ¡ENHORABUENA!, lo has conseguido en 4 intentos.

Process finished with exit code 0
 */

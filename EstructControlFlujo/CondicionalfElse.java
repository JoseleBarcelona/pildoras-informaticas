package EstructControlFlujo;

import java.util.Scanner;

public class CondicionalfElse {
    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite su edad: ");
        int edad = entrada.nextInt();
        if (edad <= 18){
            System.out.println("Su edad está comprendida dentro de la adolescencia");
        } else if (edad <=40) {
            System.out.println("Su edad está comprendida dentro de la juventud madura");
        }else if (edad <=65) {
            System.out.println("Su edad está comprendida dentro de la madurez");
        }else if (edad <=90){
            System.out.println("Está en la edad anciana");
        }else {
            System.out.println("Estoy flipando de que sigas vivo, jajajajaja.");
        }
    }
}

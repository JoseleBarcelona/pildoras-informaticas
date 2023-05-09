package EstructControlFlujo.Bucles;

public class BucleFor {
    public static void main(String[] args) {
        for (int i =0; i < 10; i++) {  //De menor a mayor
            System.out.println("Hola Mundo " + i);
        }
        System.out.println("");
        for (int j = 10; j > 0; j--){
            System.out.println("Hola Mundo " + j); //De mayor a menor
        }
        System.out.println("");
        for (int k = 0; k < 20; k+=3) {
            System.out.println("Hola Mundo " + k);
        }
    }
}
/*
Hola Mundo 0
Hola Mundo 1
Hola Mundo 2
Hola Mundo 3
Hola Mundo 4
Hola Mundo 5
Hola Mundo 6
Hola Mundo 7
Hola Mundo 8
Hola Mundo 9

Hola Mundo 10
Hola Mundo 9
Hola Mundo 8
Hola Mundo 7
Hola Mundo 6
Hola Mundo 5
Hola Mundo 4
Hola Mundo 3
Hola Mundo 2
Hola Mundo 1

Hola Mundo 0
Hola Mundo 3
Hola Mundo 6
Hola Mundo 9
Hola Mundo 12
Hola Mundo 15
Hola Mundo 18
 */

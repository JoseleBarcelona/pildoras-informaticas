package Matrices;

public class ArrayDeArrays1 {
    public static void main(String[] args) {
        int[][] numeros = new int[3][3];

        numeros[0][0] = 1;
        numeros[0][1] = 15;
        numeros[0][2] = 45;
        numeros[1][0] = 88;
        numeros[1][1] = -477;
        numeros[1][2] = -54;
        numeros[2][0] = -23;
        numeros[2][1] = 7;
        numeros[2][2] = 98;

        for (int i = 0; i < numeros.length; i++) {
            for (int j = 0; j < numeros[i].length; j++) {
                System.out.println(numeros[i][j] + " ");
            }
        }
    }
}
/*
1
15
45
88
-477
-54
-23
7
98
 */

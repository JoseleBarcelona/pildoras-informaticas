package Matrices;
//Incrementa cada año a 10.000€ un 10% el primer año, 11% el segundo año y así sucesivamente hasta un 15%
public class ArrayDeArrays3 {
    public static void main(String[] args) {

        double acumulado;
        double interes = 0.10; //10%
        double[][] saldo = new double[6][5];

        for (int i = 0; i < 6; i++) {
            saldo[i][0] = 10000; //Con la variable i va moviendo la primera dimensión, pero fijo la segunda dimensión en el índice 0 a 10000.
            acumulado = 10000;
            for (int j =1; j < 5; j++) {
                acumulado = acumulado + (acumulado * interes);
                saldo[i][j] = acumulado;
            }
            interes = interes + 0.01;
        }
        for (int z = 0; z < 6; z++){
            System.out.println();
            for (int h = 0; h < 5; h++){
                System.out.printf("%1.2f", saldo[z][h]);
                System.out.print("    ");

            }
        }
    }
}
/*
10000,00    11000,00    12100,00    13310,00    14641,00
10000,00    11100,00    12321,00    13676,31    15180,70
10000,00    11200,00    12544,00    14049,28    15735,19
10000,00    11300,00    12769,00    14428,97    16304,74
10000,00    11400,00    12996,00    14815,44    16889,60
10000,00    11500,00    13225,00    15208,75    17490,06
 */

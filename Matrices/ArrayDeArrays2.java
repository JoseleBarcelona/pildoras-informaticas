package Matrices;

public class ArrayDeArrays2 {
    public static void main(String[] args) {

        String[][] paises = {{"España", "Portugal"}, {"Italia", "Francia"}, {"Suecia", "Suiza"}};

        for (int i = 0; i < 3; i++) {  //Bucle for
            for (int j = 0; j < 2; j++){
                System.out.println(paises[i][j]);
            }
        }
        System.out.println();
        for (String[] pais : paises) {  //Bucle foreach
            System.out.println();
            for (String s : pais) {
                System.out.print(s + " ");
            }
        }
    }

}
/*
España
Portugal
Italia
Francia
Suecia
Suiza

España Portugal
Italia Francia
Suecia Suiza
 */
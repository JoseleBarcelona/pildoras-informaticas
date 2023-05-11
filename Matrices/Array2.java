package Matrices;

public class Array2 {
    public static void main(String[] args) {
        String[] paises = new String[8];

        paises[0] = "España";
        paises[1] = "Méjico";
        paises[2] = "Colombia";
        paises[3] = "Perú";
        paises[4] = "Chile";
        paises[5] = "Alemania";
        paises[6] = "Francia";
        paises[7] = "Italia";

        for (int i = 0; i < paises.length; i++) { //Bucle for
            System.out.println("País " + (i+1) + " " + paises[i]);
        }
        System.out.println("");
        for (String pais : paises) { //Bucle for Each
            System.out.println("País " + pais);
        }
    }
}

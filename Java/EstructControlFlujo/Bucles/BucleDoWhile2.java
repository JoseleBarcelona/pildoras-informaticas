package EstructControlFlujo.Bucles;

import javax.swing.*;

/*
AVERIGUAR EL PESO IDEAL DE UNA PERSONA, PARTIENDO DE LAS SIGUIENTE FÓRMULAS GENÉRICAS
- SI ES HOMBRE EL PESO IDEAL SERÁ SU ALTURA - 110
- SI ES MUJER EL PESO IDEAL SERÁ SU ALTURA - 120
 */
public class BucleDoWhile2 {
    public static void main(String[] args) {
        String genero = "";

        do {
            genero = JOptionPane.showInputDialog("Introduzca su género (H/M)");

        }while (genero.equalsIgnoreCase("H") == false && !genero.equalsIgnoreCase("M"));
        //Estas son las dos formas de decir lo mismo complejo o simplificado

        int altura = Integer.parseInt(JOptionPane.showInputDialog("Introduzca su altura en cm"));
        int pesoIdeal = 0;
        if (genero.equalsIgnoreCase("H")){
            pesoIdeal = altura - 110;
        } else if (genero.equalsIgnoreCase("M")) {
            pesoIdeal = altura - 120;
        }
        System.out.println("Su peso ideal es " + pesoIdeal + "kg");
    }
}

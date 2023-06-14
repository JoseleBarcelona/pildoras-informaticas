package Matrices;

import javax.swing.*;

public class Array3 {
    public static void main(String[] args) {
        String[] paises = new String[3];

        for (int i = 0; i < paises.length; i++) {
            paises[i] = JOptionPane.showInputDialog("Introduce país " + (i+1));
        }
        for (String pais : paises) {
            System.out.println("País " + pais);
        }
    }
}

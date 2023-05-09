package EstructControlFlujo.Bucles;

import javax.swing.*;
//AVERIGUA EL FACTORIAL DE UN NÚMERO DADO
//Ejemplo: El factorial de 5 es 5*4*3*2*1=120
public class BucleFor3 {
    public static void main(String[] args) {
        int resultado = 1;
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Introduce un número"));

        for (int i = numero; i > 0; i--) {
            resultado = resultado * i;
        }
        System.out.println("El factorial del número " + numero + " es " + resultado);
    }
}

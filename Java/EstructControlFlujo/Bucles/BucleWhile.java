package EstructControlFlujo.Bucles;

import javax.swing.*;
//ADIVINA LA CONTRASEÑA
public class BucleWhile {
    public static void main(String[] args) {
        String clave = "Núria";
        String password = ""; //con "" se inicializa la variable en un String

        while (clave.equals(password) == false){ //equals() es un método de la clase String y compara si dos cadenas de texto son iguales.
            //Mientras el String clave sea diferente al String password, se estará ejecutando el código
            //que hay por debajo del while.
            password = JOptionPane.showInputDialog("Introduzca la contraseña, por favor");
            if (!clave.equals(password)){ //esto es un simplificación de clave.equals(password) == false
                System.out.println("Contraseña incorrecta, digítela de nuevo por favor.");
            }
        }
        System.out.println("Contraseña correcta, acceso permitido.");
    }
}
/*
Contraseña incorrecta, digítela de nuevo por favor.
Contraseña incorrecta, digítela de nuevo por favor.
Contraseña incorrecta, digítela de nuevo por favor.
Contraseña correcta, acceso permitido.
 */

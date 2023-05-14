package Poo.GetterSetter;

import javax.swing.*;

public class MainCoche2 {
    public static void main(String[] args) {

        Coche2 mazda = new Coche2();

        mazda.establece_color(JOptionPane.showInputDialog("¿Qué color desea para su coche?"));//Llamamos al setter para inicializar el método

        System.out.println(mazda.dime_datos_generales());
        System.out.println(mazda.dime_color()); //Llamamos al getter para mostrarlo

        mazda.configura_asientos(JOptionPane.showInputDialog("¿Desea asientos de cuero?")); //llamamos al setter
        System.out.println(mazda.dime_asientos()); //llamamos al getter

        mazda.configura_climatizador(JOptionPane.showInputDialog("¿Quiere climatizador?")); //llamamos al setter
        System.out.println(mazda.dime_climatizador()); //llamamos al getter

        System.out.println(mazda.dime_peso());

        System.out.println("El precio total del coche, es de " + mazda.dime_precio() + "€");
    }
}

package InputOutput;

import javax.swing.*;

public class ClaseJoptionPane {
    public static void main(String[] args) {
        String nombre = JOptionPane.showInputDialog("Introduzca su nombre, por favor: ");
        int edad = Integer.parseInt(JOptionPane.showInputDialog("Introduca su edad: "));
        //Te devuelve un String, por lo que hay que pasarlo a entero con Integer.parseInt, si queremosoperar aritméticamene con él

        JOptionPane.showMessageDialog(null,"Su nombre es: " + nombre);
        JOptionPane.showMessageDialog(null,"El año que viene tendrá: " + (edad+1));

    }

}

package Poo.Interfaces.ClaseInternaLocal;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Date;
import javax.swing.*;


public class Pruebas {
    public static void main(String[] args) {
        laHora oyente = new laHora();
        Timer joder = new Timer(1000, oyente);
        joder.start();
        JOptionPane.showMessageDialog(null, "Mierda");
        System.exit(0);
    }
}
class laHora implements ActionListener{

    @Override
    public void actionPerformed(ActionEvent e) {
        Date hora = new Date();
        System.out.println(hora);
    }
}

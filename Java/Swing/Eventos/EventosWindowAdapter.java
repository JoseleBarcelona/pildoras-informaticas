package Swing.Eventos;

import javax.swing.*;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

public class EventosWindowAdapter {
    public static void main(String[] args) {

        MarcoVentana2 mimarco = new MarcoVentana2();
        mimarco.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        mimarco.setBounds(300, 300, 500, 350);
        mimarco.setTitle("Ventana1");

        MarcoVentana2 mimarco2 = new MarcoVentana2();
        mimarco2.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        mimarco2.setBounds(800, 300, 500, 350);
        mimarco2.setTitle("Ventana2");
    }
}
class MarcoVentana2 extends JFrame{
    public MarcoVentana2(){

        setVisible(true);
        Ventana2 oyenteVentana = new Ventana2(); //Creamos una instancia de la clase oyente
        addWindowListener(oyenteVentana); //Le decimos al objeto creado, que esté a la escucha
        //addWindowListener(new Ventana2()); //Otra manera es instanciar directamente la clase para que esté a la escucha
    }
}
class Ventana2 extends WindowAdapter {

    @Override
    public void windowOpened(WindowEvent e) {
        System.out.println("Ventana abierta");
    }

    @Override
    public void windowClosing(WindowEvent e) {
        System.out.println("Cerrando ventana");
    }


}

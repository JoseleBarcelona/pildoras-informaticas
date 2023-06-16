package Swing.Eventos;

import javax.swing.*;
import java.awt.event.WindowEvent;
import java.awt.event.WindowListener;

public class EventosVentana1 {
    public static void main(String[] args) {

        MarcoVentana mimarco = new MarcoVentana();
        mimarco.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        mimarco.setBounds(300, 300, 500, 350);
        mimarco.setTitle("Ventana1");

        MarcoVentana mimarco2 = new MarcoVentana();
        mimarco2.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        mimarco2.setBounds(800, 300, 500, 350);
        mimarco2.setTitle("Ventana2");
    }
}
class MarcoVentana extends JFrame{
    public MarcoVentana(){

        setVisible(true);
        Ventana oyenteVentana = new Ventana(); //Creamos una instancia de la clase oyente
        addWindowListener(oyenteVentana);  //Le decimos a objeto creado, que esté a la escucha
    }
}
class Ventana implements WindowListener{

    @Override
    public void windowOpened(WindowEvent e) {
        System.out.println("Ventana abierta");
    }

    @Override
    public void windowClosing(WindowEvent e) {
        System.out.println("Cerrando ventana");
    }

    @Override
    public void windowClosed(WindowEvent e) {
        System.out.println("La ventana ha sido cerrada");
    }

    @Override
    public void windowIconified(WindowEvent e) {
        System.out.println("Ventana minimizada");
    }

    @Override
    public void windowDeiconified(WindowEvent e) {
        System.out.println("Ventana restaurada");
    }

    @Override
    public void windowActivated(WindowEvent e) {
        System.out.println("Ventana activada");
    }

    @Override
    public void windowDeactivated(WindowEvent e) {
        System.out.println("Ventana desactivada");
    }
}

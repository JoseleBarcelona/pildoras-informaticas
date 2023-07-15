package Swing.Eventos;

import javax.swing.*;
import java.awt.*;
import java.awt.event.WindowEvent;
import java.awt.event.WindowStateListener;

public class EventosVentana2 {
    public static void main(String[] args) {
        MarcoEstado mimarco = new MarcoEstado();
        mimarco.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

    }
}
class MarcoEstado extends JFrame{
    public MarcoEstado() {
        setVisible(true);
        setBounds(300, 300, 500, 350);
        CambioEstado nuevoEstado = new CambioEstado();
        addWindowStateListener(nuevoEstado);
    }
}
class CambioEstado implements WindowStateListener{

    @Override
    public void windowStateChanged(WindowEvent e) {

        //Esta es una manera de acceder a las constantes (a través del número entero que nos devuelve la API)

        if (e.getNewState() == 6){
            System.out.println("La ventana está en pantalla completa");

        } else if (e.getNewState() == 0) {
            System.out.println("La pantalla está en su estado normal");
        } else if (e.getNewState() == 1) {
            System.out.println("La pantalla ha sido minimizada");
        }
        System.out.println(e.getNewState()); //Esto te dice cuál es el nuevo estado con el número entero asignado a la constante pertinente

        //Esta es otra manera de hacer lo mismo, a través de invocar a sus métodos (Los cuales tienen el mismo número entero asignado)

        if (e.getNewState() == Frame.MAXIMIZED_BOTH){
            System.out.println("La ventana está en pantalla completa");
        } else if (e.getNewState() == Frame.NORMAL) {
            System.out.println("La pantalla está en su estado normal");
        } else if (e.getNewState() == Frame.ICONIFIED) {
            System.out.println("La pantalla ha sido minimizada");
        }
        System.out.println(e.getNewState());

    }
}

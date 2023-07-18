package Swing.Eventos;

import javax.swing.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.MouseMotionListener;
import java.awt.event.MouseWheelEvent;

public class EventosRaton2 {
    public static void main(String[] args) {
        MarcoRaton2 mimarco = new MarcoRaton2();
        mimarco.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}
class MarcoRaton2 extends JFrame {
    public MarcoRaton2(){
        setVisible(true);
        setBounds(700, 300, 600, 450);
        EventosadaptadosRaton2 ratonAdaptado = new EventosadaptadosRaton2();
        addMouseListener(ratonAdaptado);
        /*EventosDeArrastreDeRaton mueveRaton = new EventosDeArrastreDeRaton();
        addMouseMotionListener(mueveRaton);*/
    }
}
class EventosadaptadosRaton2 extends MouseAdapter{

    @Override
    public void mouseClicked(MouseEvent e) {

        System.out.println("Coordenada x: " + e.getX() + ", Coordenada y: " + e.getY());
    }

    @Override
    public void mouseEntered(MouseEvent e) {
        System.out.println("Has entrado en la ventana");
    }

    @Override
    public void mousePressed(MouseEvent e) {
        System.out.println("Has clicado " + e.getClickCount() + " veces");
    }
}
/*class EventosDeArrastreDeRaton implements MouseMotionListener{

    @Override
    public void mouseDragged(MouseEvent e) {

        System.out.println("Mira que te arrastro");
    }

    @Override
    public void mouseMoved(MouseEvent e) {

        System.out.println("Mira come me mueves");
    }
}*/

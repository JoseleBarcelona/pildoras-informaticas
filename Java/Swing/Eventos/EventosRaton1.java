package Swing.Eventos;

import javax.swing.*;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;

public class EventosRaton1 {
    public static void main(String[] args) {
        MarcoRaton mimarco = new MarcoRaton();
        mimarco.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}
class MarcoRaton extends JFrame {
    public MarcoRaton(){
        setVisible(true);
        setBounds(700, 300, 600, 450);
        EventosDeRaton miraton = new EventosDeRaton();
        addMouseListener(miraton);
    }
}
class EventosDeRaton implements MouseListener {

    @Override
    public void mouseClicked(MouseEvent e) {
        System.out.println("Has clicado!");
    }

    @Override
    public void mousePressed(MouseEvent e) {
        System.out.println("Acabas de presionar");
    }

    @Override
    public void mouseReleased(MouseEvent e) {
        System.out.println("Has soltado el ratón");
    }

    @Override
    public void mouseEntered(MouseEvent e) {
        System.out.println("Acabas de entrar en el marco");
    }

    @Override
    public void mouseExited(MouseEvent e) {
        System.out.println("Acabas de salir del marco");

    }
}

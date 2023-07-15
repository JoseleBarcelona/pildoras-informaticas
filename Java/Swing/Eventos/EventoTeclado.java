package Swing.Eventos;

import javax.swing.*;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

public class EventoTeclado {
    public static void main(String[] args) {
        MarcoConTeclas mimarco = new MarcoConTeclas();
        mimarco.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}
class MarcoConTeclas extends JFrame{
    public MarcoConTeclas() {
        setVisible(true);
        setBounds(700, 300, 600, 450);
        EventoDeTeclado mitecla = new EventoDeTeclado();
        addKeyListener(mitecla); //ponemos a la escucha (A la espera de que se presione una tecla)

    }
}
class EventoDeTeclado implements KeyListener{

    @Override
    public void keyTyped(KeyEvent e) {
        System.out.println(e.getKeyChar());
    }

    @Override
    public void keyPressed(KeyEvent e) {
        System.out.println(e.getKeyCode());
    }

    @Override
    public void keyReleased(KeyEvent e) {
        System.out.println("keyReleased");
    }
}
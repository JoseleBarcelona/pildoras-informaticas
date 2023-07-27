package Swing.Layouts;

import javax.swing.*;
import java.awt.*;

public class ClassBorderLayout {
    public static void main(String[] args) {
        MarcoLayout2 marco = new MarcoLayout2();
        marco.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}
class MarcoLayout2 extends JFrame {
    public MarcoLayout2() {
        setVisible(true);
        setBounds(600, 350, 600, 300);
        setTitle("Prueba Layouts");

        PanelLayout2 lamina = new PanelLayout2();
        add(lamina);

    }
}
class PanelLayout2 extends JPanel {
    public PanelLayout2() {

        setLayout(new BorderLayout(10, 10));
        add(new JButton("Amarillo"), BorderLayout.NORTH);
        add(new JButton("Azul"), BorderLayout.SOUTH);
        add(new JButton("Rojo"), BorderLayout.WEST);
        add(new JButton("Verde"), BorderLayout.EAST);
        add(new JButton("Negro"), BorderLayout.CENTER);
    }
}
